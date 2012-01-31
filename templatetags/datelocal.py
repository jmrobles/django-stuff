# -*- coding: utf-8 -*-
# Author: JM Robles <jmroblesh@digitalilusion.com>

from django import template
from django.template.defaultfilters import date
register = template.Library()
from main.util import pytz
def datelocal(dt,arg=None):
#	TODO: using TZ request meta if present
	return date(dt.replace(tzinfo=pytz.UTC).astimezone(pytz.timezone("Europe/Madrid")),arg)
register.filter('datelocal', datelocal)

