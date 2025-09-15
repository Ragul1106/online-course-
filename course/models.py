from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} ({self.course.title})"


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.module.title}"


class Instructor(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    courses = models.ManyToManyField(Course, related_name="instructors")

    def __str__(self):
        return self.name
