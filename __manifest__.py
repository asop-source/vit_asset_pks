# -*- coding: utf-8 -*-
{
    'name': "vit asset pks",

    'summary': """
        Tambah Field Tanggal PKS & Rencana Lelang

        """,


    'author': "asopkarawang@gmail.com",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'asset',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','vit_asset'],

    # always loaded
    'data': [
        'views/views.xml',
    ],

}