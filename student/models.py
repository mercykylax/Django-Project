from django.db import models

from course.models import Course
import datetime
from django.core.exceptions import ValidationError



# courses = models.ManyToManyField(Course)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    registration_numbers = models.CharField(max_length=20)
    email = models.EmailField(max_length=70)
    phone_number = models.CharField(max_length=20)
    date_joined = models.DateField()
    image = models.ImageField(upload_to="profile_image",blank=True)
    course=models.ManyTo ManyField(Course,null=True,blank=true,related_name="students")
    # def __str__(self):
    #     return self.first_name

    def full_name(self):
       return "{} {}".format(self.first_name,self.last_name)

    def get_age(self):
      today = datetime.date.today()
      return today.year - self.date_of_birth.year

    age = property(get_age)
    def clean(self):
      age = self.age
      if age <17 or age >30:
        raise ValidationError("You are not authorized")
      return age

    





# Create your models here.
