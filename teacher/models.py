from django.db import models

class Teacher(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	profession = models.CharField(max_length=70) 
	gender = models.CharField(max_length=20)
	registration_numbers = models.CharField(max_length=20)
	email = models.EmailField(max_length=70)
	phone_number = models.CharField(max_length=20)
	date_joined = models.DateField()
	work_experience = models.DateField()


	def __str__(self):
		return self.first_name



# Create your models here.
