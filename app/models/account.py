from django.db import models
from django.contrib.auth.models import User

class Account ():

    id          = None
    balance     = None
    owing       = None
    owing_since = None
    user        = User()

    def getId ():
        if (self.id==None):
        	raise NameError
        return self.id

    def getBalance ():
        if (self.self.balance==None):
        	raise NameError
        return self.balance

    def getOwing ():
        if (self.owing==None):
        	raise NameError
        return self.owing

    def getOwingSince ():
        if (self.owing_since==None):
        	raise NameError
        return self.owing_since

    def getUser ():
        if (self.user==None):
        	raise NameError
        return self.user

    def setId (id):
        if (id<=0 or type(balance) is not 'int'):
        	raise ValueError
        self.id = id

    def setBalance (balance):
        if (type(balance) is not 'int' or type(balance) is not 'float'):    	
        	raise ValueError
        self.balance = balance 

    def setOwing (owing):
        if (type(owing) is not 'bool'):
        	raise ValueError
        self.owing = owing   

    def setOwingSince (owing_since):
        #if (type(owing_since) is not 'string'):
        #	raise ValueError
        self.owing_since = owing_since 

    def setUser (user):
        self.user = user 	

    def search ():
        raise NotImplementedError

    def update ():
        raise NotImplementedError  

    def save ():
        raise NotImplementedError      

    class Meta:
        managed   = False
        app_label = 'app'