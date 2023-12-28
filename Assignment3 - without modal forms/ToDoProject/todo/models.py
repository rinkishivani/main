from django.db import models
from django.db.models import Model
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.
class ToDoList(Model):
    title = models.CharField(max_length=100)
    details = RichTextField()
    date = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)

