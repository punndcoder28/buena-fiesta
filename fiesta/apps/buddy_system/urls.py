from __future__ import annotations

from django.urls import path

from ..accounts.models.profile import user_profile_picture_storage
from .views import BuddySystemIndexView
from .views.editor import BuddyRequestEditorDetailView, BuddyRequestsEditorView, QuickBuddyMatchView
from .views.matches import MyBuddies
from .views.matching import MatchingRequestsView, ProfilePictureServeView, TakeBuddyRequestView
from .views.request import BuddySystemEntrance, NewRequestView, SignUpBeforeEntranceView, WannaBuddyView

urlpatterns = [
    path("", BuddySystemIndexView.as_view(), name="index"),
    path("wanna-buddy", WannaBuddyView.as_view(), name="wanna-buddy"),
    path("entrance", BuddySystemEntrance.as_view(), name="entrance"),
    path(
        "sign-up-before-request",
        SignUpBeforeEntranceView.as_view(),
        name="sign-up-before-request",
    ),
    path("new-request", NewRequestView.as_view(), name="new-request"),
    path("requests", BuddyRequestsEditorView.as_view(), name="requests"),
    path("my-buddies", MyBuddies.as_view(), name="my-buddies"),
    path("matching-requests", MatchingRequestsView.as_view(), name="matching-requests"),
    path(
        "take-request/<uuid:pk>",
        TakeBuddyRequestView.as_view(),
        name="take-buddy-request",
    ),
    path("detail/<uuid:pk>", BuddyRequestEditorDetailView.as_view(), name="editor-detail"),
    path("quick-match/<uuid:pk>", QuickBuddyMatchView.as_view(), name="quick-match"),
    # serve profile picture with proxy view
    ProfilePictureServeView.as_url(user_profile_picture_storage, url_name="serve-issuer-profile-picture"),
]
