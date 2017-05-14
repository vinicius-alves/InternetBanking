import sys
import json
from django.shortcuts import render
from django.conf import settings
from app.models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from app.permissions import AllowAll,VipOnly

#static pages

def index(request):
    return render(request, 'app/index.html', {})

#web services

@api_view(['POST','DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((AllowAll,))
def logout(request):
    data ={}
    if settings.DEBUG:
        print ("Input: {\"function\":\"",str(sys._getframe().f_code.co_name),"} ",end="")
        print ("{\"user:\"\"",str(request.user),"\"}")
    try:
        t=Token.objects.get(user=request.user)
        t.delete()
        Token.objects.create(user=request.user)
        data = {"status":"sucesso"}
        return Response(data,status=status.HTTP_202_ACCEPTED)
    except:
        data = {"non_field_errors":["Unexpected error:" + str(sys.exc_info()[0])]}
        return Response(data,status=status.HTTP_400_BAD_REQUEST,exception=True)
    finally:
        if settings.DEBUG: print ("Output: ",data)