from django.db import models
import uuid

# Create your models here.
class MySummoner(models.Model):
    id = models.UUIDField( default=uuid.uuid4, editable=False)
    name = models.CharField(primary_key = True, max_length=30)
    level = models.IntegerField(default=0)
    rank = models.CharField(max_length=20)
    ladder_rank_percentage = models.FloatField(default=0)

    icon_path = models.CharField(max_length=200, null=True)
    #need to do more

    created_at = models.DateTimeField(auto_now_add=True)


