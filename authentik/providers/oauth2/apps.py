"""authentik oauth provider app config"""
from importlib import import_module

from django.apps import AppConfig


class AuthentikProviderOAuth2Config(AppConfig):
    """authentik oauth provider app config"""

    name = "authentik.providers.oauth2"
    label = "authentik_providers_oauth2"
    verbose_name = "authentik Providers.OAuth2"
    mountpoints = {
        "authentik.providers.oauth2.urls_github": "",
        "authentik.providers.oauth2.urls": "application/o/",
    }

    def ready(self) -> None:
        import_module("authentik.providers.oauth2.managed")
