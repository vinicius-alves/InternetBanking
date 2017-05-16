from django.db import models
from app.models.data_models import Help_Request
from app.models import TransactionManager

class RequestManager ():

    help_request        = Help_Request()
    transaction_manager = TransactionManager()

    def getHelpRequest (self):
        if (self.help_request==None):
            raise Exception("Help_Request doesn't set")
        return self.help_request

    def getTransactionManager (self):
        if (self.transaction_manager==None):
            raise Exception("TransactionManager doesn't set")
        return self.transaction_manager

    def setHelpRequest (self, help_request):
        self.help_request = help_request 	

    def setTransactionManager (self, transaction_manager):
        self.transaction_manager = transaction_manager

    def save (self):
        self.getHelpRequest().save() 
        self.getTransactionManager().payHelp()
        self.getTransactionManager().save()  

    class Meta:
        managed   = False
        app_label = 'app'