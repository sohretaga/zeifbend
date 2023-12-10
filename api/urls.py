from django.urls import path
from account.views import register_user, user_login, user_logout, leaderboard
from question.views import get_question
from chanel.views import chanels

urlpatterns = [

    #Account API's
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('leaderboards/', leaderboard, name='leaderboards'),

    # Question API's
    path('get-question/', get_question, name='get_question'),

    # Channel API's
    path('chanels/', chanels, name='chanels'),
]