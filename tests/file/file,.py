# -*- coding: utf-8 -*-
# 1 : imports of python lib
# 2 : imports of odoo
import odoo
from odoo import api, fields, models, _
# 3 : imports from odoo addons


class MyClass(models.Model):
    _inherit = "my.class"
    _name = "my.class"
    _description = "My Class"
    _auto = True
