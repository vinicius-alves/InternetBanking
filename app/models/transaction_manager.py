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
        raise NotImplementedError("Abstract method")

    def deposit (self):
        raise NotImplementedError("Abstract method")

    def doTransfer (self):
        raise NotImplementedError("Abstract method")

    def receiveTransfer (self):
        raise NotImplementedError("Abstract method")

    def payTransferTax (self):
        raise NotImplementedError("Abstract method")

    def payExcerpt (self):
        raise NotImplementedError("Abstract method")

    def payHelp (self):
        raise NotImplementedError("Abstract method")

    def save (self):
        self.transaction.save()

    class Meta:
        abstract  = True
        managed   = False
        app_label = 'app'