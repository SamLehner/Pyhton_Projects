from django.db import models

from django.db import models


class ClassManager(models.Manager):
    def create_class(self, title, course_number, instructor_name, duration):
        classInstance = self.create(title=title)
        return classInstance


class DjangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(max_length=6, default=0, blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True)
    duration = models.FloatField(max_length=6, default=01.00, blank=True)

    objects = ClassManager()


class1 = DjangoClasses.objects.create_class("Coding 101", 1, "Jessica Smith", 01.30)
class2 = DjangoClasses.objects.create_class("Django Fundamentals", 2, "Rob Davos", 02.00)
class3 = DjangoClasses.objects.create_class("Python Basics", 3, "Billy Jean", 00.45)


