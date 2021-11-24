# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modulo_personalizado(models.Model):
    _name = 'modulo_personalizado.modulo_personalizado'
    _description = 'modulo_personalizado.modulo_personalizado'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
#
    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
