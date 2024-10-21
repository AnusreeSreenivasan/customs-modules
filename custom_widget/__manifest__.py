{
    'name': 'Custom Widget',
    'author': "nin",
    'license': "LGPL-3",
    'version': '17.0.1.1',
    'depends': ['base'],
    'data': [
            "security/ir.model.access.csv",
            "view/custom_widget.xml",

        
    ],
    'assets': {
        'web.assets_backend': [
            # 'custom_widget/static/src/js/custom_widget.js', 
        ],
    },
    'installable': True,
    'auto_install': False,
}