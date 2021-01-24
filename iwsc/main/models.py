from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Blog(models.Model):
	opportunity_type =  models.CharField(max_length = 50)
	description = models.TextField()
	eligibility=models.CharField(max_length = 500)
	deadline=models.CharField(max_length = 500)
	def __str__(self):
		return self.opportunity_type

class Contact(models.Model):
	name=models.CharField(max_length=100)
	mail=models.EmailField()
	contact_Number=PhoneNumberField()
	message=models.TextField()

	def __str__(self):
		return self.name


