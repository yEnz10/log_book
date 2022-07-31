# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LogBook(models.Model):
    _name = 'log.book'
    _description = 'Log Book'

    # required=True, translate=True
    sequence = fields.Integer(string='No.')
    recipient_name = fields.Char(string='Recipient name', required=True)
    destination = fields.Char(string='Destination')
    barcode_number = fields.Char(string='Barcode number (9 Digits)', default=9)
    weight = fields.Char(string='Weight')
    baht = fields.Char(string='Baht')
    satang = fields.Char(string='Satang')
    note = fields.Text(string='Note')
    
class LogBookHIV(models.Model):
    _name = 'log.book.hiv'
    _description = 'Log Book HIV'

    # required=True, translate=True
    unit_number = fields.Char(string='Unit number', required=True)
    