"""
api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User, Group

admin.autodiscover()

from rest_framework import permissions, routers, serializers, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from settings import API_VERSION, DEBUG
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from api import views


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_api_version(request):
    return Response({API_VERSION})


# Define the serializers
class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer (DRF)
    """
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    """
    Group Serializer (DRF)
    """
    class Meta:
        model = Group


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    User View
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    Group View
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Main URLs
urlpatterns = [

    # System
    url(r'^version', get_api_version, name='get_api_version'),

    # Admin
    url(r'^admin/', admin.site.urls),

    # REST Framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # OAUTH2 Toolkit (Authentication Server)
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),  # OAUTH2 Provider

    # Verify Bearer token from clients
    url(r'^verify-token', views.verify_token, name='verify_token'),

    # API
    url(r'^', include(router.urls)),

    # Accounts App
    # url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),

]

# On DEV server serve the local media files
if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
