# coding: utf-8
###########################################################################

##############################################################################
{
    "name": "Impresor Fiscal: Facturación fiscal desde Pos y Backend en impresores fiscales PnP y TheFactory HKA",

    "summary": """
        Para facturación fiscal en impresores fiscales de desarrollo de PnP y TheFactory HKA  
        """,

    
    "description": """
        Este módulo utiliza un aplicativo ejecutable (bajo Windows y pronto en Linux) para emitir facturas en impresores fiscales desde
        el módulo de facturación. 
        
        IMPORTANTE: La licencia PERMANENTE del aplicativo se vende aparte (290$ USD), se podra solicitar una licencia demo TEMPORAL para probar el buen funcionamiento del aplicativo.
        CUALQUIER DUDA O PARA SOPORTE Y GUIA: email: odoasys@gmail.com, WhatsApp: (+58)414-4095646
        
        El aplicativo hace la funcion de reenviar el compando de impresion a la impresora fiscal desde el modulo, y el mismo modulo tanto PoS y Facturacion puede modificarlas para agregar mas funciones que ya el aplicativo esta preparado para reenviarla al impresor fiscal, tomando en cuenta el manual de uso y tecnico del aplicativo. La licencia se pega al serial del impresora y el RIF. 
        Estos impresores están adaptados a la legislación de 
        varios paises específicos, en esta versión Venezuela y Panamá.
        
        Esta versión está homologada con los módulos fiscales desarrollados por:
        Desarrollos PNP, C.A. para impresores Fiscales Epson y todas las impresoras de desarrollo de PnP.
        TheFactory HKA para impresores Bixolon, HKA80 y todas las impresoras de desarrollo de TheFactory HKA..
    """,

    "author": "odOASys",
    'sequence': 1,
    "email": 'odoasys@gmail.com',
    "website": "http://www.servitech.com",

    "version": "15.0.1.2.1",
    "price": 0.00,  
    "currency": "EUR",

    "license": "OPL-1",
    "category": "Account/Invoicing",
    "colaborador": "odOASys",
    'depends': ['account' , 'point_of_sale',],
    'images': ['static/description/spoolerfiscal.png'],
    'demo': [ ],
    "data": [ 'views/printax.xml', ],
    'test': [ ],
    "installable": True,
    'application': True,
    'qweb': [],
}
