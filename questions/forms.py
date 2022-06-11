from django import forms
from .models import Comment, SQuestion

class CommentForm (forms.ModelForm):
	class Meta :
		#Make comment user as user
		model = Comment
		fields = ['name', 'body']
		widgets = {
		'name': forms.TextInput(attrs={'class': 'form-control'}),
		'dody': forms.Textarea(attrs={'class': 'form-control'})
		}

class SQuestionForm(forms.ModelForm):
	class Meta :
		model = SQuestion
		fields = ['question_text']
		widgets = {
		'question_text': forms.TextInput(attrs={'class': 'form-control'}),
		}