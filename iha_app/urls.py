from django.urls import path
from .views import (login_page, register_page, dashboard_page, uavs_page,
                    rented_uavs_page, home_page, admin_login_page, profile_page)

urlpatterns = [
    path('', home_page, name="homepage"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('dashboard/', dashboard_page, name="dashboard"),
    path('dashboard/uavs/', uavs_page, name="dashboard-uavs"),
    path('dashboard/rented-uavs/', rented_uavs_page, name="dashboard-rented-uavs"),
    path('admin/', admin_login_page, name="admin-login"),
    path('profile/', profile_page, name="profile"),
]