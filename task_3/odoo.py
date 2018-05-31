from xmlrpc import client
info = client.ServerProxy('https://demo.odoo.com/start').start()
url, db, username, password = \
    info['host'], info['database'], info['user'], info['password']

common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()

uid = common.authenticate(db, username, password, {})


models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# tas ids with 'it' in their names
categories_ids = models.execute_kw(db, uid, password,
    'res.partner.category', 'search',
    [[['name', 'ilike', '%it%']]], {})

# partners with previously defined categories
partners_ids  = models.execute_kw(db, uid, password,
                                'res.partner', 'search',
                                [[['category_id', '=', categories_ids]]], {})


orders = models.execute_kw(db, uid, password,
                            'purchase.order', 'search_read',
                            [[['partner_id', '=', partners_ids]]], {})








self.env.cr.execute("Select * from ir_model")





