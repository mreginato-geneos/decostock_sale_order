from odoo import api, fields, models


class ProductPricelistItem(models.Model):
    _inherit='product.pricelist.item'

    sku = fields.Char(string='SKU', related='product_id.default_code')