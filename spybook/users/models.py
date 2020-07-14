from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Types(models.TextChoices):
        SPY = "SPY", "Spy"
        DRIVER = "DRIVER", "Driver"

    base_type = Types.SPY

    # What type of user are we?
    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type
    )

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class SpyManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SPY)


class DriverManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.DRIVER)


class Spy(User):
    objects = SpyManager()
    base_type = User.Types.SPY

    class Meta:
        proxy = True

    def whisper(self):
        return "whisper"


class Driver(User):
    base_type = User.Types.DRIVER
    objects = DriverManager()

    class Meta:
        proxy = True

    def accelerate(self):
        return "Go faster"

