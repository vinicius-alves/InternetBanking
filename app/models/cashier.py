from django.db import models
from app.models import Account

class Cashier ():

    account = Account()

    def getAccount ():
        if (self.account==None):
            raise NameError
        return account

    def setAccount (account):
        self.account = account 	

    def increase ():
        raise NotImplementedError

    def decrease ():
        raise NotImplementedError    

    class Meta:
        managed   = False
        app_label = 'app'