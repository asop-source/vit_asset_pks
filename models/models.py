# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class asset_pks(models.Model):
		_inherit='account.asset.asset'

		pks_date = fields.Date(string='Tanggal PKS')
		plan_date = fields.Date(string='Rencana Lelang')