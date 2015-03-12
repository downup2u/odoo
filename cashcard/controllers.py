# -*- coding: utf-8 -*-
from openerp import http

# class Cashcard(http.Controller):
#     @http.route('/cashcard/cashcard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cashcard/cashcard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cashcard.listing', {
#             'root': '/cashcard/cashcard',
#             'objects': http.request.env['cashcard.cashcard'].search([]),
#         })

#     @http.route('/cashcard/cashcard/objects/<model("cashcard.cashcard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cashcard.object', {
#             'object': obj
#         })