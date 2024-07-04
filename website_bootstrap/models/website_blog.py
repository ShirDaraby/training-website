# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
import random

from odoo import api, models, fields, _
from odoo.addons.http_routing.models.ir_http import slug, unslug
from odoo.addons.website.tools import text_from_html
from odoo.tools.json import scriptsafe as json_scriptsafe
from odoo.tools.translate import html_translate


class BlogPost(models.Model):
    _inherit = "blog.post"

    icon_image = fields.Binary(string="Image", readonly=False)
