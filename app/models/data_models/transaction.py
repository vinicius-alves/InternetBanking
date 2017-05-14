from django.db import models
from app.models.data_models import Account, Transaction_Type

class Transaction (models.Model):

    id      = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    time    = models.DateField()
    value   = models.IntegerField()
    type    = models.ForeignKey(Transaction_Type)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

    def __str__(self):

        return str(self.account.id) + ' - '+ str(self.time)+ ' - '+ str(self.value)

    class Meta:
        db_table = 'Transaction'
        app_label = 'app'
