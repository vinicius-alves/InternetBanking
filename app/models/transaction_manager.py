from django.db import models
from app.models.data_models import Transaction
from app.models import Cashier

class TransactionManager ():
    '''
    Classe reponsável pelo gerenciamento de transações. Tem basicamente duas funcionalidades: 
    incrementar ou decrementar o saldo do usuário, isto é feito pela classe auxiliar "Cashier", 
    e salvar novas transações no banco de dados.
    Como membro interno, tem-se um objeto do tipo "Transaction" e um objeto "Cashier".
    '''

    transaction = Transaction()
    cashier     = Cashier()

    def getTransaction (self):
        """
        Retorna o objeto de transação.
        """
        if (self.transaction==None):
            raise NameError
        return self.transaction

    def setTransaction (self, transaction):
        """
        Define o objeto de transação.
        """
        self.transaction = transaction
        self.cashier.setAccount(transaction.getAccount())

    def withdraw (self):
        """
        Método abstrato: deve implementar a funcionalidade de decremento de um valor na conta 
        com suas respectivas taxas de saque e também possibilitar o armazenamento da transação.
        """
        raise NotImplementedError("Abstract method")

    def deposit (self):
        """
        Método abstrato: deve implementar a funcionalidade de incremento de um valor na conta 
        e também possibilitar o armazenamento da transação.
        """
        raise NotImplementedError("Abstract method")

    def doTransfer (self):
        """
        Método abstrato: deve implementar a funcionalidade de decremento de um valor na conta 
        com suas respectivas taxas de transferência e também possibilitar o armazenamento da transação.
        """
        raise NotImplementedError("Abstract method")

    def receiveTransfer (self):
        """
        Método abstrato: deve implementar a funcionalidade de incremento de um valor na conta 
        e também possibilitar o armazenamento da transação.
        """
        raise NotImplementedError("Abstract method")

    def payTransferTax (self):
        """
        Método abstrato: deve implementar a funcionalidade de decremento de um valor na conta 
        referente às taxas de transferência e também possibilitar o armazenamento da transação.
        """
        raise NotImplementedError("Abstract method")

    def payExcerpt (self):
        """
        Método abstrato: poderia implementar a funcionalidade de decremento de um valor na conta 
        referente às taxas de emissão de extrato e também possibilitar o armazenamento dessas transações.
        Porém, não foi levantado como requisito.
        """
        raise NotImplementedError("Abstract method")

    def payHelp (self):
        """
        Método abstrato: deve implementar a funcionalidade de decremento de um valor fixo na conta 
        e também possibilitar o armazenamento da transação.
        """
        raise NotImplementedError("Abstract method")

    def save (self):
        """
        Salva a transação no banco de dados.
        """
        self.transaction.save()

    class Meta:
        abstract  = True
        managed   = False
        app_label = 'app'