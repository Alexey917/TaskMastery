from django.db import models


# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=150)


class Users(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    GENDER = [
        ("Пол", "Мужской"),
        ("Пол", "Женский"),
    ]

    image = models.ImageField(null=True)
    full_name = models.CharField(max_length=255, null=True)
    birthday = models.DateField(null=True)
    city = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, choices=GENDER, null=True)

    def __str__(self):
        return f'{self.name}/{self.full_name}/{self.birthday}/{self.city}/{self.gender}/{self.email}'



