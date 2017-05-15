from django.db import models
from app.models.data_models import Account

class Cashier ():

    account = Account()

    def getAccount (self):
        if (self.account==None):
            raise NameError
        return self.account

    def setAccount (self, account):
        self.account = account 	

    def increase (self, amount, max=0):
        if(amount<=0):
            raise NameError
        elif(amount > max):
            raise Exception("Not Allowed")
        self.account.balance += amount

    def decrease (self, amount, max=0):
        if(amount<=0):
            raise NameError
        elif(amount > max):
            raise Exception("Not Allowed")
        self.account.balance -= amount 

    def save(self):
        self.account.save()  

    class Meta:
        managed   = False
        app_label = 'app'