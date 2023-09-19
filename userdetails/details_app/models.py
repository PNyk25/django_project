from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

from django.contrib.auth.models import User
# Create your models here.
class Userdetail(models.Model):
    
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField(validators=[MinValueValidator(20), MaxValueValidator(80)])
    position=models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name+ " , " + str(self.age) +" - "+self.position