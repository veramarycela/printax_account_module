# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.http import request

import base64
import requests
import serial

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

        
        #cmd += "CNM=" + str(mdlPartner.name) + "\n"
        #cmd += "TXT=Numero de orden " + nro_orden + "\n"
        #cmd += "TXT=" + mdlPartner.contact_address + "\n"
        #cmd += "TXT=Telefono " + str(mdlPartner.phone) + "\n"

        # Cada linea debe tener el porcentaje de IVA, este porcentaje debe estar registrado en el impresor fiscal
        # se coloca 0 cuandidso es exento de impuesto
        
        #ENCABEZADO Y PIE DE PAGINA
        cmd = "STX"
        cmd += "PH"
        cmd += "01"
        cmd += "Bienvenido"      
        cmd += "LRC" + "\n"
        print(cmd)

        #CI DEL CLIENTE O RIF
        cmd = "STX"
        cmd += "iR*"     
        cmd += str(mdlPartner.vat)
        cmd += "ETX"
        cmd += "LRC" + "\n"
        print(cmd)

        #RAZON SOCIAL DEL CLIENTE
        cmd = "STX"
        cmd += "iS*"     
        cmd += str(mdlPartner.name)
        cmd += "ETX"
        cmd += "LRC" + "\n"
        print(cmd)

        #INFORMACIÓIN ADICIONAL DEL CLIENTE
        cmd = "STX"
        cmd += "¡" 
        cmd += "00"    
        cmd += str(mdlPartner.contact_address) #str(mdlPartner.street) + str(mdlPartner.street2) + str(mdlPartner.city)
        cmd += "ETX"
        cmd += "LRC" + "\n"
        print(cmd)        

        #DETALLE DE FACTURA

        for detalle in mdlMove.invoice_line_ids:
            mdlDetalle = self.env['account.move.line'].sudo().browse(detalle.id)
            mdlProd = self.env['product.product'].sudo().browse(mdlDetalle.product_id.id)
            
            cmd = "STX"
            cmd += "!"            
            cmd += str(mdlDetalle.price_unit)            
            cmd += str(mdlDetalle.quantity) + "|"
            cmd += str(mdlDetalle.product_id.id)+ "|"
            cmd += mdlProd.display_name 
            cmd += "ETX"
            cmd += "LRC" + "\n"
            print(cmd)
            
            #SUBTOTAL
            cmd = "STX"
            cmd += "3" #imprime en el papel
            cmd += "ETX"
            cmd += "LRC" + "\n"
            print(cmd)     

        #TOTALIZAR FACTURA
        cmd = "STX"
        cmd += "01" #metodo de pago efectivo efectivo
        cmd += "ETX"
        cmd += "LRC" + "\n"
        print(cmd)     

        #MENSAJE COMERCIAL DE FACTURA
        cmd = "STX"
        cmd += "@" 
        cmd += "!#####Gracias por su compra#####!"
        cmd += "ETX"
        cmd += "LRC" + "\n"
        print(cmd)           

           

        # Configurar la conexión serial
        #puerto = 'COM1'  # Cambia esto por el nombre del puerto en tu sistema
        #velocidad = 9600  # Cambia esto por la velocidad de baudios adecuada
        #conexion = serial.Serial(puerto, velocidad)
        #try:
        #    conexion = serial.Serial(puerto, velocidad)
        #except serial.SerialException as e:
        #    print(f"Error al abrir el puerto serial: {e}")

        # Enviar datos
        #datos = b'Hola, mundo!'  # Convertir los datos a bytes
        #conexion.write(datos)
        
        # Leer la respuesta
        #respuesta = conexion.readline()
        #print(respuesta)

