# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class c:\users\phong\documents\101\odoo\mymodules\log_book(models.Model):
#     _name = 'c:\users\phong\documents\101\odoo\mymodules\log_book.c:\users\phong\documents\101\odoo\mymodules\log_book'
#     _description = 'c:\users\phong\documents\101\odoo\mymodules\log_book.c:\users\phong\documents\101\odoo\mymodules\log_book'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
