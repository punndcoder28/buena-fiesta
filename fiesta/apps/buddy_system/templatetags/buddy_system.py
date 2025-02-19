from __future__ import annotations

import re

from django import template

from apps.buddy_system.apps import BuddySystemConfig
from apps.buddy_system.models import BuddyRequest, BuddySystemConfiguration
from apps.plugins.middleware.plugin import HttpRequest
from apps.plugins.models import Plugin
from apps.plugins.utils import all_plugins_mapped_to_class
from apps.utils.models.query import get_single_object_or_none

register = template.Library()

# I know, it's not the best regex for emails
# [\w.] as [a-zA-Z0-9_.]
CENSOR_REGEX = re.compile(
    # emails
    r"^$|\S+@\S+\.\S+"
    # instagram username
    r"|@[\w.]+"
    # european phone numbers
    r"|\+?\d{1,3}[ \-]?[(]?\d{3,4}[)]?[ \-]?\d{3,4}[ \-]?\d{3,4}",
    # URL adresses SIMPLIFIED
    # r"(https?://)?([a-z\d_\-]{3,}\.)+[a-z]{2,4}(/\S*)?"
    re.VERBOSE | re.IGNORECASE,
)


@register.filter
def censor_description(description: str) -> str:
    return CENSOR_REGEX.sub("---censored---", description)


@register.simple_tag(takes_context=True)
def get_current_buddy_request_of_user(context):
    request: HttpRequest = context["request"]

    return get_single_object_or_none(
        request.membership.user.buddy_system_issued_requests.filter(
            responsible_section=request.membership.section,
        )
    )  # TODO: could be more then one?


@register.simple_tag(takes_context=True)
def get_waiting_requests_to_match(context):
    request: HttpRequest = context["request"]

    buddy_system_plugin: Plugin = request.membership.section.plugins.get(
        app_label=all_plugins_mapped_to_class().get(BuddySystemConfig).label
    )

    configuration: BuddySystemConfiguration = buddy_system_plugin.configuration

    return configuration.matching_policy_instance.limit_requests(
        qs=BuddyRequest.objects.filter(responsible_section=request.membership.section),
        membership=request.membership,
    )


@register.simple_tag(takes_context=True)
def get_waiting_buddy_requests_placed_before(context, br: BuddyRequest):
    request: HttpRequest = context["request"]

    return request.membership.section.buddy_system_requests.filter(
        state=BuddyRequest.State.CREATED,
        created__lt=br.created,
    ).count()


@register.simple_tag(takes_context=True)
def get_matched_buddy_requests(context):
    request: HttpRequest = context["request"]

    # TODO: limit by semester / time
    return request.user.buddy_system_matched_requests.filter(
        responsible_section=request.membership.section,
        state=BuddyRequest.State.MATCHED,
    ).order_by("-matched_at")
