# -*- coding: utf-8 -*-
# Author: JM Robles <jmroblesh@digitalilusion.com>
from django import template

from django.utils.translation import ugettext as _
register = template.Library()

def empty(val):
	if val == None or val.strip() == "":
		return _("empty_val")
	return val

register.filter('empty',empty)

