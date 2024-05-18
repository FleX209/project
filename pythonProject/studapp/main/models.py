from django.db import models
from django.contrib.auth.models import AbstractUser


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    author = models.CharField('ФИО', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class CustomUser(AbstractUser):
    pass
