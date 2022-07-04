from django.contrib import admin
from django.urls import path, include
from apps.users.views import Login, Logout, UserToken
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.api.routers')),
    path('login/', Login.as_view(), name = 'login'),
    path('refresh-token/', UserToken.as_view(), name = 'refresh-token'),
    path('logout/', Logout.as_view(), name = 'logout')
]
