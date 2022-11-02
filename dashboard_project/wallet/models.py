from django.db import models

# Create your models here.

class WalletUsers(models.Model):
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=20, decimal_places=2)
   
    def _str_(self):
        return f'{self.firstname} - {self.lastname}'
        