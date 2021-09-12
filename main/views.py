from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.
def main_page(request):
  return render(request, 'main/main.html')

def about_us(request):
  return render(request, 'main/about_us.html')

def course_description(request):
  return render(request, 'main/course_description.html')

@login_required(login_url='accounts:login')
def program_description(request):
  return render(request, 'main/program_description.html')


def instagram(request):
  return redirect("https://instagram.com/bruteforce_univ?utm_medium=copy_link")

def kakao_plus(request):
  return redirect("http://pf.kakao.com/_UsguK")


def custom_404(request, exception=None):
  response = render(request, 'main/custom404.html',status=404)
  return response
