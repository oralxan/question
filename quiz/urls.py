# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.question_list, name='question_list'),
#     path('questions/<int:id>/', views.question_detail, name='question_detail'),
#     path('take/', views.take_quiz, name='take_quiz'),
#     path('result/', views.quiz_result, name='quiz_result'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('quiz/<int:id>/', views.question_detail, name='question_detail'),
    path('quiz/take/', views.take_quiz, name='take_quiz'),
    path('quiz/result/', views.quiz_result, name='quiz_result'),
]
