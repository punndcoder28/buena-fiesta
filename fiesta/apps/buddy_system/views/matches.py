from __future__ import annotations

from django.views.generic import ListView

from apps.plugins.middleware.plugin import HttpRequest
from apps.sections.views.mixins.membership import EnsureLocalUserViewMixin


class MyBuddies(EnsureLocalUserViewMixin, ListView):
    request: HttpRequest

    template_name = "buddy_system/my_buddies.html"

    def get_queryset(self):
        return self.request.user.buddy_system_matched_requests.prefetch_related("issuer__profile")
