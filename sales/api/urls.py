from django.urls import include, path

urlpatterns = [
    path("v1/", include("sales.api.v1.urls")),
]
