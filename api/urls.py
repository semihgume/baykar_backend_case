from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (register_user, user_login, user_logout, IHAViewSet, RentedIHAViewSet,
                    CustomUserList, admin_login, CurrentUserView)


router = DefaultRouter()
router.register(r'iha', IHAViewSet, basename='iha')
router.register(r'rented-iha', RentedIHAViewSet, basename='rented-iha')

urlpatterns = [
    path('register/', register_user, name="api-register"),
    path('login/', user_login, name="api-login"),
    path('admin-login/', admin_login, name="api-admin-login"),
    path('logout/', user_logout, name="api-logout"),
    path('get-users/', CustomUserList.as_view(), name="api-get-users"),
    path('current-user/', CurrentUserView.as_view(), name="api-current-user"),
    path('', include(router.urls)),
]