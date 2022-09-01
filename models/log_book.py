# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api, _
from datetime import datetime, date
from odoo.exceptions import ValidationError
class LogBook(models.Model):
    _name = 'log.book'
    _description = 'Log Book'
    _order = 'create_date desc'
    _rec_name = 'number'

    # line_number = fields.Char(string='ที', required=True, copy=False, readonly=True, 
    # default=lambda self: _('New'))
    create_date = fields.Date(string='วันที่', required=True, readonly=True, default=date.today())
    number = fields.Char(string='Log number', required=True, copy=False, readonly=True, 
                         default=lambda self: _('New'))
    postal_type = fields.Many2one('log.book.postal.type', string='ประเภท', required=True)
    recipient_name = fields.Char(string='นามผู้รับ', required=True)
    destination = fields.Char(string='ปลายทาง')
    barcode = fields.Char(string='Barcode (9 ตัวเลข)', size=9, required=True)
    weight = fields.Float(string='น้ำหนัก')
    service_charge = fields.Float(string='ค่าบริการ')
    note = fields.Text(string='หมายเหตุ')

    
    
    # receiver_line_ids = fields.One2many('log.book.receiver.lines', 'log_book_id',
    #                                     string='Receiver Lines')
    # image = fields.Binary(string='Log brand')
    
    @api.model
    def create(self, vals):
        if vals.get('number', _('New')) == _('New'):
            vals['number'] = self.env['ir.sequence'].next_by_code('log.book') or _('New')
            
        res = super(LogBook, self).create(vals)
        return res
    
    def action_print_pdf(self):
        print('action_print_pdf ==========================================================>')
        print('self=', self.read())
        # print('data-=>>>>>>>>>>', self.env.context)
        ptt_code = ''
        for rec in self:
            if not ptt_code:
                ptt_code = rec.postal_type.code
                
            if ptt_code != rec.postal_type.code:
                raise ValidationError(_("เลือกประเภทใบฝากได้เพียง 1 ประเภทที่ใช้ในการพิมพ์ใบฝากรวม"))

        action = self.env.ref('log_book.report_deposit_gather').sudo()
        print('end action_print_pdf =======================================================>')
        return action.report_action(self)
        
        # print('LOG==========================================================', self)
        # view = self.env.ref('sh_message.shmessage_wizard')
        # view_id = view and view.id or False
        # context = dict(self._context or {})
        # context['message'] = "Tasks create successfully"
        # return {
        #     'name': 'Success',
        #     'type': 'ir.actions.act_window',
        #     'view_type': 'form',
        #     'view_model': 'form',
        #     'res_model': 'sh.message.wizard',
        #     'views': [(view.id, 'form')],
        #     'view_id': view.id,
        #     'target': 'new',
        #     'context': context,
        # }
        # return self.env.ref('log_book.report_deposit_sum').report_action(self)
        # print("_print_pdf==>", self, type(self))
        # print('LOG==========================================================')
        # for rec in self:
        #     print('rec==============>', rec.postal_type.code)

        # print('END==========================================================')
        # print('vals================>', self['number'], type(self['number']))
    # @api.model
    # def _create_at_log(self, vals):
    #     res =  datetime.year()
    #     return res
    
class LogBookPostalType(models.Model):
    _name = 'log.book.postal.type'
    _description = ''
    _rec_name = 'name'
    # required=True, translate=True
    code = fields.Char(string='Code')
    name = fields.Char(string='Name')
    color = fields.Integer(string='Color')

# # Master Log_Book_Type
# class LogBookReceiverLines(models.Model):
#     _name = 'log.book.receiver.lines'
#     _description = ''

#     # required=True, translate=True
#     log_book_id = fields.Many2one('log.book', string='Log Book')
#     name = fields.Char(string='Name', required=True)
#     destination = fields.Char(string='Destination')
#     barcode = fields.Char(string='Barcode (9 digit)', size=9, required=True)
#     weight = fields.Float(string='Weight')
#     baht = fields.Integer(string='Baht')
#     satang = fields.Float(string='Satang')
#     note = fields.Text(string='Note')