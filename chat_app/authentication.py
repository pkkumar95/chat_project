from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomAuthentication(JWTAuthentication, TokenAuthentication, SessionAuthentication):
    """
    Custom authentication backend that uses JWT, token, and session authentication.
    """
    pass
