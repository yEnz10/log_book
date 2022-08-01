# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LogBook(models.Model):
    _name = 'log.book'
    _description = 'Log Book'
    _order = "sequence,id"

    # required=True, translate=True
    sequence = fields.Integer(string='No.', readonly=1)
    # log_book_seq = fields.Integer(string='No.', readonly=1)
    recipient_name = fields.Char(string='Recipient name', required=True)
    destination = fields.Char(string='Destination')
    barcode_number = fields.Char(string='Barcode number (9 Digits)')
    weight = fields.Char(string='Weight')
    baht = fields.Char(string='Baht')
    satang = fields.Char(string='Satang')
    note = fields.Text(string='Note')

    # @api.model
    # def create(self, vals):
    #     print("Log Book create vals ",vals)
    #     vals['log_book_seq'] = self.env['ir.sequence'].next_by_code('log.book')
    #     return super(LogBook, self).create(vals)
    
class LogBookHIV(models.Model):
    _name = 'log.book.hiv'
    _description = 'Log Book HIV'

    # required=True, translate=True
    unit_number = fields.Char(string='Unit number', required=True)
    