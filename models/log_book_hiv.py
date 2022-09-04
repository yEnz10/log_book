# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime, date, time

class LogBookHIV(models.Model):
    _name = 'log.book.hiv'
    _description = 'Log Book HIV'
    # _order = 'id'
    # _rec_name = 'number'
    
    # number = fields.Char(string='Form number', required=True, copy=False, readonly=True, 
    #                      default=lambda self: _('New'))
    create_date = fields.Date(string='วันที่', default=date.today())
    unit_number = fields.Char(string='Unit number', required=True)
    test_res_problem = fields.Char(string='ผลการตรวจที่พบปัญหา')
    call_number = fields.Char(string='เบอร์โทรศัพท์')
    contactable = fields.Char(string='ติดต่อได้')
    uncontactable = fields.Char(string='ติดต่อไม่ได้')
    call_datetime = fields.Datetime(string='วันเวลาที่โทร', default=datetime.today())
    next_time = fields.Datetime(string='เวลานัดครั้งถัดไป', default=datetime.today())
    informer = fields.Many2one('log.book.hiv.informer', string='ผู้แจ้ง', required=True)
    note = fields.Text(string='หมายเหตุ')
    # hiv_line_ids = fields.One2many('log.book.hiv.lines', 'log_book_hiv_id',
    #                                     string='HIV Lines')
    
    @api.model
    def create(self, vals):
    #     if vals.get('number', _('New')) == _('New'):
    #         vals['number'] = self.env['ir.sequence'].next_by_code('log.book.hiv') or _('New')
    #     res = super(LogBookHIV, self).create(vals)
        return 
    
    def action_print_pdf(self):
        print('action_print_pdf ===========================================================>')
        action = self.env.ref('log_book.report_log_book_hiv').sudo()
        print('action=', action)
        print('end action_print_pdf =======================================================>')
        return action.report_action(self)

class LogBookHIVInformer(models.Model):
    _name = 'log.book.hiv.informer'
    _description = ''
    _rec_name = 'full_name'
    
    code = fields.Char(string='รหัส')
    full_name = fields.Char(string='ชื่อ - นามสกุล')
    email = fields.Char('Email', required=True)
    phone = fields.Char(string='เบอร์โทร', size=12)