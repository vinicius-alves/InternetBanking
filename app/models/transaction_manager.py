from django.db import models
from app.models import Transaction, Cashier

class TransactionManager ():

    cashier     =  Cashier()
    transaction =  Transaction()

    def getTransaction ():
        if (self.transaction==None):
            raise NameError
        return self.transaction

    def setTransaction (transaction):
        self.transaction = transaction

    def withdraw ():
        raise NotImplementedError

    def deposit ():
        raise NotImplementedError

    def doTransfer ():
        raise NotImplementedError

    def receiveTransfer ():
        raise NotImplementedError

    def payExcerpt ():
        raise NotImplementedError

    def payHelp ():
        raise NotImplementedError

    def save ():
        self.transaction.save()

    class Meta:
        abstract  = True
        managed   = False
        app_label = 'app'