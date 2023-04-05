from django.db import models


# Create your models here.

class Task(models.Model):
    """Модель задачи"""

    title = models.CharField(verbose_name='Задача', max_length=255)
    description = models.TextField(verbose_name='Описание', max_length=500)
    status = models.BooleanField(verbose_name='Статус', default=False)
    create_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


