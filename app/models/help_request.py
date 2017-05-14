from django.db import models
from django.contrib.auth.models import User

class HelpRequest ():

    id     = None
    type   = None
    solved = None  
    start  = None  
    user   = User()

    def getId ():
        if (self.id==None):
            raise NameError
        return self.id

    def getType ():
        if (self.type==None):
            raise NameError
        return self.type

    def getSolved ():
        if (self.solved==None):
            raise NameError
        return self.solved

    def getStart ():
        if (self.start==None):
            raise NameError
        return self.start

    def getUser ():
        if (user==None):
            raise NameError
        return user

    def setId (id):
        if (id<=0 or type(balance) is not 'int'):
            raise ValueError
        self.id = id

    def setType (type):
        if (type<=0 or type(type) is not 'int'):
            raise ValueError
        self.type = type 

    def setValue (solved):
        if (type(solved) is not 'bool'):     
            raise ValueError
        self.solved = solved   

    def setStart (start):
        #if (type(owing_since) is not 'string'):
        #	raise ValueError
        self.start = start 

    def setUser (user):
        self.user = user 

    def search ():
        raise NotImplementedError

    def update ():
        raise NotImplementedError  

    def create ():
        raise NotImplementedError      

    class Meta:
        managed   = False
        app_label = 'app'