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
    :return: Json Response whether requested user exists
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











