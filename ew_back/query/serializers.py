from rest_framework.serializers import ModelSerializer

from .models import MySummoner

class MySummonerSerialzier(ModelSerializer):
    class Meta:
        model = MySummoner
        fields = ('name', 'level', 'rank', 'ladder_rank_percentage', 'icon_path')