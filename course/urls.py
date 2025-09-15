from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, ModuleViewSet, LessonViewSet, InstructorViewSet

router = DefaultRouter()
router.register("courses", CourseViewSet)
router.register("modules", ModuleViewSet)
router.register("lessons", LessonViewSet)
router.register("instructors", InstructorViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
