from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    subject = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category,
                                            on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.subject






