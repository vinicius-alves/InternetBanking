from django.db import models
from app.models.data_models import Account, Transaction
from app.models import TransactionManager

class AccountHistory ():

    """
    Esta classe é responsável por processar as solicitações de extrato de conta.
    Ela tem como membro um objeto do tipo TransactionManager, porém não o utiliza, dado
    que até o momento não há cobrança de taxas pela requisição de extrato.
    """

    account             = Account()
    transaction_manager = TransactionManager()

    def __init__(self, account): 
        self.setAccount(account)

    def getAccount (self):
        """
        Retorna o objeto de conta do usuário.
        """
        if (self.account==None):
            raise Exception("Account doesn't set")
        return self.account

    def getTransactionManager (self):
        """
        Retorna o objeto gerenciador de transações.
        """
        if (self.transaction_manager==None):
            raise Exception("TransactionManager doesn't set")
        return self.transaction_manager

    def setAccount (self, account):
        """
        Define o objeto de conta do usuário.
        """
        self.account = account 	

    def setTransactionManager (self, transaction_manager):
        """
        Define o objeto gerenciador de transações.
        """       
        self.transaction_manager = transaction_manager

    def getExcerpt (self):
        """
        Retorna uma lista de objetos do tipo "Transaction" que sejam ligados a conta
        do usuário requerente.
        """
        transactions = list(Transaction.objects.filter(account=self.account))
        return transactions

    class Meta:
        managed   = False
        app_label = 'app'