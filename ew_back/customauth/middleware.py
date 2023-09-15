# customauth/middleware.py
import uuid
from rest_framework_simplejwt.tokens import RefreshToken

class AnonymousUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if 'uuid' not in request.session:
                request.session['uuid'] = str(uuid.uuid4())  # Assign a UUID

                # Generate an access token using simplejwt
                refresh = RefreshToken.for_user(None)
                request.session['access_token'] = str(refresh.access_token)

            # Attach UUID and access token to the request object
            request.anonymous_uuid = request.session['uuid']
            request.anonymous_access_token = request.session['access_token']

        response = self.get_response(request)
        return response
