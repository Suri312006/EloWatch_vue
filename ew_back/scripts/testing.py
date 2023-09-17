import django
import os
import sys
from datetime import timedelta
from django.utils import timezone
from collections import Counter

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ew_back.settings')
django.setup()

from query.models import MySummoner, MyRank


sums = MySummoner.objects.all()

for sum in sums:
    print(sum.rank)
    sum.delete()

ranks = MyRank.objects.all()


for rank in ranks:
    print(rank)