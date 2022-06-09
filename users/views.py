from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from django.http import HttpResponse

# def home(request):
#     return HttpResponse(" <h1> home page </h1>")
# def loginpage(request):
#     return HttpResponse("login page")
# def registration (request):
#     return HttpResponse("registration ")
class Home_View(View):
    def get(self,request):
        return render(request,"home.html")
class Login_page(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        print(request.POST.get("log_name"))
        print(request.POST.get("log_pass"))
        return render(request,"login.html")

class Registration_Page(View):
    def get(self,request):
        return render(request,"registration.html")
    def post(self,request):
        print(request.POST.get("r_name"))
        print(request.POST.get("r_pass"))
        print(request.POST.get("r_mail"))
        return render(request, "registration.html")
