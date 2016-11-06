from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(max_length=255, unique=True, verbose_name=_('Email'))
