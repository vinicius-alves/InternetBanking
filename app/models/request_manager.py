from django.db import models
from app.models import HelpRequest, TransactionManager

class RequestManager ():

    help_request        = HelpRequest()
    transaction_manager = TransactionManager()

    def getHelpRequest ():
        if (self.help_request==None):
            raise NameError
        return self.help_request

    def getTransactionManager ():
        if (self.transaction_manager==None):
            raise NameError
        return self.transaction_manager

    def setAccount (help_request):
        self.help_request = help_request 	

    def setTransactionManager (transaction_manager):
        self.transaction_manager = transaction_manager

    def save ():
        raise NotImplementedError

    class Meta:
        managed   = False
        app_label = 'app'