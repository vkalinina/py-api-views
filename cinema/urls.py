from django.urls import path

from cinema.models import CinemaHall
from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)


urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path(
        "cinema_halls/",
        CinemaHallViewSet.as_view(
            actions={
                "get": "list",
                "post": "create",
            }
        ),
        name="cinema-hall-list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallViewSet.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ),
        name="cinema-hall-detail"),
    path("movies/", MovieViewSet.as_view(
        {
            "get": "list",
            "post": "create",
        }
    ), name="movie-list"),
    path("movies/<int:pk>/", MovieViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }
    ), name="movie-list"),
]

app_name = "cinema"
