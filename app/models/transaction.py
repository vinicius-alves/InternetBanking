from django.db import models
from app.models import Account

class Transaction ():

    id      = None
    type    = None
    value   = None  
    time    = None  
    account = Account()

    def getId ():
        if (self.id==None):
            raise NameError
        return self.id

    def getType ():
        if (self.type==None):
            raise NameError
        return self.type

    def getValue ():
        if (self.value==None):
            raise NameError
        return self.value

    def getTime ():
        if (self.time==None):
            raise NameError
        return self.time

    def getAccount ():
        if (self.account==None):
            raise NameError
        return account

    def setId (id):
        if (id<=0 or type(balance) is not 'int'):
            raise ValueError
        self.id = id

    def setType (type):
        if (type<=0 or type(type) is not 'int'):
            raise ValueError
        self.type = type 

    def setValue (value):
        if (type(value) is not 'int' or type(value) is not 'float'):     
            raise ValueError
        self.value = value   

    def setTime (time):
        #if (type(owing_since) is not 'string'):
        #	raise ValueError
        self.time = time 

    def setAccount (account):
        self.account = account 	

    def search ():
        raise NotImplementedError

    def update ():
        raise NotImplementedError  

    def create ():
        raise NotImplementedError      

    class Meta:
        managed   = False
        app_label = 'app'