from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from base.models import MockSet
from django.contrib.auth.models import User

class person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    dob = models.DateField(blank=True)
    registered_on = models.DateTimeField(auto_now_add=True)
    mock_test_solved = models.ManyToManyField(MockSet)

    def __str__(self):
        return self.name
