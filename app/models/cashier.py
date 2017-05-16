from django.db import models
from app.models.data_models import Account
from datetime import datetime
from pytz import timezone
from math import pow

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
        balance = self.account.getBalance() 
        self.account.setBalance(balance+amount)

    def decrease (self, amount, max=2147483647, can_owing=True):
        if(amount<=0):
            raise NameError
        elif(amount > max):
            raise Exception("Not Allowed")

        balance = self.account.getBalance() 
        if(not(can_owing) and (amount > balance)):
            raise Exception("Not Allowed")

        self.account.setBalance(balance-amount)

    def save(self):
        self.account.save() 

    def updateDebits(self):
        debits = 0
        owing = self.account.getOwing()
        if(not(owing)):
            return debits

        minutes_owing = self.minutesOwing()
        if(minutes_owing==0):
            return debits

        balance = self.account.getBalance()
        interest_rate = pow(1.001,minutes_owing) 
        debits = abs(balance)*(interest_rate-1)
        self.decrease(debits)  
        
        return debits


    def minutesOwing(self):
        time_since = self.account.getOwingSince()
        if(time_since== None):
            return 0
        time_now   = datetime.now(timezone('America/Sao_Paulo'))

        time_delta_difference = time_now - time_since
        minutes = (time_delta_difference.seconds//60)%60

        if(minutes<0):
            raise NameError
        
        return minutes

    class Meta:
        managed   = False
        app_label = 'app'