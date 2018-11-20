# coding=utf-8

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.validators import RegexValidator

# Aqui tambem introduzimos o django translation os texto estão todos dentro de uma função ugettext_lazy
class Client(models.Model):

    fantasy_name = models.CharField(_('Fantasy Name'), max_length=100)
    social_name = models.CharField(_('Social Name'), max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
				     message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
				    )
    phone_number = models.CharField(validators=[phone_regex],
				    max_length=17,
				    blank=True) # validators should be a list


    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

