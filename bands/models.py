from django.db import models
from django.utils.translation import gettext_lazy as _


class Bands(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('band')
        verbose_name_plural = _('bands')
