# -*- coding: utf-8 -*-
# from odoo import http


# class C:\users\phong\documents\101\odoo\mymodules\logBook(http.Controller):
#     @http.route('/c:\users\phong\documents\101\odoo\mymodules\log_book/c:\users\phong\documents\101\odoo\mymodules\log_book/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/c:\users\phong\documents\101\odoo\mymodules\log_book/c:\users\phong\documents\101\odoo\mymodules\log_book/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('c:\users\phong\documents\101\odoo\mymodules\log_book.listing', {
#             'root': '/c:\users\phong\documents\101\odoo\mymodules\log_book/c:\users\phong\documents\101\odoo\mymodules\log_book',
#             'objects': http.request.env['c:\users\phong\documents\101\odoo\mymodules\log_book.c:\users\phong\documents\101\odoo\mymodules\log_book'].search([]),
#         })

#     @http.route('/c:\users\phong\documents\101\odoo\mymodules\log_book/c:\users\phong\documents\101\odoo\mymodules\log_book/objects/<model("c:\users\phong\documents\101\odoo\mymodules\log_book.c:\users\phong\documents\101\odoo\mymodules\log_book"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('c:\users\phong\documents\101\odoo\mymodules\log_book.object', {
#             'object': obj
#         })
