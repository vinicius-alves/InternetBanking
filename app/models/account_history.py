from django.db import models
from app.models import Account, TransactionManager

class Account_History ():

    account             = Account()
    transaction_manager = TransactionManager()

    def getAccount ():
        if (self.account==None):
            raise NameError
        return self.account

    def getTransactionManager ():
        if (self.transaction_manager==None):
            raise NameError
        return self.transaction_manager

    def setAccount (account):
        self.account = account 	

    def setTransactionManager (transaction_manager):
        self.transaction_manager = transaction_manager

    def getExcerpt ():
        raise NotImplementedError

    class Meta:
        managed   = False
        app_label = 'app'