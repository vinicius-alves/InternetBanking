from django.db import models
from django.contrib.auth.models import User

class Help_Request (models.Model):

    id     = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    solved = models.BooleanField(default=False)
    start  = models.DateField(auto_now_add=True)
    user   = models.OneToOneField(User,on_delete=models.CASCADE)

    def getId (self):
        return self.id

    def getType (self):
        return self.type

    def getSolved (self):
        return self.solved

    def getStart (self):
        return self.start

    def getUser (self):
        return self.user

    def setId (self,id):
        self.id = id

    def setType (self,type):
        self.type = type 

    def setValue (self,solved):
        self.solved = solved   

    def setStart (self,start):
        self.start = start 

    def setUser (self,user):
        self.user = user 

    def update (self):
        self.save()

    def __str__(self):

        return str(self.account.id) + ' - '+ self.time.user.username+ ' - '+ str(self.start)

    class Meta:
        db_table = 'Help_Request'
        app_label = 'app'
