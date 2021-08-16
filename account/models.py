from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    displayname = models.CharField(max_length=50, null=True)
    telephone = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        verbose_name = 'Employee'

    def __str__(self):
        return "{}".format(self.user.__str__())
