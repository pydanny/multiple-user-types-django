from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Types(models.TextChoices):
        SPY = "SPY", "Spy"
        DRIVER = "DRIVER", "Driver"

    # What type of user are we?
    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=Types.SPY
    )

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class SpyManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SPY)


class DriverManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.DRIVER)


class Spy(User):
    objects = SpyManager()

    class Meta:
        proxy = True

    def whisper(self):
        return "whisper"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.SPY
        return super().save(*args, **kwargs)


class Driver(User):
    objects = DriverManager()

    class Meta:
        proxy = True

    def accelerate(self):
        return "Go faster"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.DRIVER
        return super().save(*args, **kwargs)
