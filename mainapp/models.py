from django.db import models
from django.contrib.auth.models import User
from datetime import datetime    
# Create your models here.
class addapartment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appname = models.CharField(max_length=800)
    owner = models.CharField(max_length=800)
    renter =  models.CharField(max_length=800, default='1')
    OPhone =  models.CharField(max_length=800,default='1')
    RPhone =  models.CharField(max_length=800,default='1')
    share = models.PositiveIntegerField(default='1')
    stno = models.PositiveIntegerField(default='2')
    startdate = models.DateField(default=datetime.now(), blank=True)
    expiredate = models.DateField(default=datetime.now(), blank=True)
    image = models.FileField(upload_to ='image/',null=True)
    def __str__(self):
             return "%s" % (self.id)