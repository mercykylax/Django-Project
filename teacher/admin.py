from django.contrib import admin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
	list_display =("registration_numbers","first_name","last_name","profession","email",)
	search_fields =("registration_numbers","first_name","last_name","profession","email",)




admin.site.register(Teacher,TeacherAdmin)


# Register your models here.
