from django.test import TestCase
from .models import Student
from student.forms import StudentForm
from django.test import Client
from django.urls import reverse
import datetime




# Create your tests here.


class AddStudentTestCase(TestCase):
	def setUp(self):
			self.data={
			"firstname":"Mercy",
			"lastname":"Nyawira",
			"email":"nyawiramercy49@gmail.com",
			"date_of_birth": datetime.date(2000,6,20),
			"gender" : "female",
			"registration_numbers" : "2019456",
			"phone_number" : "+254725412346",
			"date_joined": datetime.date.today(),
	}

			self.bad_data={
			"firstname":"Mercy",
			"lastname":"Nyawira",
			"date_of_birth": datetime.date(1,2,3),
			"gender" : "female",
			"registration_numbers" : "2019456",
			"email":"123",
			"phone_number" : "+254725412346",
			"date_joined": "datetime.date.today()",
			}	


	def test_student_form_accepts_valid_data(self):
	    form = StudentForm(self.data)
	    self.assertFalse(form.is_valid())

	def test_student_form_rejects_invalid_data(self):
		form = StudentForm(self.bad_data)
		self.assertFalse(form.is_valid())	

	def test_add_student_view(self):
		client = Client() 
		url = reverse("add_student")
		response = client.post(url,self.data)
		self.assertEqual(response.status_code,200)

	def test_add_student_view_bad_test(self):
		client = Client() 
		url = reverse("add_student")
		response = client.post(url,self.bad_data)
		self.assertEqual(response.status_code,400)
		  

class StudentTestCase(TestCase):
	def setUp(self):
	  self.student = Student(
		   first_name = "Mercy",
		   last_name ="Nyawira",
		   date_of_birth = datetime.date(2000,6,20),
		   gender = "female",
		   registration_numbers = "2019456",
		   email = "nyawiramercy49@gmail.com",
		   phone_number = "+254725412346",
		   date_joined = datetime.date.today(),
	)

	def test_full_name_contains_first_name(self):
	  self.assertIn(self.student.first_name,self.student.full_name())

	def test_full_name_contains_last_name(self):
	  self.assertIn(self.student.last_name,self.student.full_name())

	def test_age_is_always_above_17(self):
	  self.assertFalse(self.student.clean() < 17)

	def test_age_is_always_below_30(self):
	  self.assertFalse(self.student.clean() > 30)





	# def test_get_age(self):
	#    self.assertIn(self.student.date_of_birth())

# Create your tests here.
