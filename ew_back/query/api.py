from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .tasks import Pyot_Interface
import asyncio
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def search(request):
    query = request.data['query']

    print(query)


    inter = Pyot_Interface(query)

    rank = asyncio.run(inter.get_level())

    print(rank)

    return JsonResponse({'rank': rank})








