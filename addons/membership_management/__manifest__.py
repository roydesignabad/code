{
    'name': 'Membership Management',
    'version': '16.0.1.0.0',
    'category': 'Membership',
    'summary': 'Manage members, renewals, branches and approvals',
    'author': 'Your Name',
    'website': '',
    'license': 'AGPL-3',
    'depends': ['base', 'sale'],
    'data': [
        'security/membership_security.xml',
        'security/ir.model.access.csv',
        'views/membership_views.xml',
    ],
    'application': True,
}
