from django.db import models
from app.models.data_models import Account, Transaction
from app.models import TransactionManager

class AccountHistory ():

    account             = Account()
    transaction_manager = TransactionManager()

    def __init__(self, account): 
        self.setAccount(account)

    def getAccount (self):
        if (self.account==None):
            raise Exception("Account doesn't set")
        return self.account

    def getTransactionManager (self):
        if (self.transaction_manager==None):
            raise Exception("TransactionManager doesn't set")
        return self.transaction_manager

    def setAccount (self, account):
        self.account = account 	

    def setTransactionManager (self, transaction_manager):
        self.transaction_manager = transaction_manager

    def getExcerpt (self):
        transactions = list(Transaction.objects.filter(account=self.account))
        return transactions

    class Meta:
        managed   = False
        app_label = 'app'