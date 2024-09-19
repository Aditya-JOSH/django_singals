from django.urls import path
from . import views

urlpatterns = [
    path('run-test/', views.run_test_view, name='run_test_view'),
    path('create-comment/', views.create_comment_view, name='create_comment_view'),
    path('create-user/', views.create_user_view, name='create_user_view'),

]