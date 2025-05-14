from django.db import models
from django.contrib.auth.models import User

# Create your models here.







class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.BigIntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    joining_date = models.DateTimeField(auto_now_add=True)
    total_project = models.IntegerField(default=1)
    total_test_case = models.IntegerField(default=1)
    total_defects_found = models.IntegerField(default=1)
    total_defects_pending = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username
