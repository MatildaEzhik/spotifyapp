from django.urls import path

from user import views

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up_page_name'),
    path('sign-in/', views.sign_in, name='sign_in_page_name'),
    path('profile/', views.profile, name='home_page')
]