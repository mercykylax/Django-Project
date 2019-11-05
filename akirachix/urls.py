

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("student/",include("student.urls")),
    path("teacher/",include("teacher.urls")),
    path("course/",include("course.urls")),
    path("api/",include("api.urls")),
    path("",include("core.urls")),
    path("accounts/",include("registration.backends.default.urls")),


    

]
