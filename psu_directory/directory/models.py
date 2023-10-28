import uuid
from django.db import models
from django.utils.safestring import mark_safe 
from PIL import Image as Im

# Create your models here.
class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    discription = models.TextField(max_length=250)
    image = models.ImageField(upload_to='pics/')

def save(self):
    self.save()
    img = Im.open(self.photo.path)

def image_tag(self):                     
        return mark_safe('<img src="/../../media/%s"/>' % (self.photo))