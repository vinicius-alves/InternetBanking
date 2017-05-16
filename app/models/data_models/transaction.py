from django.db import models
from app.models.data_models import Account, Transaction_Type

class Transaction (models.Model):

    id      = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    time    = models.DateTimeField(auto_now_add=True)
    value   = models.IntegerField(default=0)
    type    = models.ForeignKey(Transaction_Type)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

    def getId (self):
        return self.id

    def getType (self):
        return self.type

    def getValue (self):
        return self.value

    def getTime (self):
        return self.time

    def getAccount (self):
        return self.account

    def setId (self,id):
        self.id = id

    def setType (self,type):
        self.type = type 

    def setValue (self,value):
        self.value = value   

    def setTime (self,time):
        self.time = time 

    def setAccount (self,account):
        self.account = account  

    def update (self):
        self.save()

    def as_json(self):

        json_dict = {}
        json_dict["id"]    = self.id
        json_dict["time"]  = self.time.strftime("%d/%m/%Y %H:%M:%S")
        json_dict["value"] = self.value
        json_dict["type"]  = self.type.name

        deposito = Transaction_Type.objects.get(id=2)
        recebimento_transferencia = Transaction_Type.objects.get(id=8)

        if(self.type == deposito or self.type == recebimento_transferencia):
            json_dict["mode"]  = "increase"
        else:
            json_dict["mode"]  = "decrease"

        return json_dict

    def __str__(self):

        return str(self.account.id) + ' - '+ str(self.time)+ ' - '+ str(self.value)

    class Meta:
        db_table = 'Transaction'
        app_label = 'app'
