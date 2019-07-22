from django.contrib.auth import get_user_model

from .settings import api_settings

User = get_user_model()
token_backend = api_settings.TOKEN_BACKEND_CLASS(
    api_settings.ALGORITHM,
    api_settings.SIGNING_KEY,
    api_settings.VERIFYING_KEY,
)
