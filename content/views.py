
# Swagger Modules
from django.http import HttpResponse
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



@swagger_auto_schema(method="GET",responses=responses.GET_RESPONSES,)
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def units(request):
    data = [
        {"title" : "Unit 1", "content" : "This is the content of unit 1" , "count" : 7},
        {"title" : "Unit 2", "content" : "This is the content of unit 2", "count" : 3},
        {"title" : "Unit 3", "content" : "This is the content of unit 3", "count" : 4},
    ]
    return response.Response(data, status.HTTP_200_OK)





@swagger_auto_schema(
    method="POST",
    responses=responses.GET_RESPONSES,
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={
            'message': openapi.Schema(type=openapi.TYPE_STRING),
        }
    )
)
@api_view(['POST'])
# @decorators.try_except
@permission_classes([])
@authentication_classes ([])
def ChatGPT(request):
    import openai
    message = request.data['message']

    
    openai.api_key = "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"
    prompt = f"{message}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = response.choices[0].text.strip()
    return HttpResponse(response_text)