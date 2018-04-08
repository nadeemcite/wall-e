from django.db import models
from django.contrib.postgres import fields as pg

# Create your models here.

class Event(models.Model):
    app = models.CharField(max_length=200)
    okind = models.CharField(max_length=200, null=True)
    oid = models.CharField(max_length=200, null=True)
    odata = pg.JSONField(null=True)
    ekind = models.CharField(max_length=200, null=True)
    edata = pg.JSONField(null=True)
    user_id = models.IntegerField(null=True)
    tracker = models.CharField(max_length=200, null=True)
    ip = models.CharField(max_length=200, null=True)
    user_agent = models.CharField(max_length=200, null=True)
    visit_id = models.IntegerField(null=True)