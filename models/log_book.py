# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LogBook(models.Model):
    _name = 'log_book.profile'

    name = fields.Char(string ="Name")
    email = fields.Char(string = "Email")
    phone = fields.Char(string ="Phone")
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
