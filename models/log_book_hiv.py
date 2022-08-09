# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime

class LogBookHIV(models.Model):
    _name = 'log.book.hiv'
    _description = 'Log Book HIV'
    _order = 'id'
    _rec_name = 'number'
    
    number = fields.Char(string='Form number', required=True, copy=False, readonly=True, 
                         default=lambda self: _('New'))
    create_date = fields.Date(string='Create date', default=datetime.today())
    hiv_line_ids = fields.One2many('log.book.hiv.lines', 'log_book_hiv_id',
                                        string='HIV Lines')
    
    @api.model
    def create(self, vals):
        if vals.get('number', _('New')) == _('New'):
            vals['number'] = self.env['ir.sequence'].next_by_code('log.book.hiv') or _('New')
        res = super(LogBookHIV, self).create(vals)
        return res

class LogBookHIVLines(models.Model):
    _name = 'log.book.hiv.lines'
    _description = ''

    # required=True, translate=True
    log_book_hiv_id = fields.Many2one('log.book.hiv', string='Log Book')
    form_date = fields.Date(string='วันที่', default=datetime.today())
    unit_number = fields.Char(string='Unit number', required=True)
    # ผลการตรวจที่พบปัญหา
    test_res_problem = fields.Char(string='ผลการตรวจที่พบปัญหา')
    call_number = fields.Char(string='เบอร์โทรศัพท์')
    contactable = fields.Char(string='ติดต่อได้')
    cant_contact = fields.Char(string='ติดต่อไม่ได้')
    call_date = fields.Date(string='วันที่โทร', default=datetime.today())
    call_time = fields.Char(string='เวลา') # TODO::
    next_time = fields.Date(string='เวลานัดครั้งถัดไป', default=datetime.today())
    informer = fields.Char(string='ผู้แจ้ง')
    note = fields.Text(string='Note')