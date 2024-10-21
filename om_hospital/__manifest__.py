{
    'name':'Hospital Management System',
    'author':'Odoo Mates',
    'website':'www.odoomates.tech',
    'summary':'Oddo 16 Development',
    'depends':['mail'],
    'data':[
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/menu.xml',
        'views/appointment.xml'
    ],
    'application':True,
    
}