
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import AnonymousUserData

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def your_anonymous_view(request):
    if request.method == 'POST':
        # Store or update data linked to the UUID
        uuid = request.anonymous_uuid
        access_token = request.anonymous_access_token
        data, created = AnonymousUserData.objects.get_or_create(uuid=uuid)
        data.data = request.data  # Assuming data is sent in the request
        data.save()

        return Response({'message': 'Data stored successfully!'})

    elif request.method == 'GET':
        # Retrieve data linked to the UUID
        uuid = request.anonymous_uuid
        try:
            data = AnonymousUserData.objects.get(uuid=uuid)
            return Response(data.data)
        except AnonymousUserData.DoesNotExist:
            return Response({'message': 'No data found for this UUID.'})
