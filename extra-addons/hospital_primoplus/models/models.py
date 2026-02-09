# hospital_modelos.py
from odoo import models, fields

class hospital_paciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'paciente_hospital'
    name = fields.Char(string="Nombre_Apellidos", required=True)
    sintomas = fields.Text(string="Sintomas_Paciente")

class hospital_medico(models.Model):
    _name = 'hospital.medico'
    _description = 'medico_hospital'
    name = fields.Char(string="Nombre_Medico", required=True)
    num_colegiado = fields.Char(string="Numero_Colegiado", required=True)

class hospital_diagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'diagnostico_hospital'
    name = fields.Char(string="Diagnostico_Titulo", required=True)
    paciente_id = fields.Many2one('hospital.paciente', string="Paciente_Atendido")
    medico_id = fields.Many2one('hospital.medico', string="Medico_Tratante")
    diagnostico_texto = fields.Text(string="Descripcion_Diagnostico")