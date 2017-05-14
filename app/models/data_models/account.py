from django.db import models
from django.contrib.auth.models import User

class Account (models.Model):

    id          = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    balance     = models.IntegerField()
    owing       = models.BooleanField()
    owing_since = models.DateField()
    user        = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' - '+ self.user.username

    class Meta:
        db_table = 'Account'
        app_label = 'app'
