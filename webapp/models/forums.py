from django.db import models
from django.urls import reverse

from webapp.models import BaseCreateUpdateModel


class Forum(BaseCreateUpdateModel):
    title = models.CharField(max_length=50,  verbose_name='Название', null=False, blank=False)
    description = models.TextField(verbose_name='Содержимое', null=False, blank=False)

    class Meta:
        db_table = 'Forum'
        verbose_name = 'Форум'
        verbose_name_plural = "Форумы"

    def get_absolute_url(self):
        return reverse('webapp:index')