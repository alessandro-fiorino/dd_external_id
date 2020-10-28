# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import logging
_logger = logging.getLogger(__name__)

class ExternalIDMixin(models.AbstractModel):
    _name = 'dd.externalid.mixin'
    _description = 'Add external ID as field'
    _externalid_module = '__import__'
    
    
    def _externalid_gen(self):
        self.ensure_one()
        return "%s_%d" % (self._name.replace('.','_'),self.id)
    
    def _calc_external_id(self):
        exids = self.env['ir.model.data'].search([('model','=',self._name),
                            ('res_id','in',self.ids)]).mapped(lambda k: {'id': k.res_id ,'s': k.module+'.'+k.name if k.id else ''})
        dids={d['id']:d['s'] for d in exids}
        if self.env.context.get('externalid_force_create',False):  
            _logger.info("externalid create")
            m=self.env.context.get('externalid_module',self._externalid_module)
            Imd=self.env['ir.model.data']
            for r in self:
                if r.id!=0:
                    v=dids.get(r.id,False)
                    if v:
                        r.external_id = v
                    else:
                        newid = r._externalid_gen()
                        Imd.create({'name':newid, 'model': self._name, 'res_id': r.id, 'module': m, 'noupdate': False, })
                        r.external_id = m+'.'+newid
                else:
                    r.externa_id = False
        else:
            for r in self:
                r.external_id = dids.get(r.id,False)
                
    external_id = fields.Char(string="External ID (comp)", compute_sudo=True, compute='_calc_external_id')

class ExternalIDPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner','dd.externalid.mixin']
    
