from django.db import models
import uuid

# Create your models here.


class MySummoner(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(primary_key=True, max_length=30)
    level = models.IntegerField(default=0)

    ladder_rank_percentage = models.FloatField(default=0)

    icon_path = models.CharField(max_length=200, null=True)
    # need to do more

    created_at = models.DateTimeField(auto_now_add=True)


class MyRank(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    icon_path = models.CharField(max_length=200, null=True)

    tier = models.CharField(max_length=20, null=True)
    division = models.CharField(max_length=20, null=True)
    lp = models.CharField(max_length=20, null=True)

    rank_of = models.OneToOneField(MySummoner, related_name='rank', on_delete=models.CASCADE)


    wins=models.IntegerField(default=0)
    losses=models.IntegerField(default=0)



