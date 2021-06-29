from odoo import models, fields, api, _

class QcCustom(models.Model):
	_inherit = 'qc.inspection'

	description = fields.Text(string='Description')
	date = fields.Date(string='Date')
	qty_sample = fields.Float(string='Qty Sample', default=1.00)
	so_ref = fields.Many2one('sale.order', 'SO Reference', store=True)
	product_ref = fields.Many2one('product.product', 'Product', store=True)	
	child_line = fields.One2many('qc.inspection.child', 'parent_id', readonly=False, ondelete='cascade', copy=True)


class StockPickingCustom(models.Model):
	_inherit = 'stock.picking'

	qc_inspections = fields.One2many(
		comodel_name='qc.inspection.child', inverse_name='picking_cst', copy=False,
		string='Inspections', help="Inspections related to this picking.")


class QcLineCustom(models.Model):
	_name =  'qc.inspection.child'

	parent_id = fields.Many2one('qc.inspection', store=True, ondelete='cascade')
	picking_cst = fields.Many2one('stock.picking', string='Picking', store=True, ondelete='cascade')
	state = fields.Selection(related='parent_id.state')