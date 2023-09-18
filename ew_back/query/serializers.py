from rest_framework.serializers import ModelSerializer

from .models import *

class MyRankSerializer(ModelSerializer):

    class Meta:
        model=MyRank
        fields=('icon_path', 'tier', 'division', 'lp', 'wins', 'losses')
class MySummonerSerialzier(ModelSerializer):
    rank = MyRankSerializer(read_only=True)
    class Meta:
        model = MySummoner
        fields = ('id', 'name', 'level', 'rank', 'ladder_rank_percentage', 'icon_path')


