from rest_framework import routers

from . import views
from django.urls import path, include

from .views import UserView

router = routers.DefaultRouter()
router.register(r'users', UserView)

urlpatterns = [
    path('register/', views.RegisterUserApiView.as_view()),
    path('api/', include(router.urls))
]
