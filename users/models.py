from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GENDER_CHOICES = [('N', 'Мужской'), ('Ж', 'Женский')]

    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    is_active = models.BooleanField(default=False)
    middle_name = models.CharField('отчество', max_length=100, blank=True)
    birth_date = models.DateField('дата рождения', null=True, blank=True)
    gender = models.CharField('пол', max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField('телефон', max_length=20, blank=True)
    address = models.TextField('adress', blank=True)
    photo = models.ImageField(upload_to='studens/', blank=True, null=True)
    student_id = models.CharField('номер студенческого билета', max_length=20, unique=True)
    group =— middle_name (отчество, CharField 100, blank=True)
