from django.db import models
from app.models.data_models import Help_Request, Transaction, Transaction_Type
from app.models import TransactionManager

class RequestManager ():

    help_request        = Help_Request()
    transaction_manager = TransactionManager()

    def getHelpRequest (self):
        if (self.help_request==None):
            raise NameError
        return self.help_request

    def getTransactionManager (self):
        if (self.transaction_manager==None):
            raise NameError
        return self.transaction_manager

    def setHelpRequest (self, help_request):
        self.help_request = help_request 	

    def setTransactionManager (self, transaction_manager):
        self.transaction_manager = transaction_manager

    def save (self):
        transaction = Transaction()
        transaction_manager = TransactionManager()
        type = Transaction_Type.objects.get(id=7)  
        transaction.setType(type)
        transaction.setAccount(account)
        transaction_manager.setTransaction(transaction) 

        raise NotImplementedError

    class Meta:
        managed   = False
        app_label = 'app'