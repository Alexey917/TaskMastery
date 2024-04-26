from django.db import models

# Create your models here.
class Projects(models.Model):
  name = models.CharField(max_length=150)


class Profile(models.Model):
  GENDER = [
    ("Пол", "Мужской"),
    ("Пол", "Женский"),
  ]


  image = models.ImageField()
  full_name = models.CharField(max_length=255)
  birthday = models.DateField()
  city = models.CharField(max_length=255)
  gender = models.CharField(max_length=255, choices=GENDER)

