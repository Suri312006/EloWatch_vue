from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .tasks import *
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
    :return: basic summoner info
    """
    summoner = asyncio.run(get_summoner(name))

    print(summoner.name)

    return JsonResponse({'message': 'received'})





