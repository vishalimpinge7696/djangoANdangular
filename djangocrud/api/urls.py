from django.urls import include
from rest_framework import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]