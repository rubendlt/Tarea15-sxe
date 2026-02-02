# -*- coding: utf-8 -*-
# from odoo import http


# class NivelSueno(http.Controller):
#     @http.route('/nivel_sueno/nivel_sueno', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nivel_sueno/nivel_sueno/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nivel_sueno.listing', {
#             'root': '/nivel_sueno/nivel_sueno',
#             'objects': http.request.env['nivel_sueno.nivel_sueno'].search([]),
#         })

#     @http.route('/nivel_sueno/nivel_sueno/objects/<model("nivel_sueno.nivel_sueno"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nivel_sueno.object', {
#             'object': obj
#         })

