from django.db import models

class Transaction_Type(models.Model):

    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    
    # Transaction Types:
    Transaction_Types = (
        ('Type1', 'Type1'),
        ('Type2', 'Type2'),
        ('Type3', 'Type3'),
    )
    name = models.CharField(
        max_length = 30,
        choices = Transaction_Types
    )

    def __str__(self):

        return str(self.id) + ' - '+ self.name

    class Meta:
        db_table = 'Transaction_Type'
        app_label = 'app'
