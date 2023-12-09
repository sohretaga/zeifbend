from django.urls import path
from account.views import register_user, user_login, user_logout
from question.views import get_question

urlpatterns = [

    #Account API's
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    # Question API's
    path('get-question/', get_question, name='get_question')
]