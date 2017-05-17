from django.db import models
from app.models import TransactionManager
from app.models.data_models import Transaction, Transaction_Type

class TransactionPublic (TransactionManager):

    def withdraw (self):
        """
        Recebe um valor através do objeto de transação e repassa para o "Cashier"
        a função de decrementar este valor.
        Em seguida, requisita que o "Cashier" salve as atualizações na conta.
        """
        value = self.transaction.getValue()
        self.cashier.decrease(amount=value,max=1000,can_owing=False)
        self.cashier.save()

    def deposit (self):
        """
        Recebe um valor através do objeto de transação e repassa para o "Cashier"
        a função de incrementar este valor.
        Em seguida, requisita que o "Cashier" salve as atualizações na conta.
        """
        value = self.transaction.getValue()
        self.cashier.increase(amount=value)
        self.cashier.save()

    def doTransfer (self):
        """
        Recebe um valor através do objeto de transação e verifica se o valor é maior
        que o máximo permitido (1000), caso seja dispara uma exceção. 
        Caso isto não ocorra, repassa para o "Cashier" a função de decrementar este valor.
        Executa o método "payTransferTax()" para gerar outra transação e salvar os dados
        sobre as taxas cobradas na transferência.
        Em seguida, requisita que o "Cashier" salve as atualizações na conta.
        """
        value = self.transaction.getValue()
        if(value>1000):
            raise Exception("O valor máximo é de RS1000,00")
        self.cashier.decrease(amount=value, can_owing=False)
        self.payTransferTax()
        self.cashier.save()

    def receiveTransfer (self):
        """
        Recebe um valor através do objeto de transação e repassa para o "Cashier"
        a função de incrementar este valor.
        Em seguida, requisita que o "Cashier" salve as atualizações na conta.
        """        
        value = self.transaction.getValue()
        self.cashier.increase(amount=value)
        self.cashier.save()

    def payTransferTax (self):
        """
        Cria uma nova transação do tipo "Pagamento de taxa de transferência bancária", em
        seguida ordena ao "Cashier" que decremente a taxa fixa de R$ 8,00 da conta e após, 
        salva a transação no banco.
        """        
        tax_transaction = Transaction()
        type_transaction = Transaction_Type.objects.get(id=6)  
        tax_transaction.setType(type_transaction)
        tax = 8
        tax_transaction.setValue(tax)
        self.cashier.decrease(amount=tax)
        tax_transaction.setAccount(self.transaction.getAccount())
        tax_transaction.save()

    def payExcerpt (self):
        '''
        Não utilizado. Pois não há taxas sobre emissão de extrato. 
        '''
        raise NotImplementedError

    def payHelp (self):
        '''
        Não utilizado. Pois este tipo de usuário não pode realizar solicitações de ajuda,
        segundo às regras de negócio. 
        '''
        raise NotImplementedError

    class Meta:
        managed   = False
        app_label = 'app'