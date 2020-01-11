#
# @license
# Copyright (c) 2020 XGDFalcon®. All Rights Reserved.
#
#
# XGDFalcon LLC retains all intellectual property rights to the code
# distributed as part of the Control Point System Software (CPSS) package.
#

"""
This python module provides...

Written by Larry Latouf (xgdfalcon@gmail.com)
"""

from django.db.models import signals
from django.dispatch import dispatcher

def generate_longterm(sender, instance, signal, *args, **kwargs):
  from .models.client import FacebookClientOption
  for client in FacebookClientOption.objects.all():
    client.generate_longterm()
