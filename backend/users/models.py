from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from model_utils.fields import (
    AutoCreatedField,
    AutoLastModifiedField,
)


class User(AbstractUser):
    created = AutoCreatedField(_('created'))
    modified = AutoLastModifiedField(_('modified'))

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    togglApiToken = CharField(blank=True, null=True, max_length=32)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
