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
    duration = models.FloatField(default=01.00, blank=True)

    objects = models.Manager()


