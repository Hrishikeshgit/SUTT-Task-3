from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.core.exceptions import ValidationError


hostel_choices = (	('SR', 'SR'),	('VK', 'VK'), ('Krishna', 'Krishna'), ('Gandhi', 'Gandhi'), ('Ram', 'Ram'),	('Budh', 'Budh'),
	('Malviya', 'Malviya'), ('Bhagirath', 'Bhagirath'),	('Meera', 'Meera'),	)

class UserRegisterForm (UserCreationForm):
	email = forms.EmailField(help_text = "Enter your BITS email")
	hostel = forms.CharField(max_length = 50, widget = forms.Select(choices = hostel_choices))
	student_id = forms.CharField(max_length = 20)
	room = forms.IntegerField()
	mobile = forms.IntegerField()

	class Meta :
		model = User
		fields = ['username', 'email', 'password1', 'password2' ]
		labels = {'mobile': 'Mobile number',
				'student_id': 'Student ID',
				'hostel': 'Hostel',
				'room': 'room',
				}

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise ValidationError("Email already exists")
		return email

	def clean_student_id(self):
		branch_list = ["AA","AB" ,"A1" ,"A2" ,"A3" ,"A4" ,"A5" ,"A7" ,"A8" ,"B1" ,"B2" ,"B3" ,"B4" ,"B5" ]
		student_id = self.cleaned_data['student_id']
		if len(student_id) == 13 and (student_id[4:6] in branch_list) and ((student_id[6:8] == "PS") or (student_id[6:8] in branch_list)):
			return student_id
		else:
			raise ValidationError("Enter valid id")


class UserUpdateForm (forms.ModelForm):
	email = forms.EmailField()

	class Meta :
		model = User 
		fields = ['username', 'email']

class ProfileUpdateForm (forms.ModelForm):
	class Meta :
		model = Profile
		fields = ['student_id' , 'hostel', 'room', 'mobile', 'year', 'first_branch', 'second_branch', 'image']


