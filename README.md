# Modulo de comucicacion con el ejecutable bajo Windows 64/32 (Pronto en Linux)

Descripción:

Compatible para Odoo 13, 14 y 15 (pronto v16), Community & Enterprize

El módulo en Odoo para imprimir a impresor fiscal via el programa server/spooler fiscal

Odoo >> spooler >> Impresora Fiscal

Versión 1.2.1 [compatible con la nueva providencia del IGTF]
Compatible con IMPRESORAS FISCALES THE FACTORY HKA Y PNP EPSON Venezuela / Panama
La licencia demo y/o permanente del aplicativo ejecutable se solicita con serial del impresor y RIF

El módulo utiliza el programa ejecutable bajo Windows para emitir facturas en impresores fiscales desde
facturación y POS. Estos impresores están adaptados a la legislación de
varios paises específicos; en esta versión Venezuela y Panamá.

Esta versión está homologada con los módulos fiscales desarrollados por:
- Desarrollos PNP, C.A.(impresores Epson y compatibles de desarrollos PnP).
- TheFactory HKA para impresores Bixolon y HKA80 (Y compatibles de desarrollos TheFactory ).
- Desarrollos privados



El programa hace un puente entre módulo de facturación Odoo y un impresor fiscal. Desde Odoo se envían los mensajes al aplicativo, este lo interpreta y lo adapta al impresor configurado. El aplicativo responde al Odoo con el resultado de la operación sea exitosa o fallida. 

Vendemos la licencia del programa, un solo pago. se da periodo de prueba con modulos POS y facturacion compatible y probado con Odoo 13,14 y 15 (pronto v16). Aparte del manual de uso y comandos desde Odoo - Programación Python. El modulo en Odoo es codigo abierto y lo puede modificar y desarrollar y usar su propio modulo que desarrolle en Odoo.

** Módulo para la emisión de facturas fiscales a través del aplicativo desde facturación
Este módulo utiliza el programa PrinTax para emitir facturas en impresores fiscales desde el módulo de facturación normal en Odoo
.
** Módulo para la emisión de facturas fiscales a través del programa aplicativo desde el POS.
Este módulo utiliza el programa aplicativo para emitir facturas en impresores fiscales desde el módulo de punto de venta (POS). 


Instalación
El aplicativo se debe instalar en el equipo que esté conectado físicamente y directo al impresor fiscal, para instalarlo se ejecuta el instalador y se le da aceptar en las diferentes opciones.
Se agrega una impresora con direccion IP usando la IP de la PC donde esta instalado el aplicativo.

Tabla de contenido del manual

Manual de Operación Versión 1.2.1............... 3

Instalación ............... 3

Ejecución del aplicativo ............... 3

Desactivación de botones ............... 5

Operación regular............... 6

Apertura de caja ............... 7

Reporte X ............... 7

Reporte Z ............... 8

Copia de factura ............... 8

Tarifas de Impuesto ............... 9

Manual de Programación Versión 1.2.1 ...............11

Envío de comando desde ODOO - Programación Python ............... 11

Tipos de operación ............... 12

Parametros según tipo de mensaje ............... 13

Apertura y cierre de caja ............... 15

Carga de cajeros ............... 15

Carga de medios de pago ............... 16

Encabezados y pie de página ...............16

Impresión de facturas ............... 16

Ejemplo de factura & Reimpresión de facturas ............... 18

Notas de crédito & Reimpresión de notas de crédito ............... 19

Documentos no fiscales & Tarifas de impuesto ............... 20

Reimpresión de reporte de cierre Z ............... 21
