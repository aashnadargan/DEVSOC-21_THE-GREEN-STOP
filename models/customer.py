from django.db import models
from django.core.validators import MinLengthValidator

class Customer(models.Model):
    username = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        
        return False
    


