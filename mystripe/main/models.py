from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(verbose_name='Название', unique=True, db_index=True, max_length=50)
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.IntegerField(verbose_name='Цена', blank=False, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'itemid': self.pk})
