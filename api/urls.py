from django.urls import path,include
from .views import StudentViewSet
from .views import TeacherViewSet
from .views import CourseViewSet
from rest_framework import routers


router=routers.DefaultRouter()
router.register("students",StudentViewSet)
router.register("teacher",TeacherViewSet)
router.register("course",CourseViewSet)
urlpatterns=[
path("",include(router.urls)),]