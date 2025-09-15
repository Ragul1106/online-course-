from rest_framework import serializers
from .models import Course, Module, Lesson, Instructor


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "title", "content", "module"]


class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    lessons = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="lesson-detail"
    )

    class Meta:
        model = Module
        fields = ["id", "title", "course", "lessons"]


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "title", "description", "modules"]


class InstructorSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Instructor
        fields = ["id", "name", "bio", "courses"]
