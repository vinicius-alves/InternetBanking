from django.db import models
from app.models.data_models import Help_Request
from app.models import TransactionManager

class RequestManager ():

    """
    Esta classe é responsável pelo gerenciamento de requisições de ajuda.
    Ela salva novos pedidos de ajuda no banco e utiliza um objeto do tipo
    "TransactionManager" para cobrar os encargos sobre as solicitações.
    """

    help_request        = Help_Request()
    transaction_manager = TransactionManager()

    def getHelpRequest (self):
        """
        Retorna o objeto de requisição de ajuda.
        """
        if (self.help_request==None):
            raise Exception("Help_Request doesn't set")
        return self.help_request

    def getTransactionManager (self):
        """
        Retorna o objeto gerenciador de transações.
        """
        if (self.transaction_manager==None):
            raise Exception("TransactionManager doesn't set")
        return self.transaction_manager

    def setHelpRequest (self, help_request):
        """
        Define o objeto de requisição de ajuda.
        """
        self.help_request = help_request 	

    def setTransactionManager (self, transaction_manager):
        """
        Define o objeto gerenciador de transações.
        """
        self.transaction_manager = transaction_manager

    def save (self):
        """
        Salva o objeto de requisição de ajuda no banco.
        Utiliza o TransactionManager para debitar um valor fixo na conta do usuario e 
        salvar a transação correspondente no banco.
        """
        self.getHelpRequest().save() 
        self.getTransactionManager().payHelp()
        self.getTransactionManager().save()  

    class Meta:
        managed   = False
        app_label = 'app'