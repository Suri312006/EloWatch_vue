from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .tasks import Pyot_Interface



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def search(request) -> JsonResponse:
    """

    :param request: axios post request containing user query
    :return: Json Response whether requested user exists
    """
    query = request.data['query']
    try:
        Pyot_Interface(query)
        message = 'success'
    except:
        message = 'Summoner does not exist.'

    return JsonResponse({'message': message})








