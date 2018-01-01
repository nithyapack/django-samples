from django.db import models
from django.utils import timezone

class Feedback(models.Model):
	id = models.IntegerField(primary_key=True)
	stars = models.IntegerField(null=True)
	email = models.EmailField()
	comments = models.TextField(null=True, blank=True)
	created_date = models.DateTimeField(default = timezone.now)
	updated_date = models.DateTimeField(default = timezone.now, null=True)
	
	def __str__(self):
		return self.email
	
