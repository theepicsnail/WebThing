from django.db import models

class Agent(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    def __unicode__(self):
        return self.username

class Computer(models.Model):
    speed    = models.IntegerField()
    owner    = models.ForeignKey(Agent)
    def __unicode__(self):
        return unicode(self.owner)+"-"+speed

# Create your models here.
