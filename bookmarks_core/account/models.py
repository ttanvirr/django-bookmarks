from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Make the email field unique and required
    email = models.EmailField(unique=True)
