# -*- coding: utf-8 -*-

from openerp import models, fields, api

 class memberCard(models.Model):
    _name = 'cashcard.memberCard'
    card_number = fields.Char()
    open_time = fields.Date(default=fields.Date.today)
    left_value = fields.Float()
    card_password = fields.Char()



 class cardReduceRecord(models.Model):
    _name = 'cashcard.cardReduceRecord'
    reduce_time = fields.Date(default=fields.Date.today)
    card_number = fields.Char()
    left_value = fields.Float()
    reduce_value = fields.Float()
