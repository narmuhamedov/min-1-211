from django.db import models
from django.contrib.auth.models import User

GENDER_TYPE = (
    ('М', 'М'),
    ('Ж', "Ж"),
    ('Не определился', "Не определился")
)

class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    phone_number = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100, choices=GENDER_TYPE)
