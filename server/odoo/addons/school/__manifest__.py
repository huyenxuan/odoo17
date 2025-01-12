# -*- coding: utf-8 -*-
{
    'name' : 'School Management',
    'author' : 'NXH10',
    'version' : '1.1',
    'summary': 'School Management',
    'sequence': 2,
    'description': """
        School Management
    """,
    'category': 'School/Management',
    'depends': ['base'],
    'data': [
        'views/school_information.xml',
        'sercurity/ir.model.access.csv',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
