from django.urls import path

from .views import SnackListView, SnackDetailView

urlpatterns = [
    path("", SnackListView.as_view(), name="snack_list"),
    path(
        "<int:pk>/", SnackDetailView.as_view(), name="snack_detail"
    ),  # to look at one snack in detail. Represents the primary key for a given snack.
]
