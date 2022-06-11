from django.urls import path
from . import views
from .views import (QuestionListView,
 					QuestionDetailView,
 					QuestionCreateView,
 					QuestionUpdateView,
 					QuestionDeleteView,
 					AddCommentView,
 					ReportView,
 					AddSQuestionView)

urlpatterns = [
	path ('', QuestionListView.as_view(), name ='home'),
	path ('questions/<int:pk>/', QuestionDetailView.as_view(), name ='detail'),
	path ('questions/<int:pk>/update/', QuestionUpdateView.as_view(), name ='update'),
	path ('questions/<int:pk>/delete/', QuestionDeleteView.as_view(), name ='delete'),
	path ('questions/new/', QuestionCreateView.as_view(), name ='create'),
	path ('questions/<int:pk>/add_comment/', AddCommentView.as_view(), name ='add_comment'),
	#path ('s_questions/<int:pk>/', QuestionDetailView.as_view(), name ='s_detail'),
	#path ('s_questions/<int:pk>/update/', QuestionUpdateView.as_view(), name ='s_update'),
	#path ('s_questions/<int:pk>/delete/', QuestionDeleteView.as_view(), name ='s_delete'),
	#path ('s_questions/new/', QuestionCreateView.as_view(), name ='s_create'),
	#path ('s_questions/<int:pk>/add_comment/', AddCommentView.as_view(), name ='s_add_comment'),
	path ('about/', views.about, name = 'about'),
	path ('report/<int:pk>/', ReportView, name = 'report_question'),
	]