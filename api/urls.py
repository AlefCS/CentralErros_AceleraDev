from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api import views

router = routers.DefaultRouter()
router.register(r"errors", views.ErrorAPIViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("docs/", views.show_docs, name="docs"),
    path('get_token/', obtain_auth_token),
]
