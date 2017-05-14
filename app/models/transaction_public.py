from django.db import models
from app.models import TransactionManager

class TransactionPublic (TransactionManager):

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

    class Meta:
        managed   = False
        app_label = 'app'