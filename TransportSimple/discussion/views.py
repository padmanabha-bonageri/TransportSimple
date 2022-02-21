from django.shortcuts import render, reverse, get_object_or_404
from .models import Question, Comment
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class QuestionListView(LoginRequiredMixin,ListView):
	model = Question
	context_object_name = 'objects'


class QuestionDetailView(DetailView):
	model = Question


class QuestionCreateView(CreateView):
	model = Question
	fields = ['question']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)	


class AnswerAddView(CreateView):
	model = Comment
	template_name = 'discussion/add_answer.html'
	fields = ['answer']

	def form_valid(self, form):
		print(dir(self.request))
		form.instance.question_id = self.kwargs['pk']
		form.instance.author = self.request.user
		return super().form_valid(form)


def LikeView(request, pk):
	comment = get_object_or_404(Comment, id=request.POST.get('answer_id'))
	comment.likes.add(request.user)
	return HttpResponseRedirect(reverse('home'))


	