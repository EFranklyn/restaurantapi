from django.db import models


class Chef(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome do Chefe')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Chefe'
        verbose_name_plural = 'Chefes'