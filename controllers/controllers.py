# -*- coding: utf-8 -*-
# from odoo import http


# class Custom/repositories/customs/decoSaleOrder(http.Controller):
#     @http.route('/custom/repositories/customs/deco_sale_order/custom/repositories/customs/deco_sale_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom/repositories/customs/deco_sale_order/custom/repositories/customs/deco_sale_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom/repositories/customs/deco_sale_order.listing', {
#             'root': '/custom/repositories/customs/deco_sale_order/custom/repositories/customs/deco_sale_order',
#             'objects': http.request.env['custom/repositories/customs/deco_sale_order.custom/repositories/customs/deco_sale_order'].search([]),
#         })

#     @http.route('/custom/repositories/customs/deco_sale_order/custom/repositories/customs/deco_sale_order/objects/<model("custom/repositories/customs/deco_sale_order.custom/repositories/customs/deco_sale_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/repositories/customs/deco_sale_order.object', {
#             'object': obj
#         })
