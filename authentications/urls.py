from django.urls import path,include
from . import  views
from .views import ( CompanySignupView,
 PersonSignupView,
 CustomAuthToken, LogoutView)


urlpatterns = [
    path('signup/company/', CompanySignupView.as_view()),
    path('signup/user/', PersonSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),

    
]