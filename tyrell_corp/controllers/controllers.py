# -*- coding: utf-8 -*-
from odoo import http

# class TyrellCorp(http.Controller):
#     @http.route('/tyrell_corp/tyrell_corp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tyrell_corp/tyrell_corp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tyrell_corp.listing', {
#             'root': '/tyrell_corp/tyrell_corp',
#             'objects': http.request.env['tyrell_corp.tyrell_corp'].search([]),
#         })

#     @http.route('/tyrell_corp/tyrell_corp/objects/<model("tyrell_corp.tyrell_corp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tyrell_corp.object', {
#             'object': obj
#         })