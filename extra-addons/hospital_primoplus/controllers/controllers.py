# -*- coding: utf-8 -*-
# from odoo import http


# class Hospital.paciente(http.Controller):
#     @http.route('/hospital_primoplus/hospital_primoplus', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_primoplus/hospital_primoplus/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_primoplus.listing', {
#             'root': '/hospital_primoplus/hospital_primoplus',
#             'objects': http.request.env['hospital_primoplus.hospital_primoplus'].search([]),
#         })

#     @http.route('/hospital_primoplus/hospital_primoplus/objects/<model("hospital_primoplus.hospital_primoplus"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_primoplus.object', {
#             'object': obj
#         })

