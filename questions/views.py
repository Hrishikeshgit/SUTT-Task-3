from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  get_object_or_404
from .models import Question, Student, Comment
from django.template import loader
from django.urls import reverse
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (	ListView,
								 	DetailView,
								 	CreateView,
								 	UpdateView,
								 	DeleteView)

from users.models import Profile

# Create your views here.
@login_required
def ReportView (request, pk):
	question = get_object_or_404(Question, id = request.POST.get('question_id'))
	reported = False
	if question.report.filter(id = request.user.id).exists():
		question.report.remove(request.user)
		reported = False
	else :
		question.report.add(request.user)
		reported = True
	return HttpResponseRedirect (reverse('detail', args = [ pk]) )

@login_required
def index (request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render (request, 'questions/index.html', context)

@login_required
def details (request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render (request, 'questions/details.html', {'question': question})


class QuestionListView (LoginRequiredMixin, ListView):
	model = Question
	template_name = 'questions/home.html'
	context_object_name = 'questions'
	ordering = ['-pub_date']


class QuestionDetailView (LoginRequiredMixin, DetailView):
	model = Question

	def get_context_data (self, *args, **kwargs):
		context = super (QuestionDetailView, self).get_context_data(*args, **kwargs)
		stuff = get_object_or_404 (Question, id = self.kwargs['pk'])
		total_report = stuff.total_report()

		reported = False
		if stuff.report.filter(id = self.request.user.id).exists():
			reported = True 


		context['total_report'] =  total_report
		context['reported'] =  reported
		

		return context


class QuestionCreateView (LoginRequiredMixin, CreateView):
	model = Question
	fields = ['question_text']

	#To show that the logged in user is the author
	def form_valid(self, form):
		form.instance.op_name = self.request.user
		return super().form_valid(form)


class QuestionUpdateView (LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
	model = Question
	fields = ['question_text']

	#To show that the logged in user is the author
	def form_valid(self, form):
		form.instance.op_name = self.request.user
		return super().form_valid(form)

	def test_func(self):
		questions = self.get_object()
		if self.request.user == questions.op_name:
			return True
		return False

class QuestionDeleteView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Question
	success_url = '/home'
	def test_func(self):
		questions = self.get_object()
		if self.request.user == questions.op_name :
			return True
		return False

@login_required
def home (request):
	context = {
	'questions': Question.objects.all()
	}
	return render (request, 'questions/home.html', context)

@login_required
def about (request):
	return render (request, 'questions/about.html', {'title': 'About'})


@login_required
def question_detail (request, question_id):
	new_comment = None 
	if request.method == 'POST':
		#A comment was posted
		comment_form = CommentForm(data = request.POST)

		if comment_form.is_valid ():
			new_comment = comment_form.save(commit = False)
			new_comment.question = question
			new_comment.save()

		else :
			comment_form = CommentForm

		context = {
		'question' : question,
		'comments' : comments,
		'new_comment': new_comment,
		'comment_form': comment_form
		}
		return render (request, 'questions/comment_detail.html', context)


class AddCommentView (LoginRequiredMixin, CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'questions/add_comment.html'
	success_url = '/home'

	def form_valid(self, form):
		form.instance.question_id = self.kwargs['pk']
		form.instance.op_name = self.request.user
		return super().form_valid(form)

def squestion_detail(request):
	squestions = []
	current_year = request.user.profile.year
	yearmates = Profile.objects.filter(year = current_year)
	questions = Question.objects.all()
	for question in questions:
		if yearmates.username == question.op_name:
			squestions.append(question)
	return render (request, 'questions/squestion_detail.html', context)