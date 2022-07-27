# -*- coding: utf-8 -*-
{
    'name': "Log Book",
    'sequence': -100,
    'summary': """
        Log Book Software
    """,
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Productivity',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/log_book_views.xml"
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
