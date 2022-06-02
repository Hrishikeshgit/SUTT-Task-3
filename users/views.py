from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.core.exceptions import ValidationError
from .methods import getBranch, firstBranch, secondBranch, obtain_year


def update_user_data (user):
	Profile.objects.update_or_create(user = user, defaults = {'mobile' : user.profile.mobile })

# Create your views here.
def register(request):
	rollno = []
	if request.method == 'POST':

		profile_form = ProfileUpdateForm(request.POST)
		form = UserRegisterForm(request.POST)

		if form.is_valid ():
			user = form.save()
			user.refresh_from_db()
			
			username = form.cleaned_data.get('username')
			user.profile.mobile = form.cleaned_data.get('mobile')
			user.profile.hostel = form.cleaned_data.get('hostel')
			user.profile.room = form.cleaned_data.get('room')
			user.profile.student_id = form.cleaned_data.get('student_id')

			#Getting the rest of info from student id
			rollno = form.cleaned_data.get('student_id')
			year  = obtain_year (rollno)
			user.profile.year = year
			first_branch = firstBranch(rollno)
			user.profile.first_branch = first_branch
			second_branch = secondBranch(rollno)
			user.profile.secondBranch = second_branch


			update_user_data (user)
			user.save()
			messages.success(request, f'Account created for {username} !')
			return redirect('login')
		else :
			print(form.errors)
	else :
		form = UserRegisterForm()
		profile_form = ProfileUpdateForm()
	context = {'form': form, 'profile_form': profile_form}
	return render (request, 'users/register.html' , context )

@login_required
def profile (request):
	if request.method == 'POST':
		#Used to store data that is given 
		u_form = UserUpdateForm(request.POST, instance = request.user)
		p_form = ProfileUpdateForm( request.POST,
								 	request.FILES,
									instance = request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated !')
			return redirect('profile')
		else: 
			print(u_form.errors)
			print(p_form.errors)

	else :
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.profile)
		
	context = {
		'u_form': u_form,
		'p_form': p_form,
	}
	return render(request, 'users/profile.html', context)


@login_required
def branch_view (request):
	branch_list = ["AA","AB" ,"A1" ,"A2" ,"A3" ,"A4" ,"A5" ,"A7" ,"A8" ,"B1" ,"B2" ,"B3" ,"B4" ,"B5" ]
	current_branch = request.user.profile.first_branch
	people = Profile.objects.filter(first_branch = current_branch).order_by('year')
	context = {
	'people':people,
	'current_branch':current_branch,
	}
	print(people)
	return render(request, 'users/branch.html', context)

