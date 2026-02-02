# -*- coding: utf-8 -*-

from odoo import models, fields, api


class nivel_sueno(models.Model):
    _name = 'nivel_sueno.nivel_sueno'
    _description = 'Calcular e café que necesita'

    alumno = fields.Char(string="Nombre del alumno")
    nivel_sueño = fields.Integer(string="Nivel de sueño")
    bebida_recomendado = fields.Char(string="Bebida que se le recomienda")

    if 1 <= nivel_sueño >= 3:
        bebida_recomendado = "Café con leche"
    elif 4 <= nivel_sueño >= 6:
        bebida_recomendado = "Café solo largo"
    elif 7 <= nivel_sueño >= 9:
        bebida_recomendado = "Café solo largísimo"
    else:
        bebida_recomendado = "Inyección adrenalina"



