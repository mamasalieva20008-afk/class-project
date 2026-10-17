
from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название факультета')
    short_name = models.CharField(max_length=30, unique=True, verbose_name='Сокращение')
    dean = models.CharField(max_length=200, verbose_name='Декан')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'
        ordering = ['name']


class Direction(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name='Код направления')
    name = models.CharField(max_length=200, verbose_name='Название направления')
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.PROTECT,
        related_name='directions',
        verbose_name='Факультет',
    )
    study_duration = models.PositiveSmallIntegerField(
        verbose_name='Срок обучения (лет)'
    )

    def __str__(self):
        return f'{self.code} — {self.name}'

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'
        ordering = ['name']


class Group(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название группы')
    direction = models.ForeignKey(
        Direction,
        on_delete=models.PROTECT,
        related_name='groups',
        verbose_name='Направление',
    )
    admission_year = models.PositiveSmallIntegerField(verbose_name='Год набора')
    is_active = models.BooleanField(default=True, verbose_name='Активная группа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'
        ordering = ['name']
