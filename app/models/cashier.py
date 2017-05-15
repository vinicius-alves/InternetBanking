from django.db import models
from app.models.data_models import Account
from datetime import datetime

class Cashier ():

    account = Account()

    def getAccount (self):
        if (self.account==None):
            raise NameError
        return self.account

    def setAccount (self, account):
        self.account = account 	

    def increase (self, amount, max=2147483647):
        if(amount<=0):
            raise NameError
        elif(amount > max):
            raise Exception("Not Allowed")
        self.account.balance += amount

    def decrease (self, amount, max=2147483647):
        if(amount<=0):
            raise NameError
        elif(amount > max):
            raise Exception("Not Allowed")
        self.account.balance -= amount 

    def save(self):
        self.account.save() 

    def updateDebits(self):
        if(self.account.balance>=0):
            return False
        

        raise NotImplementedError


    def differenceMinutes(self):
        time_since = self.account.getTime()
        time_now   = datetime.now()

        minutes = (time_now - time_since).minutes

        if(minutes<0):
            raise NameError
        
        return minutes

    class Meta:
        managed   = False
        app_label = 'app'