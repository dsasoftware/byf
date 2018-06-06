# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    @api.model
    def _get_indicador(self):
        indicador = self.env['hr.indicadores'].search([])
        return indicador and indicador[0].id or False           

    indicadores_id = fields.Many2one(default=_get_indicador)


class hr_payslip_run(models.Model):
    _inherit = 'hr.payslip.run'

    @api.model
    def _get_indicador(self):
        indicador = self.env['hr.indicadores'].search([])
        return indicador and indicador[0].id or False
        
    indicadores_id = fields.Many2one(default=_get_indicador)