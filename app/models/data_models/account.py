from django.db import models
from django.contrib.auth.models import User

class Account (models.Model):

    id          = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    balance     = models.IntegerField(default=0)
    owing       = models.BooleanField(default=False)
    owing_since = models.DateField(blank=True)
    user        = models.OneToOneField(User,on_delete=models.CASCADE)

    def getId (self):
        return self.id

    def getBalance (self):
        return self.balance

    def getOwing (self):
        return self.owing

    def getOwingSince (self):
        return self.owing_since

    def getUser (self):
        return self.user

    def setId (self,id):
        self.id = id

    def setBalance (self,balance):
        self.balance = balance

    def setOwing (self,owing):
        self.owing = owing

    def setOwingSince (self,owing_since):
        self.owing_since = owing_since

    def setUser (self,user):
        self.user = user

    def update (self):
        self.save()       

    def __str__(self):
        return str(self.id) + ' - '+ self.user.username

    class Meta:
        db_table = 'Account'
        app_label = 'app'
