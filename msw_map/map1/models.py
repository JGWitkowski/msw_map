from django.db import models

class User(models.Model):
	name = models.CharField(max_length = 80)
	message = models.CharField(max_length = 200)
	longtitude = models.DecimalField(max_digits=15, decimal_places=6)
	latitude = models.DecimalField(max_digits=15, decimal_places=6)