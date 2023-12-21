# coding: utf-8
###########################################################################

##############################################################################
{
    "name": """Impresor Fiscal The Factory
    
    """,

    "summary": """
        Para facturación fiscal en impresores fiscales  
        """,
    
    "description": """
        Este módulo utiliza permite emitir facturas en impresores fiscales desde
        el módulo de facturación.       
       
        TheFactory HKA, impresores Bixolon, HKA80 y todas las impresoras de desarrollo de TheFactory HKA..
    """,

    "author": "Marycela Vera",
    'sequence': 1,
    "email": 'veramarycela@gmail.com',
    "website": "http://www.servitech.com",

    "version": "15.0.1.2.1",
    "price": 0.00,  
    "currency": "VES",

    "license": "OPL-1",
    "category": "Account/Invoicing",
    "colaborador": "Marycela Vera",
    'depends': ['account' , 'point_of_sale',],
    'images': ['static/description/spoolerfiscal.png'],
    'demo': [ ],
    "data": [ 'views/printax.xml'         
             ],
    'test': [ ],
    "installable": True,
    'application': True,
    'qweb': [],
}
