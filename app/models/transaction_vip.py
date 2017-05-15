from django.db import models
from app.models import TransactionManager

class TransactionVip (TransactionManager):

    def withdraw (self):
        raise NotImplementedError

    def deposit (self):
        raise NotImplementedError

    def doTransfer (self):
        raise NotImplementedError

    def receiveTransfer (self):
        raise NotImplementedError

    def payExcerpt (self):
        raise NotImplementedError

    def payHelp (self):
        raise NotImplementedError

    class Meta:
        managed   = False
        app_label = 'app'