from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=30,blank = True)
    location = models.CharField(max_length=30,blank = True)
    email= models.EmailField(null=True,blank = True)
    phone = models.CharField(max_length=10,blank = True)
    reference =models.CharField(max_length=30,blank = True)
    project_name= models.CharField(max_length=30,blank = True)
    domain_name= models.CharField(max_length=30,blank = True)
    acc_name= models.CharField(max_length=30,blank = True)
    acc_password= models.CharField(max_length=30,blank = True)
    purchase_date= models.DateField(null=True, blank=True)
    expiry_date= models.DateField(null=True,blank = True)
    amount= models.IntegerField(null=True,blank = True)

    hosting_account=models.CharField(max_length=30,null=True,blank = True)
    hosting_pass = models.CharField(max_length=10,null=True,blank = True)
    hosting_date = models.DateField(null=True,blank = True)
    hosting_expiry_date=models.DateField(null=True, blank = True)
    hosting_amount=models.IntegerField(null=True,blank = True)

    sll_type=models.CharField(max_length=30,null=True,blank = True)
    sll_account=models.CharField(max_length=30,null=True,blank = True)
    sll_date=models.DateField(null=True,blank = True)
    sll_expiry_date=models.DateField(null=True,blank = True)
    sll_amount=models.IntegerField(null=True,blank = True)

    amc_date=models.DateField(null=True,blank = True)
    amc_expiry_date=models.DateField(null=True,blank = True)
    amc_amount=models.IntegerField(null=True,blank = True)

    project_update=models.CharField(max_length=30,null=True,blank = True)
    updated_date=models.DateField(null=True,blank = True)
    project_details=models.CharField(max_length=30,null=True,blank = True)
    time_spent=models.TextField(max_length=30,null=True,blank = True)

    chatbot_type=models.CharField(max_length=30,null=True,blank = True)
    credits_purchased=models.CharField(max_length=30,null=True,blank = True)
    chatbot_amount=models.IntegerField(null=True,blank = True)
    chatbot_date=models.DateField(null=True,blank=True)
    chatbot_last_date=models.DateField(null=True,blank = True)




    def __str__(self):
        return 'Client Name : {0}'.format(self.client_name.title())
