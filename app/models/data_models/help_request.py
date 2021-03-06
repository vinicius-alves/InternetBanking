from django.db import models
from django.contrib.auth.models import User

class Help_Request (models.Model):

    """
    Classe de dados do tipo requisição de ajuda. Possui os campos de solved, que representa
    se o caso já foi resolvido, start, que representa o momento em que o usuário requisitou ajuda 
    e uma chave para o usuário correspondente.
    """

    id     = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    solved = models.BooleanField(default=False)
    start  = models.DateTimeField(auto_now_add=True)
    user   = models.ForeignKey(User,on_delete=models.CASCADE)

    def getId (self):
        return self.id

    def getSolved (self):
        return self.solved

    def getStart (self):
        return self.start

    def getUser (self):
        return self.user

    def setId (self,id):
        self.id = id

    def setValue (self,solved):
        self.solved = solved   

    def setStart (self,start):
        self.start = start 

    def setUser (self,user):
        self.user = user 

    def update (self):
        self.save()

    def __str__(self):

        return str(self.id) + ' - '+ self.user.username+ ' - '+ str(self.start)

    class Meta:
        db_table = 'Help_Request'
        app_label = 'app'
