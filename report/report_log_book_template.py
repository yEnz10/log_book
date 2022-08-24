# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ReportLogBook(models.AbstractModel):
    _name = 'report.log_book.report_deposit_gather'
    _description = ''

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['log.book'].browse(docids)
        print('PRINT=========================> _get_report_values', docs)
        # return {
        #     'doc_ids' : docids,
        #     'doc_model' : self.env['res.company'],
        #     'data' : data,
        #     'docs' : self.env['res.company'].browse(self.env.company.id),
        # }
