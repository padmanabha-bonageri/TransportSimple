from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Question(models.Model):
	question = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.question

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk':self.pk})


class Comment(models.Model):
	question = models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE)
	answer = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name='comments_like')

	def __str__(self):
		return self.answer

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk':self.question.pk})