from django.db import models

# Create your models here.
class AnonymousUserData(models.Model):
    uuid = models.UUIDField(unique=True)
    
    #TODO change data with data that we actually want to store
    data = models.JSONField(default=dict)
    
    