from odoo import fields, models, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    source_project = fields.Char(string="Project", compute='_compute_project')

    def _compute_project(self):
        for rec in self:
            if rec.purchase_id:
                rec.source_project = rec.purchase_id.origin
            else:
                rec.source_project = ''
