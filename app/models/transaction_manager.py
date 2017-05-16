from django.db import models
from app.models.data_models import Transaction
from app.models import Cashier

class TransactionManager ():

    transaction = Transaction()
    cashier     = Cashier()

    def getTransaction (self):
        if (self.transaction==None):
            raise NameError
        return self.transaction

    def setTransaction (self, transaction):
        self.transaction = transaction
        self.cashier.setAccount(transaction.getAccount())

    def withdraw (self):
        raise NotImplementedError

    def deposit (self):
        raise NotImplementedError

    def doTransfer (self):
        raise NotImplementedError

    def receiveTransfer (self):
        raise NotImplementedError

    def payTransferTax (self):
        raise NotImplementedError

    def payExcerpt (self):
        raise NotImplementedError

    def payHelp (self):
        raise NotImplementedError

    def save (self):
        self.transaction.save()

    class Meta:
        abstract  = True
        managed   = False
        app_label = 'app'