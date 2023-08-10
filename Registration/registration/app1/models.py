from django.db import models
from django.contrib.auth.models import User
import datetime

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return '{0}/{1}'.format("create_user",filename)

class Department(models.Model):
    name = models.CharField(max_length=100)
    # Other fields and methods

class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # Other fields and methods

class Batch(models.Model):
    YEAR_CHOICES = [(r, r) for r in range(2020, datetime.date.today().year + 1)]
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Other fields and methods
    
class Class(models.Model):
    name = models.CharField(max_length=100)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    # Other fields and methods

class Section(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    # Other fields and methods

    def __str__(self):
        return self.name

class UserDetails(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_details')
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    phoneno = models.CharField(max_length=10)
    role = models.CharField(max_length=20)
    createdon = models.DateTimeField(auto_now_add=True)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_user_details')

    class Meta:
        db_table = 'UserDetails'
