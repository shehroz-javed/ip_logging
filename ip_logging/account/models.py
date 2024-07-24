from django.db import models
from django.contrib.auth.models import AbstractUser

from ip_logging.models import BaseTimeStampModel

from account.manager import UserManager


class User(AbstractUser):

    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    objects = UserManager()


class RequestCount(BaseTimeStampModel):

    ip = models.CharField(max_length=255)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ip}-{self.count}"
