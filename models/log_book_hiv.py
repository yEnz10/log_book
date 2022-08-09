# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class LogBookHIV(models.Model):
    _name = 'log.book.hiv'
    _description = 'Log Book HIV'
    _order = 'id'
    # _rec_name = 'number'