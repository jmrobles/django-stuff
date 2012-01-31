# -*- coding: utf-8 -*-
# Author: JM Robles <jmroblesh@digitalilusion.com>

from django import template

from django.utils.translation import ugettext as _
register = template.Library()

def mapval(val,arg):
	maps = arg.split(",")
	for m in maps:
		if val == m.split(":")[0]:
			return _(m.split(":")[1])
	return _("not_found")


register.filter('mapval',mapval)

