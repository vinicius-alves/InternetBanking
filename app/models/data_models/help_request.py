from django.db import models
from django.contrib.auth.models import User

class Help_Request (models.Model):

    id     = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    solved = models.BooleanField()
    start  = models.DateField()
    user   = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):

        return str(self.account.id) + ' - '+ self.time.user.username+ ' - '+ str(self.start)

    class Meta:
        db_table = 'Help_Request'
        app_label = 'app'
