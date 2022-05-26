#-*- coding: utf-8 -*-
#Default Libraries
import time
import math
import re
import logging
import warnings
import os, os.path

from odoo.osv import expression
from odoo.tools.float_utils import float_round as round, float_compare
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, remove_accents
from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _, tools
from odoo.tests.common import Form
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

class credit_limit(models.Model):
    _name='credit_limit'
    _description='Verificar y Aplicar Limites de Creédito a los clientes'
    
    #Campos para Credit Limit
    total_invoiced = fields.Char(string='Total Invoiced')
    
credit_limit()