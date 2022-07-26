# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LogBook(models.Model):
    _name = "log.book"
    _description = "Log Book"

    # required=True, translate=True
    name = fields.Char(string='Name', required=True)
    destination = fields.Char(string='Destination')