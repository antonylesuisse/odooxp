# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tyrell_corp(models.Model):
    _name = 'tyrell_corp.tyrell_corp'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    super_field = fields.Boolean(string="DBO Was Here", default=True)

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100
