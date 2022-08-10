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
    'version': '2.0',
    'depends': ['base'],
    'data': [
        'data/log_book_data.xml',
        # 'report/log_book_header_footer.xml'
        # 'report/report_log_book_template.xml',
        # 'report/report.xml',
        'security/ir.model.access.csv',
        'views/log_book_views.xml',
        # 'views/log_book_hiv_views.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
