from django.db import models

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField(unique=True)
    stu_name = models.CharField(max_length=200)
    vote1 = models.IntegerField(blank=True, null=True)
    vote2 = models.IntegerField(blank=True, null=True)
    vote3 = models.IntegerField(blank=True, null=True)
    vote4 = models.IntegerField(blank=True, null=True)
    vote5 = models.IntegerField(blank=True, null=True)
    vote6 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.stu_name

class Candidate(models.Model):
    canid = models.IntegerField(unique=True)
    can_name = models.CharField(max_length=200)
    can_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.can_name
