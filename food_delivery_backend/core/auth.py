from firebase_admin import auth
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            return None  # No token provided

        token = auth_header.split(" ").pop()  # Extract token
        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token["uid"]
            email = decoded_token.get("email", "")
            user, _ = User.objects.get_or_create(username=uid, email=email)
            return (user, None)  # Authenticated user object
        except Exception:
            raise AuthenticationFailed("Invalid Firebase token")
