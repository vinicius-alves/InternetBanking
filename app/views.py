import json
import sys
from django.shortcuts import render
from django.conf import settings
from django.core.serializers import serialize
from django.utils.safestring import mark_safe
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from app.models import *
from django.contrib.auth.models import User
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

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((AllowAll,))
def balance(request):
    data ={}
    if settings.DEBUG:
        print ("Input: {\"function\":\"",str(sys._getframe().f_code.co_name),"} ",end="")
        print ("{\"user:\"\"",str(request.user),"\"}")
    try:
        account = Account.objects.get(user=request.user)
        data = {"status":"sucesso", "balance":account.getBalance()}
        return Response(data,status=status.HTTP_200_OK)
    except:
        data = {"non_field_errors":["Unexpected error:" + str(sys.exc_info()[0])]}
        return Response(data,status=status.HTTP_400_BAD_REQUEST,exception=True)
    finally:
        if settings.DEBUG: print ("Output: ",data)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((AllowAll,))
def excerpt(request):
    data ={}
    if settings.DEBUG:
        print ("Input: {\"function\":\"",str(sys._getframe().f_code.co_name),"} ",end="")
        print ("{\"user:\"\"",str(request.user),"\"}")
    try:
        account = Account.objects.get(user=request.user)
        account_history = AccountHistory(account)
        transactions = account_history.getExcerpt()
        data = {"status":"sucesso"}
        data["transactions"] = [transaction.as_json() for transaction in transactions]
        return Response(data,status=status.HTTP_200_OK)
    except:
        data = {"non_field_errors":["Unexpected error:" + str(sys.exc_info()[0])]}
        return Response(data,status=status.HTTP_400_BAD_REQUEST,exception=True)
    finally:
        if settings.DEBUG: print ("Output: ",data)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((AllowAll,))
def withdraw(request):
    data ={}
    groups_manager = SettingsUserGroups()
    transaction = Transaction()
    transaction_manager = TransactionManager()
    if settings.DEBUG:
        print ("Input: {\"function\":\"",str(sys._getframe().f_code.co_name),"} ",end="")
        print ("{\"user:\"\"",str(request.user),"\"}")
    try:
        json_in=json.loads(request.body.decode("utf-8"))
        account = Account.objects.get(user=request.user)
        type_transaction = Transaction_Type.objects.get(id=1)  
        transaction.setType(type_transaction)
        transaction.setValue(abs(int(json_in["value"])))
        transaction.setAccount(account)

        if(groups_manager.isPublic(request.user)):
            transaction_manager = TransactionPublic()

        elif(groups_manager.isVip(request.user)):
            transaction_manager = TransactionVip()  
            
        transaction_manager.setTransaction(transaction)
        transaction_manager.withdraw()   
        transaction_manager.save() 

        data = {"status":"sucesso"}
        return Response(data,status=status.HTTP_200_OK) 
          
    except:
        data = {"non_field_errors":["Unexpected error:" + str(sys.exc_info()[0])]}
        return Response(data,status=status.HTTP_400_BAD_REQUEST,exception=True)
    finally:
        if settings.DEBUG: print ("Output: ",data)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((AllowAll,))
def deposit(request):
    data ={}
    groups_manager = SettingsUserGroups()
    transaction = Transaction()
    transaction_manager = TransactionManager()
    if settings.DEBUG:
        print ("Input: {\"function\":\"",str(sys._getframe().f_code.co_name),"} ",end="")
        print ("{\"user:\"\"",str(request.user),"\"}")
    try:
        json_in=json.loads(request.body.decode("utf-8"))
        account = Account.objects.get(user=request.user)
        type_transaction = Transaction_Type.objects.get(id=2)  
        transaction.setType(type_transaction)
        transaction.setValue(abs(int(json_in["value"])))
        transaction.setAccount(account)

        if(groups_manager.isPublic(request.user)):
            transaction_manager = TransactionPublic()

        elif(groups_manager.isVip(request.user)):
            transaction_manager = TransactionVip()  
            
        transaction_manager.setTransaction(transaction)
        transaction_manager.deposit()   
        transaction_manager.save() 

        data = {"status":"sucesso"}
        return Response(data,status=status.HTTP_200_OK) 
          
    except:
        data = {"non_field_errors":["Unexpected error:" + str(sys.exc_info()[0])]}
        return Response(data,status=status.HTTP_400_BAD_REQUEST,exception=True)
    finally:
        if settings.DEBUG: print ("Output: ",data)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((AllowAll,))
