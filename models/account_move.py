# -*- coding: utf-8 -*-

import sys

from odoo import api, fields, models
from odoo.http import request

from . import Tfhka

import base64
import requests
import serial
import time

###################

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from datetime import (timedelta, datetime as pyDateTime, date as pyDate, time as pyTime)

from unidecode import unidecode
import os

###################
class AccountMove(models.Model):
    _inherit = 'account.move'
    
    # definición de los campos que reciben la información que retorna el PrinTax
    ptx_fiscal_invoice = fields.Char("Número de factura fiscal impresa", size = 10)
    ptx_serial_printer = fields.Char("Serial del impresor fiscal", size = 12)
    ptx_printing_date = fields.Datetime('fecha y hora de impresión de la factura fiscal')
    ptx_base_imponible = fields.Float('Total de la base imponible')
    ptx_impuesto_printer = fields.Float('IVA calculado por el impresor')
    ptx_reporte_z = fields.Char("Número de reporte Z asociado a la factura", size = 6)
    
    @api.model
    def imprimir_factura_fiscal(self, id_move):
        
        records = self.env['account.move'].search([('id', '=', id_move)])

        if not records:
            # Manejo de la situación cuando no se encuentran registros
            print("NO hay registros en la factura")
        else:
            records.ensure_one()
            #self.ensure_one()
            print("En proceso -> ", self)
        
            mdlMove = self.env['account.move'].sudo().browse(id_move[0])
            mdlPartner = self.env['res.partner'].sudo().browse(mdlMove.partner_id.id)      

            printer = Tfhka.Tfhka()

            def abrir_puerto():
                try:
                    resp = printer.OpenFpctrl('COM3')
                    if resp:
                        print("Impresora Conectada Correctamente en: COM3")
                        
                        def obtener_parte_entera_precio(numero):
                            # Verificar si el número es válido
                            if not isinstance(numero, (int, float)):
                                raise ValueError("El argumento debe ser un número.")
                                # Obtener la parte entera
                            parte_entera = str(int(numero))
                            # Rellenar con ceros por delante si es necesario
                            parte_entera_ceros = parte_entera.zfill(8)
                            return parte_entera_ceros

                        def obtener_parte_decimal_precio(numero):
                            # Redondear a dos decimales y convertir a cadena
                            parte_decimal_str = str(round(numero % 1, 2))[2:]    
                            # Rellenar con ceros hacia adelante si es necesario
                            parte_decimal_rellenada = parte_decimal_str.zfill(2)    
                            return parte_decimal_rellenada
                            # Verificar si el número es válido
                            if not isinstance(numero, (int, float)):
                                raise ValueError("El argumento debe ser un número.")
                            # Obtener la parte entera
                            parte_entera = str(int(numero))
                            # Rellenar con ceros por delante si es necesario
                            parte_entera_ceros = parte_entera.zfill(5)
                            return parte_entera_ceros
                        def obtener_parte_decimal_cantidad(numero):
                            # Redondear a dos decimales y convertir a cadena
                            parte_decimal_str = str(round(numero % 1, 3))[3:]    
                            # Rellenar con ceros hacia adelante si es necesario
                            parte_decimal_rellenada = parte_decimal_str.zfill(3)    
                            return parte_decimal_rellenada
                        def documentoNF():
                            #Documento No Fiscal
                            printer.SendCmd(str("80$ hola mundo"))
                            printer.SendCmd(str("80¡Esto es un documento de texto"))
                            printer.SendCmd(str("80!Es un documento no fiscal"))
                            printer.SendCmd(str("80*Es bastante util y versatil"))
                            printer.SendCmd(str("80*Test de codigo"))
                            printer.SendCmd(str("810Fin del Documento no Fiscal"))    
                        def encabezado_factura_personalizada():
                            #Factura Personalizada
                            printer.SendCmd(str("iR*"+str(mdlPartner.vat)))#RIF
                            printer.SendCmd(str("iS*"+str(mdlPartner.name)))#RAZON SOCIAL
                            printer.SendCmd(str("i00Direccion: "+str(mdlPartner.name)))#DIRECCION
                            printer.SendCmd(str("i01Telefono: "+str(mdlPartner.phone)))#TELEFONO
                            printer.SendCmd(str("i02CAJERO: 00001"))
                            printer.SendCmd(str("@COMMENT/PRODUCTOS:"))
                        def detalle_factura_personalizada():
                            #Detalle de factura
                            for detalle in mdlMove.invoice_line_ids:
                                mdlDetalle = self.env['account.move.line'].sudo().browse(detalle.id)
                                mdlProd = self.env['product.product'].sudo().browse(mdlDetalle.product_id.id)                
                                lista_impuestos=mdlProd.taxes_id.ids               
                                print("codigo producto:", str(mdlDetalle.product_id.id))
                                print("detalle de producto:", str(mdlProd.display_name))
                                print("lista de impuestos del productos:", lista_impuestos)
                                if 1 in lista_impuestos: #TASA EXENTO DE IVA
                                    printer.SendCmd(" "+obtener_parte_entera_precio(mdlDetalle.price_unit)+
                                    obtener_parte_decimal_precio(mdlDetalle.price_unit)+
                                    obtener_parte_entera_cantidad(mdlDetalle.quantity)+
                                    obtener_parte_decimal_cantidad(mdlDetalle.quantity)+
                                    unidecode("IVA 0%"+str(mdlProd.display_name)))
                                    print("precio:", str(mdlDetalle.price_unit))
                                    print("cantidad:", str(mdlDetalle.quantity))
                                elif 17 in lista_impuestos: # TASA GENERAL IVA DE 16% 
                                    printer.SendCmd("!"+obtener_parte_entera_precio(mdlDetalle.price_unit)+
                                    obtener_parte_decimal_precio(mdlDetalle.price_unit)+
                                    obtener_parte_entera_cantidad(mdlDetalle.quantity)+
                                    obtener_parte_decimal_cantidad(mdlDetalle.quantity)+
                                    unidecode("IVA 16%"+str(mdlProd.display_name)))
                                    print("precio:", str(mdlDetalle.price_unit))
                                    print("cantidad:", str(mdlDetalle.quantity))
                                elif 18 in lista_impuestos: # TASA REDUCIDA IVA DE 8%
                                    printer.SendCmd('"'+obtener_parte_entera_precio(mdlDetalle.price_unit)+
                                    obtener_parte_decimal_precio(mdlDetalle.price_unit)+
                                    obtener_parte_entera_cantidad(mdlDetalle.quantity)+
                                    obtener_parte_decimal_cantidad(mdlDetalle.quantity)+
                                    unidecode("IVA 8%"+str(mdlProd.display_name)))
                                    print("precio:", str(mdlDetalle.price_unit))
                                    print("cantidad:", str(mdlDetalle.quantity))                    
                                elif 19 in lista_impuestos: # TASA ADICIONAL IVA DE 31%
                                    printer.SendCmd("#"+obtener_parte_entera_precio(mdlDetalle.price_unit)+
                                    obtener_parte_decimal_precio(mdlDetalle.price_unit)+
                                    obtener_parte_entera_cantidad(mdlDetalle.quantity)+
                                    obtener_parte_decimal_cantidad(mdlDetalle.quantity)+
                                    unidecode("IVA 31%"+str(mdlProd.display_name)))
                                    print("precio:", str(mdlDetalle.price_unit))
                                    print("cantidad:", str(mdlDetalle.quantity))                                            
                                else:
                                    # Acción por defecto si no coincide con ninguna de las condiciones anteriores
                                    print("La tasa de impuesto del producto no es: Exento, 16%, 8%, 31%, 3%")       
                        def total_subtotal_factura_personalizada():
                            #Subtotal y total de factura
                            printer.SendCmd(str("3"))
                            printer.SendCmd(str("101")) 
    
                        #documentoNF()
                        encabezado_factura_personalizada()
                        detalle_factura_personalizada()
                        total_subtotal_factura_personalizada()
                    else:
                        print("Impresora no Conectada o Error Accediendo al Puerto")
                except Exception:
                    print("Impresora no Conectada o Error Accediendo al Puerto")
            print('Abriendo Puerto COM3....')
            abrir_puerto()          
        
            



