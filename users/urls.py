from django.urls import path
from users import views
urlpatterns=[
    path("home",views.Home_View.as_view()),
    path("login",views.Login_page.as_view()),
    path("reg",views.Registration_Page.as_view())
#     path("home",views.home),
#     path("login",views.loginpage),
#     path("registration",views.registration)
]



