import re

from django import template

from apps.buddy_system.models import BuddyRequest
from apps.plugins.middleware.plugin import HttpRequest

register = template.Library()

# I know, it's not the best regex for emails
# [\w.] as [a-zA-Z0-9_.]
CENSORE_REGEX = re.compile(
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
def censore_description(description: str) -> str:
    return CENSORE_REGEX.sub("---censored---", description)


@register.simple_tag(takes_context=True)
def get_current_buddy_request_of_user(context):
    request: HttpRequest = context["request"]

    # TODO: could be more then one?
    return request.membership.user.buddy_system_issued_requests.filter(
        responsible_section=request.membership.section,
    ).first()


@register.simple_tag(takes_context=True)
def get_buddy_requests_waiting_count(context):
    request: HttpRequest = context["request"]

    return request.membership.section.buddy_system_requests.filter(
        state=BuddyRequest.State.CREATED,
    ).count()
