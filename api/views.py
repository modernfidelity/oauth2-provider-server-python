from django.http import HttpResponse, JsonResponse
from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from oauth2_provider.models import AccessToken
from oauth2_provider.oauth2_validators import OAuth2Validator
from django.views.decorators.csrf import csrf_exempt
import logging


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_api_version(request):
    """
    Server Version
    :param request:
    :return:
    """
    return Response({API_VERSION})


# class ApiEndpoint(ProtectedResourceView):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('Hello, OAuth2!')


@api_view(['POST'])
@permission_classes((AllowAny,))
@csrf_exempt
def verify_token(request):
    """

    Verify client token is valid

    :param request:
    :return:
    """
    key = request.POST.get('token', '')

    try:
        token = AccessToken.objects.get(token=key)

        if AccessToken.is_valid(token):
            logging.info('Valid access')
            return JsonResponse(
                {'isValid': 'true'}
            )

    except AccessToken.DoesNotExist, e:
        return JsonResponse(
            {'isValid': 'false'}
        )
