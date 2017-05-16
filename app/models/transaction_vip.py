from django.db import models
from app.models import TransactionManager
from app.models.data_models import Transaction, Transaction_Type
from datetime import datetime
from pytz import timezone

class TransactionVip (TransactionManager):

    def updateDebits(self):
        debits = self.cashier.updateDebits()
        if(debits !=0):
            tax_transaction = Transaction()
            type = Transaction_Type.objects.get(id=4)  
            tax_transaction.setType(type)
            tax_transaction.setValue(debits)
            tax_transaction.setAccount(self.transaction.getAccount())
            datetime_now = datetime.now(timezone('America/Sao_Paulo'))
            self.transaction.getAccount().setOwingSince(datetime_now)
            self.transaction.getAccount().save()
            tax_transaction.save()

    def check_if_pay_debits(self):
        value = self.transaction.getValue()
        account = self.transaction.getAccount()
        balance = account.getBalance()
        if(balance<0 and value>abs(balance)):
            account.setOwingSince(None)
            account.save()
            return True
        return False

    def check_if_did_debits(self):
        value = self.transaction.getValue()
        account = self.transaction.getAccount()
        balance = account.getBalance()
        if(value>balance):
            datetime_now = datetime.now(timezone('America/Sao_Paulo'))
            account.setOwingSince(datetime_now)
            account.save()

    def withdraw (self):
        value = self.transaction.getValue()
        self.updateDebits()
        self.check_if_did_debits()
        self.cashier.decrease(amount=value)
        self.cashier.save()

    def deposit (self):
        self.updateDebits()
        self.check_if_pay_debits()       
        value = self.transaction.getValue()
        self.cashier.increase(amount=value)
        self.cashier.save()

    def doTransfer (self):
        self.updateDebits()
        self.check_if_did_debits()        
        value = self.transaction.getValue()
        self.cashier.decrease(amount=value)
        raise NotImplementedError 
        self.cashier.save()

    def receiveTransfer (self):
        self.updateDebits()
        self.check_if_pay_debits()        
        value = self.transaction.getValue()
        self.cashier.increase(amount=value)
        self.cashier.save()

    def payExcerpt (self):
        self.updateDebits()
        self.check_if_did_debits()        
        raise NotImplementedError

    def payHelp (self):
        self.updateDebits()
        self.check_if_did_debits()        
        self.cashier.decrease(amount=50)
        self.cashier.save()

    class Meta:
        managed   = False
        app_label = 'app'