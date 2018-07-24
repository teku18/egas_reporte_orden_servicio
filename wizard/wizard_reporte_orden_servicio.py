# -*- coding: utf-8 -*-

from odoo import fields, models, api

class wizard_reporte_orden_servicio(models.TransientModel):
    _name='wizard.orden.servicio'
    _description='wizard orden de servicio'

    fecha_inicio= fields.Date('Fecha inicio')
    fecha_fin= fields.Date('Fecha fin')


    # def check_report(self, cr, uid, ids, context=None):
    #     obj=self.read(cr, uid, ids,['fecha_inicio','fecha_fin'])
    #     datas={"model":"ir.ui.menu"}
    #     if obj:
    #         datas["form"]=obj[0]
    #         datas["form"]["uid"]=uid
    #     return {'type':'ir.actions.report.xml',
    #             'report_name':'orden.servicio',
    #             'datas':datas,
    #             }

    def check_report(self):
        print('funciona ????')
        return True

wizard_reporte_orden_servicio()