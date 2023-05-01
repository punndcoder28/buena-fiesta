from __future__ import annotations

import magic
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.urls import path
from django.urls.resolvers import RoutePattern
from django.views import View

from apps.files import logger
from apps.files.storage import NamespacedFilesStorage
from apps.plugins.middleware.plugin import HttpRequest


class NamespacedFilesServeView(View):
    mime = magic.Magic(mime=True)

    # got from as_view() call in as_url()
    storage: NamespacedFilesStorage = None

    def get(self, request, name: str, *args, **kwargs) -> HttpResponse:
        if not self.storage.exists(name):
            logger.warning("File %s in namespace %s not found.", name, self.storage.location)
            return HttpResponseNotFound()

        if not self.has_permission(request, name) and not request.user.is_superuser:
            logger.warning("Access to %s denied for %s.", name, request.user)
            return HttpResponseForbidden()

        return HttpResponse(
            headers={
                "Content-Disposition": f'filename="{name}"',
                "X-Accel-Redirect": self.storage.internal_serve_url(name),
                "Content-Type": self.mime.from_file(self.storage.path(name=name)),
            }
        )

    def has_permission(self, request: HttpRequest, name: str) -> bool:
        # for overriding purposes
        return self.storage.has_permission(request, name)

    @classmethod
    def as_url(cls, storage: NamespacedFilesStorage, url_name: str = None) -> RoutePattern:
        return path(
            f"serve/{storage.namespace}/<path:name>",
            cls.as_view(
                storage=storage,
            ),
            name=url_name or f"serve-{storage.location}",
        )
