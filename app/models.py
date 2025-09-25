from django.db import models

class Event(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=55, null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    password=models.CharField(max_length=55)
    location=models.TextField()
    time= models.TimeField(null=True, blank=True)
    date=models.DateField(null=True, blank=True)
    image=models.ImageField(upload_to="image/", null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    phone= models.CharField(null=True, blank=True, max_length=11)

    class meta:
        ordering: ["created_at"]
# Create your models here.
