
from django.test import TestCase
from .models import Teacher
from teacher.forms import TeacherForm
from django.test import Client
from django.urls import reverse
import datetime
class AddTeacherTestCase(TestCase):
   def setUp(self):
       self.data = {
       "first_name": "Yasmin",
       "last_name": "Abdalla",
       "gender": "Female",
       "email": "yasm@gmail.com",
       "phone_number": "0745677899",
       "profession":"Python",
       "date_joined":datetime.date.today(),
       "registration_numbers":"29876531",
       "work_experience": datetime.date.today(),
       }
       self.bad_data = {
       "first_name": "Yasmin",
       "last_name": "Abdalla",
       "gender": "Female",
       "email": "yasmgmail.com",
       "phone_number": "0745677899",
       "profession":"Python",
       "date_joined":datetime.date.today(),
       "registration_numbers":"29876531",
       "work_experience": datetime.date.today(),
       }

   def test_teacher_form_accepts_valid_data(self):
   		form = TeacherForm(self.data)
   		self.assertTrue(form.is_valid())


   def test_teacher_form_rejects_invalid_data(self):
       form = TeacherForm(self.bad_data)
       self.assertFalse(form.is_valid())

   def test_add_teacher_view(self):
       client = Client() 
       url = reverse("add_teacher")
       response = client.post(url,self.data)
       self.assertEqual(response.status_code,200)

   def test_add_teacher_view_bad_test(self):
       client = Client() 
       url = reverse("add_teacher")
       response = client.post(url,self.bad_data)
       self.assertEqual(response.status_code,400)
           



# Create your tests here.
