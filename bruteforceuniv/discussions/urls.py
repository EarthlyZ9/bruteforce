from django.urls import path
from .views import base_views, question_views, answer_views, vote_views, comment_views

urlpatterns = [
  #base_views
  path('', base_views.question_list, name='question-list'),
  path('<int:question_id>/', base_views.detail, name='detail'),

  #question_views
  path('question/create/', question_views.create_question, name='create-question'),
  path('question/modify/<int:question_id>/', question_views.modify_question, name='modify-question'),
  path('question/delete/<int:question_id>/', question_views.delete_question, name='delete-question'),

  #answer_views
  path('answer/create/<int:question_id>/', answer_views.create_answer, name='create-answer'),
  path('answer/modify/<int:answer_id>/', answer_views.modify_answer, name='modify-answer'),
  path('answer/delete/<int:answer_id>/', answer_views.delete_answer, name='delete-answer'),
  
  #comment_views
  path('comment/create/answer/<int:answer_id>/', comment_views.create_answer_comment, name='create-answer-comment'),
  path('comment/modify/answer/<int:comment_id>/', comment_views.modify_answer_comment, name='modify-answer-comment'),
  path('comment/delete/answer/<int:comment_id>/', comment_views.delete_answer_comment, name='delete-answer-comment'),


  #vote_views
  path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote-answer'),
]