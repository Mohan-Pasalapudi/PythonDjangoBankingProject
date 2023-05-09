from random import random
from random import randint
from django.db import models
from django.utils import timezone
import random
from django.contrib.auth.models import User

from django.db import models


class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "admin_table"


class Employee(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pics', default='profile_pics/')
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices = (("M", "Male"), ("F", "Female"), ("Others", "Prefer not to say"))
    gender = models.CharField(blank=False, choices=gender_choices, max_length=10)
    date_of_birth = models.CharField(max_length=20, blank=False)
    age = models.IntegerField(blank=False)
    aadhar_no = models.BigIntegerField(blank=False, unique=True)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    username = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    contact = models.BigIntegerField(blank=False, unique=True)
    address = models.CharField(max_length=200, blank=False)
    registrationtime = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "employee_table"


def generate_account_no():
    return random.randint(1000000000, 9999999999)


class AccountHolder(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pics', default='profile_pics/default.jpg')
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices = (("M", "Male"), ("F", "Female"), ("Others", "Prefer not to say"))
    gender = models.CharField(blank=False, choices=gender_choices, max_length=10)
    date_of_birth = models.CharField(max_length=20, blank=False)
    age = models.IntegerField(blank=False)
    aadhar_no = models.BigIntegerField(blank=False, unique=True)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    username = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    contact = models.BigIntegerField(blank=False, unique=True)
    address = models.CharField(max_length=200, blank=False)
    account_no = models.PositiveIntegerField(primary_key=True, unique=True, default=generate_account_no)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    registrationtime = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return str(self.account_no)

    class Meta:
        db_table = "accountHolder_table"


class Transaction(models.Model):
    from_account = models.ForeignKey('AccountHolder', related_name='sent_transactions', on_delete=models.CASCADE)
    to_account = models.ForeignKey('AccountHolder', related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Transaction {self.pk} - {self.from_account} to {self.to_account}'

    class Meta:
        db_table = "transaction_table"