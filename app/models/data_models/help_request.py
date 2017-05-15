from django.db import models
from django.contrib.auth.models import User

class Help_Request (models.Model):

    id     = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    solved = models.BooleanField(default=False)
    start  = models.DateField(auto_now_add=True)
    user   = models.OneToOneField(User,on_delete=models.CASCADE)

    def getId ():
        return self.id

    def getType ():
        return self.type

    def getSolved ():
        return self.solved

    def getStart ():
        return self.start

    def getUser ():
        return user

    def setId (id):
        self.id = id

    def setType (type):
        self.type = type 

    def setValue (solved):
        self.solved = solved   

    def setStart (start):
        self.start = start 

    def setUser (user):
        self.user = user 

    def update ():
        self.save()

    def __str__(self):

        return str(self.account.id) + ' - '+ self.time.user.username+ ' - '+ str(self.start)

    class Meta:
        db_table = 'Help_Request'
        app_label = 'app'
