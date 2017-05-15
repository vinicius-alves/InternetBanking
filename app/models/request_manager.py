from django.db import models
from app.models.data_models import Help_Request
from app.models import TransactionManager

class RequestManager ():

    help_request        = HelpRequest()
    transaction_manager = TransactionManager()

    def getHelpRequest (self):
        if (self.help_request==None):
            raise NameError
        return self.help_request

    def getTransactionManager (self):
        if (self.transaction_manager==None):
            raise NameError
        return self.transaction_manager

    def setAccount (self, help_request):
        self.help_request = help_request 	

    def setTransactionManager (self, transaction_manager):
        self.transaction_manager = transaction_manager

    def save (self):
        raise NotImplementedError

    class Meta:
        managed   = False
        app_label = 'app'