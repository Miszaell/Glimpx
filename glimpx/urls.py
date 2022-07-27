from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from apps.users.views import Login, Logout, UserToken
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name = 'login'),
    path('refresh-token/', UserToken.as_view(), name = 'refresh-token'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('users/', include('apps.users.api.routers')),
    path('materials/', include('apps.products.api.routers')),
    path('physicalExm/', include('apps.health.api.routers.routerPhysical')),
    path('clinicalExm/', include('apps.health.api.routers.routerClinical')),
    path('familyBkg/', include('apps.health.api.routers.routerFamily')),
    path('anamnesis/', include('apps.health.api.routers.routerAnamnesis')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
