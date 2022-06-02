from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Question (models.Model):
	op_name = models.ForeignKey (User, on_delete = models.CASCADE)
	op_id = models.CharField (max_length = 15)
	pub_date = models.DateTimeField (default = timezone.now)
	no_replies = models.IntegerField (default = 0)
	question_text = models.CharField(max_length = 200)
	report = models.ManyToManyField(User, related_name = 'questions')

	def total_report (self):
		return self.report.count()

	def __str__ (self):
		return self.question_text

	def get_absolute_url (self):
		return reverse ('detail', kwargs = {'pk': self.pk})




class Student (models.Model):
	year = models.IntegerField(default = 0)
	student_name = models.CharField (max_length = 50)
	student_id = models.CharField (max_length = 15)
	hostel = models.CharField (max_length = 25)
	room = models.IntegerField(default = 0)
	mobile = models.IntegerField(default = 0)

	def __str__ (self):
		return Student.student_name


class Comment(models.Model):
	question =models.ForeignKey(Question,on_delete=models.CASCADE,related_name='comments')
	name =models.CharField(max_length = 50)
	body =models.TextField()
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'Comment by {}'.format(self.name)
		

#Making a new model secret Question
"""class S_Question(models.Model):
	op_name = models.ForeignKey (User, on_delete = models.CASCADE)
	op_id = models.CharField (max_length = 15)
	pub_date = models.DateTimeField (default = timezone.now)
	no_replies = models.IntegerField (default = 0)
	question_text = models.CharField(max_length = 200)
	report = models.ManyToManyField(User, related_name = 'questions')

	def total_report (self):
		return self.report.count()

	def __str__ (self):
		return self.question_text

	def get_absolute_url (self):
		return reverse ('detail', kwargs = {'pk': self.pk})"""
