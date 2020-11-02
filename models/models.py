# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import random, string
import logging
_logger = logging.getLogger(__name__)

letters = string.ascii_lowercase

def _random_string(length):
    return ''.join(random.choice(letters) for i in range(length))

class ExternalIDMixin(models.AbstractModel):
    _name = 'dd.externalid.mixin'
    _description = 'Add external ID as virtual field'
    _externalid_module = '__import__'
    _externalid_addrandom = False
    
    
    def _externalid_gen(self):
        self.ensure_one()
        if self._externalid_addrandom:
            return "%s_%d_%s" % (self._table,self.id,_random_string(8))
        else:
            return "%s_%d" % (self._table,self.id)
    
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
    
    def set_external_id(self,xmlid):
        self.ensure_one()
        Imd=self.env['ir.model.data'].sudo()
        r=Imd.search([('model','=',self._name),('res_id','=',self.id)])
        if len(r)>0:
            _logger.info("unlinking old id %s" % (r.name))
            r.unlink()
        if xmlid.find('.')>=0:
            m,newid=xmlid.split('.',1)
        else:
            m,newid=self._externalid_module,xmlid
        _logger.info("Setting xmlid %s" % (newid))        
        Imd.create({'name':newid, 'model': self._name, 'res_id': self.id, 'module': m, 'noupdate': False, })
        self.external_id = m+'.'+newid
    

class ExternalIDPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner','dd.externalid.mixin']
    
    
