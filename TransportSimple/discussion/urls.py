from django.urls import path
from . import views
from .views import QuestionListView, QuestionDetailView, QuestionCreateView, AnswerAddView, LikeView

urlpatterns = [
	path('', QuestionListView.as_view(), name='home'),
	path('ask/<int:pk>/', QuestionDetailView.as_view(), name='detail'),
	path('ask/new/', QuestionCreateView.as_view(), name='create'),
	path('ask/<int:pk>/answer', AnswerAddView.as_view(), name='answer'),
	path('like/<int:pk>/', LikeView, name='like'),

]