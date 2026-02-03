# -*- coding: utf-8 -*-

from odoo import models, fields, api


class nivel_sueno(models.Model):
    _name = 'nivel_sueno.nivel_sueno'
    _description = 'Calcular e café que necesita'

    alumno = fields.Char(string="Nombre del alumno")
    nivel_sueno = fields.Integer(string="Nivel de sueno")
    bebida_recomendado = fields.Char(string="Bebida que se le recomienda", compute="_compute_bebida",store=True)


    @api.depends('nivel_sueno')
    def _compute_bebida(self):
        for record in self:
            if 1 <= record.nivel_sueno <= 3:
                record.bebida_recomendado = "Café con leche"
            elif 4 <= record.nivel_sueno <= 6:
                record.bebida_recomendado = "Café solo largo"
            elif 7 <= record.nivel_sueno <= 9:
                record.bebida_recomendado = "Café solo largísimo"
            elif record.nivel_sueno >= 10:
                record.bebida_recomendado = "Inyección adrenalina"
            else:
                record.bebida_recomendado = "Sin recomendación"





