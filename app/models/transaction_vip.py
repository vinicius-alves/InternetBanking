from django.db import models
from app.models import TransactionManager
from app.models.data_models import Transaction, Transaction_Type
from datetime import datetime
from pytz import timezone

class TransactionVip (TransactionManager):

    def updateDebits(self):
        '''
        Inicialmente, chama o "Cashier" para verificar se o usuário deve pagar alguma
        taxa referente a juros sobre saldo negativo. Caso tenha, o "Cashier" já descontará este
        valor. E neste caso, o método cria uma nova transação com o valor a ser debitado, e o 
        salva no banco. Também atualiza o campo "owing_since" do objeto de conta.
        '''
        debits = self.cashier.updateDebits()
        if(debits !=0):
            tax_transaction = Transaction()
            type = Transaction_Type.objects.get(id=4)  
            tax_transaction.setType(type)
            tax_transaction.setValue(debits)
            tax_transaction.setAccount(self.transaction.getAccount())
            datetime_now = datetime.now(timezone('America/Sao_Paulo'))
            self.transaction.getAccount().setOwingSince(datetime_now)
            self.transaction.getAccount().save()
            tax_transaction.save()

    def check_if_pay_debits(self):
        '''
        Verifica se com o valor da transação a ser efetuada, o usuário que era devedor
        deixou de ser. Se isto ocorrer, define como null o valor do campo "owing_since"
        da conta do usuário.
        '''
        value = self.transaction.getValue()
        account = self.transaction.getAccount()
        balance = account.getBalance()
        if(balance<0 and value>abs(balance)):
            account.setOwingSince(None)
            account.save()
            return True
        return False

    def check_if_did_debits(self):
        '''
        Verifica se com o valor da transação a ser efetuada o usuário se tornou devedor.
        Para isto, necessita acessar a conta para obter o saldo.
        Caso o usuário se torne devedor, atualiza o campo da conta "owing_since" para
        o momento atual.
        '''
        value = self.transaction.getValue()
        account = self.transaction.getAccount()
        balance = account.getBalance()
        if(value>balance):
            datetime_now = datetime.now(timezone('America/Sao_Paulo'))
            account.setOwingSince(datetime_now)
            account.save()

    def withdraw (self):
        """
        Atualiza os juros caso o cliente seja devedor, através do método "updateDebits()".
        Verifica se, com esta transação o cliente se torna devedor.
        Após, recebe um valor através do objeto de transação e repassa para o "Cashier"
        a função de decrementar este valor.
        Em seguida, requisita que o "Cashier" salve as atualizações na conta.
        """
        value = self.transaction.getValue()
        self.updateDebits()
        self.check_if_did_debits()
        self.cashier.decrease(amount=value)
        self.cashier.save()

    def deposit (self):
        """
        Atualiza os juros caso o cliente seja devedor, através do método "updateDebits()".
        Verifica se o cliente era devedor e se com esta transação deixou de ser.
        Recebe um valor através do objeto de transação e repassa para o "Cashier"
        a função de incrementar este valor.
        Em seguida, requisita que o "Cashier" salve as atualizações na conta.
        """
        self.updateDebits()
        self.check_if_pay_debits()       
        value = self.transaction.getValue()
        self.cashier.increase(amount=value)
        self.cashier.save()

    def doTransfer (self):
        """
        Atualiza os juros caso o cliente seja devedor, através do método "updateDebits()".
        Verifica se, com esta transação o cliente se torna devedor.
        Após, recebe um valor através do objeto de transação e repassa para o "Cashier"
        a função de decrementar este valor.
        Executa o método "payTransferTax()" para gerar outra transação e salvar os dados
        sobre as taxas cobradas na transferência.
        Em seguida, requisita que o "Cashier" salve as atualizações na conta.
        """
        self.updateDebits()
        self.check_if_did_debits()        
        value = self.transaction.getValue()
        self.cashier.decrease(amount=value)
        self.payTransferTax()
        self.cashier.save()

    def receiveTransfer (self):
        """
        Atualiza os juros caso o cliente seja devedor, através do método "updateDebits()".
        Verifica se o cliente era devedor e se com esta transação deixou de ser.
        Recebe um valor através do objeto de transação e repassa para o "Cashier"
        a função de incrementar este valor.
        Em seguida, requisita que o "Cashier" salve as atualizações na conta.
        """
        self.updateDebits()
        self.check_if_pay_debits()        
        value = self.transaction.getValue()
        self.cashier.increase(amount=value)
        self.cashier.save()

    def payTransferTax (self):
        """
        Cria uma nova transação do tipo "Pagamento de taxa de transferência bancária", em
        seguida ordena ao "Cashier" que decremente a taxa 8% do valor da última transação da 
        conta e após, salva a transação no banco.
        """ 
        tax_transaction = Transaction()
        type_transaction = Transaction_Type.objects.get(id=6)  
        tax_transaction.setType(type_transaction)
        tax = self.transaction.getValue()*0.08
        tax_transaction.setValue(tax)
        self.cashier.decrease(amount=tax)
        tax_transaction.setAccount(self.transaction.getAccount())
        tax_transaction.save()

    def payExcerpt (self):
        '''
        Não utilizado. Pois não há taxas sobre emissão de extrato. 
        '''
        self.updateDebits()
        self.check_if_did_debits()        
        raise NotImplementedError

    def payHelp (self):
        """
        Atualiza os juros caso o cliente seja devedor, através do método "updateDebits()".
        Verifica se, com esta transação o cliente se torna devedor.
        Após, repassa para o "Cashier" a função de decrementar o valor fixo de R$ 50,00.
        Em seguida, requisita que o "Cashier" salve as atualizações na conta.
        """
        self.updateDebits()
        self.check_if_did_debits()        
        self.cashier.decrease(amount=50)
        self.cashier.save()

    class Meta:
        managed   = False
        app_label = 'app'