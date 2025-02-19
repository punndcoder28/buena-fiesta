from __future__ import annotations

import typing

from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from apps.plugins.plugin import PluginAppConfig
from apps.utils.templatetags.navigation import NavigationItemSpec

if typing.TYPE_CHECKING:
    from apps.plugins.middleware.plugin import HttpRequest


class SectionsConfig(PluginAppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.sections"

    configuration_model = "sections.SectionsConfiguration"

    verbose_name = _("ESN section")

    login_not_required_urls = [
        "choose-space",
    ]

    def as_navigation_item(self, request: HttpRequest) -> NavigationItemSpec | None:
        if request.membership.is_privileged:
            return (
                super()
                .as_navigation_item(request)
                ._replace(
                    url="",
                    children=[
                        NavigationItemSpec(
                            _("Members"),
                            reverse("sections:section-members"),
                        ),
                        NavigationItemSpec(
                            _("Statistics"),
                            reverse("sections:section-stats"),
                        ),
                    ],
                )
            )
        return None


__all__ = ["SectionsConfig"]
