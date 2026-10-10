from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):

    GENDER_CHOICES = [
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
    ]

    EDUCATION_FORM_CHOICES = [
        ('очная', 'Очная'),
        ('заочная', 'Заочная'),
        ('вечерняя', 'Вечерняя'),
    ]

    FUNDING_CHOICES = [
        ('бюджет', 'Бюджет'),
        ('контракт', 'Контракт'),
    ]

    STATUS_CHOICES = [
        ('обучается', 'Обучается'),
        ('академический отпуск', 'Академический отпуск'),
        ('отчислен', 'Отчислен'),
        ('выпускник', 'Выпускник'),
    ]

    COURSE_CHOICES = [
        (1, '1 курс'),
        (2, '2 курс'),
        (3, '3 курс'),
        (4, '4 курс'),
    ]

    middle_name = models.CharField(
        max_length=100, blank=True, verbose_name='Отчество'
    )
    birth_date = models.DateField(
        null=True, blank=True, verbose_name='Дата рождения'
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, verbose_name='Пол'
    )
    phone = models.CharField(
        max_length=20, blank=True, verbose_name='Телефон'
    )
    address = models.TextField(
        blank=True, verbose_name='Адрес'
    )
    photo = models.ImageField(
        upload_to='students/', blank=True, null=True,
        verbose_name='Фотография'
    )
    student_id = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True,
        verbose_name='Номер студенческого билета'
    )
    group = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Учебная группа'
    )
    specialty = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Специальность'
    )
    course = models.PositiveSmallIntegerField(
        choices=COURSE_CHOICES,
        null=True,
        blank=True,
        verbose_name='Курс'
    )
    admission_year = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name='Год поступления'
    )
    education_form = models.CharField(
        max_length=20, choices=EDUCATION_FORM_CHOICES,
        blank=True,
        verbose_name='Форма обучения'
    )
    funding = models.CharField(
        max_length=20, choices=FUNDING_CHOICES,
        blank=True,
        verbose_name='Основа обучения'
    )
    status = models.CharField(
        max_length=30, choices=STATUS_CHOICES, default='обучается',
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления'
    )

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'.strip()

    def __str__(self):
        return f'{self.full_name} — {self.group}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name', 'first_name']