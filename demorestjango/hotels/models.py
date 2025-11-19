from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4)

    class Meta:
        abstract = True


class Todo(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_done = models.BooleanField(default=False)

    def __repr__(self):
        return f"Title : {self.title}, discription : {self.description}"

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    thumbnail = models.URLField(null=True, blank=True,default="https://cdn.vectorstock.com/i/1000v/11/95/flat-style-of-hotel-vector-12421195.jpg")
    rating = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )

    location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    photos = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.location}"