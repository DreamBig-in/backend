from users.models import User

# Swagger Modules
from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from utils import responses
import json


from rest_framework import views, response, status, permissions, authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import logging
from users import models as UserModels



@swagger_auto_schema(
    method="POST",
    responses=responses.GET_RESPONSES,
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={
            'google_id': openapi.Schema(type=openapi.TYPE_STRING),
        }
    )
)
@api_view(['POST'])
# @decorators.try_except
@permission_classes([])
@authentication_classes ([])
def user_check(request):
    google_id = request.data.get("google_id", None)
    data = {}
    data["status"] = False
    try:
        user = User.objects.get(google_id = google_id)
        print(user)
        if user:
            token = Token.objects.get(user=user)
            # TODO: Also Add a onboarded flag
            data["token"] = str(token)
            # TODO: Fill in dynamic data
            data["onboarded"] = True
            data["points"] = 0
            data["level"] = 0
            

            data["status"] = True
        return response.Response(data, status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return response.Response(data, status.HTTP_200_OK)
