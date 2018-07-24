# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Repair_update(models.Model):
    _inherit='mrp.repair'

#SE AGREGO EL METODO PARA PODER LLAMARLO DESDE EL REPORTE QWEB Y ESTE DEVUELVA EL TOTAL
#DE LOS PRECIOS Y CANTIDADES
    def total_cantidades_precios(self):
        print('esto es el total cantidad XD', self.id, self.amount_total)

        filtro=[('repair_id','=',self.id)]
        campos=['product_uom_qty','price_unit']
        consulta= self.env['mrp.repair.line'].search_read(filtro,campos)
        print(consulta)

        total_cantidad=0
        total_precio=0
        for con in consulta:
            total_cantidad=total_cantidad+con['product_uom_qty']
            total_precio=total_precio+con['price_unit']
        return total_cantidad, total_precio

Repair_update()