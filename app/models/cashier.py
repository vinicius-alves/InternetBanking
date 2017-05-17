from django.db import models
from app.models.data_models import Account
from datetime import datetime
from pytz import timezone
from math import pow

class Cashier ():

    """
    Classe-parte de TransactionManager, responsável pela atualização do saldo de conta do usuário.
    Esta, apenas atualiza o saldo do usuário de acordo com as regras de negócio da aplicação.
    Isto é feito principalmente através dos métodos "increase" e "decrease".
    Aqui também há um método "updateDebits" que se encarrega de descontar no saldo os juros por
    saldo negativo de algum cliente.
    Como membro interno, tem-se apenas um objeto do tipo "Account".
    """

    account = Account()

    def getAccount (self):
        """
        Retorna o objeto de conta do usuário.
        """
        if (self.account==None):
            raise NameError
        return self.account

    def setAccount (self, account):
        """
        Define o objeto de conta do usuário.
        """
        self.account = account 	

    def increase (self, amount, max=2147483647):
        """
        Incrementa um valor, representado por "amount", no saldo da conta. 
        Há um argumento opcional "max" que representa o máximo permitido.
        Caso, se tente incrementar além do máximo, gera uma exceção.
        """
        if(amount<=0):
            raise Exception("Internal Error")
        elif(amount > max):
            raise Exception("O valor da transação não pode exceder R$"+str(max))
        balance = self.account.getBalance() 
        self.account.setBalance(balance+amount)

    def decrease (self, amount, max=2147483647, can_owing=True):
        """
        Decrementa um valor, representado por "amount", no saldo da conta. 
        Há um argumento opcional "max" que representa o máximo permitido.
        Caso, se tente decrementar além do máximo, gera uma exceção.
        E também gera uma exceção quando o usuário não pode ter saldo negativo e 
        tenta sacar além do permitido, representado pelo argumento "can_owing".
        """
        if(amount<=0):
            raise Exception("O valor da transação deve ser maior que zero.")
        elif(amount > max):
            raise Exception("O valor da transação não pode exceder R$"+str(max))

        balance = self.account.getBalance() 
        if(not(can_owing) and (amount > balance)):
            raise Exception("O valor da transação não pode exceder R$"+str(balance))

        self.account.setBalance(balance-amount)

    def save(self):
        '''
        Salva as atualizações na conta.
        '''
        self.account.save() 

    def updateDebits(self):
        '''
        Verifica se o usuário está com saldo negativo, se não estiver, retorna quantidade 
        de débitos igual a zero. Caso esteja, calcula através de "minutesOwing()" quantos
        minutos está devendo. Em seguida, calcula a taxa a ser cobrada e decrementa da conta.
        '''
        debits = 0
        owing = self.account.getOwing()
        if(not(owing)):
            return debits

        minutes_owing = self.minutesOwing()
        if(minutes_owing==0):
            return debits

        balance = self.account.getBalance()
        interest_rate = pow(1.001,minutes_owing) 
        debits = abs(balance)*(interest_rate-1)
        self.decrease(debits) 
        
        return debits


    def minutesOwing(self):
        '''
        Calcula a diferença de tempo em minutos entre a hora atual e a hora armazenada
        como atributo na conta de usuário "owing_since".
        '''

        time_since = self.account.getOwingSince()
        if(time_since== None):
            return 0
        time_now   = datetime.now(timezone('America/Sao_Paulo'))

        time_delta_difference = time_now - time_since
        minutes = (time_delta_difference.seconds//60)%60

        if(minutes<0):
            raise Exception("Internal Error")
        
        return minutes

    class Meta:
        managed   = False
        app_label = 'app'