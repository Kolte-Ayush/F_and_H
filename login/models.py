

# Create your models here.
from django.db import models
import datetime

class Otp_model(models.Model):

    class Meta:
        db_table='demo'

    Number = models.IntegerField(length=10)
    OTP =models.IntegerField(min_length=1, max_length=6)
    time = models.TimeField(auto_now=True)

