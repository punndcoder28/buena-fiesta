from __future__ import annotations

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "accounts/user_profile/index.html"