def transfer(request):
    data ={}
    groups_manager = SettingsUserGroups()
    first_transaction = Transaction()
    second_transaction = Transaction()
    transaction_manager = TransactionManager()
    if settings.DEBUG:
        print ("Input: {\"function\":\"",str(sys._getframe().f_code.co_name),"} ",end="")
        print ("{\"user:\"\"",str(request.user),"\"}")
    try:
        json_in=json.loads(request.body.decode("utf-8"))
        receiver = User.objects.get(id=json_in["receiver"])
        if(request.user==receiver):
            raise NameError
        account = Account.objects.get(user=request.user)
        receiver_account = Account.objects.get(user=receiver)

        #first transaction
        type_transaction = Transaction_Type.objects.get(id=5)  
        first_transaction.setType(type_transaction)
        first_transaction.setValue(abs(int(json_in["value"])))
        first_transaction.setAccount(account)

        if(groups_manager.isPublic(request.user)):
            transaction_manager = TransactionPublic()

        elif(groups_manager.isVip(request.user)):
            transaction_manager = TransactionVip()  
            
        transaction_manager.setTransaction(first_transaction)
        transaction_manager.doTransfer()   
        transaction_manager.save()

        #second transaction
        type_transaction = Transaction_Type.objects.get(id=8)  
        second_transaction.setType(type_transaction)
        second_transaction.setValue(abs(int(json_in["value"])))
        second_transaction.setAccount(receiver_account)

        if(groups_manager.isPublic(receiver)):
            transaction_manager = TransactionPublic()

        elif(groups_manager.isVip(receiver)):
            transaction_manager = TransactionVip()
   
        transaction_manager.setTransaction(second_transaction)
        transaction_manager.receiveTransfer()   
        transaction_manager.save()

        data = {"status":"sucesso"}
        return Response(data,status=status.HTTP_200_OK) 
          
    except:
        data = {"non_field_errors":["Unexpected error:" + str(sys.exc_info()[0])]}
        return Response(data,status=status.HTTP_400_BAD_REQUEST,exception=True)
    finally:
        if settings.DEBUG: print ("Output: ",data)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((VipOnly,))
def help(request):
    data ={}
    transaction =Transaction()
    transaction_manager = TransactionManager()    
    request_manager = RequestManager()
    if settings.DEBUG:
        print ("Input: {\"function\":\"",str(sys._getframe().f_code.co_name),"} ",end="")
        print ("{\"user:\"\"",str(request.user),"\"}")
    try:

        help_request = Help_Request()
        help_request.setUser(request.user)
        request_manager.setHelpRequest(help_request)

        account = Account.objects.get(user=request.user)
        type_transaction = Transaction_Type.objects.get(id=7)  
        transaction.setType(type_transaction)
        transaction.setValue(50)
        transaction.setAccount(account)

        transaction_manager = TransactionVip()  
        transaction_manager.setTransaction(transaction)        
        request_manager.setTransactionManager(transaction_manager) 

        request_manager.save()

        data = {"status":"sucesso"}
        return Response(data,status=status.HTTP_200_OK) 
          
    except:
        data = {"non_field_errors":["Unexpected error:" + str(sys.exc_info()[0])]}
        return Response(data,status=status.HTTP_400_BAD_REQUEST,exception=True)
    finally:
        if settings.DEBUG: print ("Output: ",data)
