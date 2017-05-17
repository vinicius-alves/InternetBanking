from django.db import models

class Transaction_Type(models.Model):

    """
    Classe de dados que representa os tipos de transação de conta. 
    Possui apenas o campo name (nome), e é limitada a algumas opções pré-estabelecidas.
    """

    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    
    # Transaction Types:
    type1 = "Saque"
    type2 = "Depósito"
    type3 = "Pagamento de Extrato"
    type4 = "Juros sobre saldo negativo"
    type5 = "Transferência bancária"
    type6 = "Pagamento de taxa de transferência bancária"
    type7 = "Solicitação de visita do gerente"
    type8 = "Recebimento de transferência bancária"

    Transaction_Types = (
        (type1, type1), (type2, type2), (type3, type3), (type4, type4),
        (type5, type5), (type6, type6), (type7, type7), (type8, type8)
    )
    name = models.CharField(
        max_length = 50,
        choices = Transaction_Types
    )

    def __str__(self):

        return str(self.id) + ' - '+ self.name

    class Meta:
        db_table = 'Transaction_Type'
        app_label = 'app'
