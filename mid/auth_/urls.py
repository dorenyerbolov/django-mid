from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token

from auth_.views import UserRegistrationViewSet

router = SimpleRouter()
router.register('register', UserRegistrationViewSet, basename='register')

urlpatterns = [
    path('login/', obtain_jwt_token)
]

urlpatterns += router.urls
