from django.db import models

# Create your models here.

# for sorting of individual objects
class String_Object(models.Model):
    string_value = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

# for bulk sorting
class Integer_Object(models.Model):
    int_value = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

# for saving of big data
class Bytes_Object(models.Model):
    bytes_value = models.BinaryField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)