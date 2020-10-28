# -*- coding: utf-8 -*-
# from odoo import http


# class DdExternalId(http.Controller):
#     @http.route('/dd_external_id/dd_external_id/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dd_external_id/dd_external_id/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dd_external_id.listing', {
#             'root': '/dd_external_id/dd_external_id',
#             'objects': http.request.env['dd_external_id.dd_external_id'].search([]),
#         })

#     @http.route('/dd_external_id/dd_external_id/objects/<model("dd_external_id.dd_external_id"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dd_external_id.object', {
#             'object': obj
#         })
