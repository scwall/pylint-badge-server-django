"""pylint_badge_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.urls import router_users
from pylint.urls import router, urlpatterns
from users.urls import urlpatternsuser
from rest_framework_simplejwt import views as jwt_views

# router = routers.DefaultRouter()
# router.register(r"number-users",MainPageCount)
urlpatterns = [
    path('user/', include((urlpatternsuser, "users"), namespace='users')),
    path('pylint/', include((urlpatterns, "pylint"), namespace='pylint')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
