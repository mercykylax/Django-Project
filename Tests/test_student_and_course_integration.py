from django test import  TestCase
from student .models import Student
from course .models import Course
import datetime




Class StudentCourseTestCase(TestCase):
	def setup(self):
		self.student_a=Student.objects.create{
			"firstname":"Mercy",
			"lastname":"Nyawira",
			"email":"nyawiramercy49@gmail.com",
			"date_of_birth": datetime.date(2000,6,20),
			"gender" : "female",
			"registration_numbers" : "2019456",
			"phone_number" : "+254725412346",
			"date_joined": datetime.date.today(),
			}
		self.student b=Student.objects.create{
			"firstname":"Kyla",
			"lastname":"Wambui",
			"date_of_birth": datetime.date(1,2,3),
			"gender" : "female",
			"registration_numbers" : "205656",
			"email":"kyla@gmail.com",
			"phone_number" : "+254725412346",
			"date_joined": "datetime.date.today()",

			}
			self.python=Course.ojects.create{
			"duration_in_months":5,
			"start_date":datetime.date.today(),
			"end_date":datetime.date.today(),
			"description":"A backened coding language",

			}

			self.javascript=Course.objects.create{
			"duration_in_months":8,
			"start_date":datetime.date.today(),
			"end_date":datetime.date.today(),
			"description":"A language for both frontend and backened",


			}
			self.design=Course.objects.create{
			"duration_in_months":18,
			"start_date":datetime.date.today(),
			"end_date":datetime.date.today(),
			"description":"Adobe softwares are used in design",


			}
	def test_student_can_join_a_course(self):
		self.student_a. courses add(self.python)
		self.assertEqual(self.student_a.courses.count(),1)
		self.student_a.courses.add(self.javascript)
		self.assertEqual (self.student_a.course.count)


	def test_student_can_join_many_courses(self):
	    self.student_b courses.add(self.python,self.javascript,self.design
	    self.assertEqual(self.student_b.courses.count(),3)
	    	)

    def test_course_can_be_trained_by_a_teacher(self):
        self.python.teacher = self.teacher_a
        self.assertEqual(self.python.teacher, self.teacher_a)
        
   def test_many_courses_can_be_trained_by_one_trainer(self):
        self.python.teacher = self.teacher_b
        self.java.teacher = self.teacher_b
        self.assertEqual(self.java.teacher,self.python.teacher)




