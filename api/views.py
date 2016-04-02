from django.http import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_api_version(request):
    """
    Server Version
    :param request:
    :return:
    """
    return Response({API_VERSION})


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')


@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)


@api_view(['POST'])
@permission_classes((AllowAny,))
def verify_token(request, *args, **kwargs):
    """
    Verify Token is still valid
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    return Response(
        # @todo : check client id exists
        # @todo : then check token is valid
        'token = ' + request.POST.get("token")
    )





#
#
# @csrf_exempt
# def verify_token(request):
#
#     if is_authenticated(request) == False:
#         return HttpResponse(
#             json.dumps({
#                 'error': 'invalid_request'
#             }),
#             status = 403
#         )
#
#     return HttpResponse(
#         json.dumps({
#             'user': request.user.username
#         })
#     )
