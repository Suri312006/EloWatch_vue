from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import MySummonerSerialzier
from .tasks import *
from .models import *
import asyncio


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def search(request) -> JsonResponse:
    """

    :param request: axios post request containing user query
    :return: Json Response whether requested user exists. If user exists, returns name as well

    """
    name = request.data['query']

    if asyncio.run(check_summoner(name)):
        name = asyncio.run(get_name(name))
        print(name)
        return JsonResponse({
            'message': 'exists',
            'name': name

        })
    else:

        return JsonResponse({'message': 'does not exist'})


def profile(request, name) -> JsonResponse:
    """

    :param request: axios post request
    :param name: name of summoner, passed in through urls.py
    :return: JsonResponse with 'data': serializer.data
    """

    # gets summoner object
    summoner = asyncio.run(get_summoner(name))
    print(asyncio.run(get_icon_path(summoner)))

    # Deletes any existing data in the database for the searched summoner
    existing_instances = MySummoner.objects.filter(name=str(summoner.name))
    if len(existing_instances) > 0:
        for instance in existing_instances:
            instance.delete()


    rank_data = asyncio.run(get_rank(summoner))
    print(rank_data)

    # creates new model in database
    model_summoner = MySummoner.objects.create(
        name=summoner.name,
        level=summoner.level,

        ladder_rank_percentage=asyncio.run(get_ladder_rank(summoner)),
        icon_path=asyncio.run(get_icon_path(summoner))
    )
    model_rank = MyRank.objects.create(
        icon_path=asyncio.run(get_rank_icon_path(rank_data['tier'])),
        tier=rank_data['tier'],
        division=rank_data['division'],
        lp=rank_data['lp'],
        rank_of = model_summoner,
        wins=rank_data["wins"],
        losses=rank_data["losses"]
    )

    model_summoner.rank = model_rank



    # serializer to make data sending easier
    serializer = MySummonerSerialzier(model_summoner)

    return JsonResponse({'summoner': serializer.data}, safe=False)


def test(request) -> JsonResponse:
    summoner = asyncio.run(get_summoner("SirYum"))
    print(asyncio.run(get_ladder_rank(summoner)))

    return JsonResponse({'message': 'tested'})
