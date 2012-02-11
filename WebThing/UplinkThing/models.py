from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):
    user = models.OneToOneField(User)
    money = models.IntegerField()
    def __unicode__(self):
        return "Agent:"+self.user.username

class Software(models.Model):
    version = models.IntegerField()
    name    = models.CharField(max_length=64)
    cost    = models.IntegerField()

class Computer(models.Model):
    speed    = models.IntegerField()
    owner    = models.ForeignKey(Agent)
    software = models.ForeignKey(Software)
    def __unicode__(self):
        return unicode(self.owner)+"-"+speed


    
# Create your models here.
