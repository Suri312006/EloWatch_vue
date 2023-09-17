# -*- coding: utf-8 -*-

import django
import os
import sys
from datetime import timedelta
from django.utils import timezone
from collections import Counter

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ew_back.settings')
django.setup()

from query.models import MySummoner


expiry_time = timedelta(days=0, hours=0, minutes=0, seconds=0, microseconds=0, milliseconds=0)
now = timezone.now()

difference = now - expiry_time

expired_summoners = MySummoner.objects.filter(created_at__lte=difference)

for summoner in expired_summoners:
    summoner.delete()
    print('successfully')
