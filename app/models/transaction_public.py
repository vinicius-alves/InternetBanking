from django.db import models
from app.models import TransactionManager
from app.models.data_models import Transaction, Transaction_Type

class TransactionPublic (TransactionManager):

    def withdraw (self):
        value = self.transaction.getValue()
        self.cashier.decrease(amount=value,max=1000,can_owing=False)
        self.cashier.save()

    def deposit (self):
        value = self.transaction.getValue()
        self.cashier.increase(amount=value)
        self.cashier.save()

    def doTransfer (self):
        value = self.transaction.getValue()
        if(value>1000):
            raise Exception("O valor máximo para transferência é de RS1000,00")
        self.cashier.decrease(amount=value, can_owing=False)
        self.payTransferTax()
        self.cashier.save()

    def receiveTransfer (self):
        value = self.transaction.getValue()
        self.cashier.increase(amount=value)
        self.cashier.save()

    def payTransferTax (self):
        tax_transaction = Transaction()
        type_transaction = Transaction_Type.objects.get(id=6)  
        tax_transaction.setType(type_transaction)
        tax = 8
        tax_transaction.setValue(tax)
        self.cashier.decrease(amount=tax)
        tax_transaction.setAccount(self.transaction.getAccount())
        tax_transaction.save()

    def payExcerpt (self):
        raise NotImplementedError

    def payHelp (self):
        raise NotImplementedError

    class Meta:
        managed   = False
        app_label = 'app'