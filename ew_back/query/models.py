from django.db import models


# Create your models here.
class MySummoner(models.Model):
    name = models.CharField(max_length=30)
    level = models.IntegerField(default=0)
    ladder_rank = models.IntegerField(default=0)
    ladder_rank_percentage = models.IntegerField(0)

    # TODO implement profile pic here too
