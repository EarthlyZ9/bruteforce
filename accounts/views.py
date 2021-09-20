from points.models import PurchaseRequest
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts.forms import UpdateInfoForm, UserForm, ResetPasswordForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import FindIdForm, PasswordChangeCustomForm
from django.contrib.auth import update_session_auth_hash
from adminpage.models import PointsStatus
from accounts.models import Account_Info
import datetime
from activities.models import Week
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import string
import random


# Create your views here.
@login_required(login_url='accounts:login')
def profile(request):
  #1주차부터 12주차 계산해서 보여주기

  #주차 표시
  date_now = datetime.datetime.now()
  user_info = request.user
  week_num = Week.objects.filter(season=user_info.season, start_date__lte=date_now, end_date__gte=date_now).first().week_num

  if PointsStatus.objects.filter(user=request.user).first():
    print(PointsStatus.objects.filter(user=request.user).first())
    user_points_status = PointsStatus.objects.filter(user=request.user).first()
    available_points = user_points_status.total_points - user_points_status.used_points
    total_points = user_points_status.total_points 
  else:
    available_points = 0
    total_points = 0

  return render(request, 'accounts/profile.html', {'user_info': user_info, 'week_num':week_num, 'total_points':total_points, 'available_points':available_points})

@login_required(login_url='accounts:login')
def update_user_info(request):
  if request.method == "POST":
    form = UpdateInfoForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('accounts:profile')

  else: 
    form = UpdateInfoForm(instance=request.user)

    context=dict()
    context['user_info']=request.user
    context['form']= form
    return render(request, 'accounts/update_user_info.html', context=context)


def check_login(request):
  username = request.POST.get('username')
  password = request.POST.get('password')

  user = authenticate(username=username, password=password)
  valid = user is not None
  if valid:
    login(request, user)
  
  return JsonResponse({'result':valid})

def signup(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('accounts:login')
  else:
    form = UserForm()
  
  return render(request, 'accounts/signup.html', {'form':form, 'anchor':'name'})

def username_availability(request):
  username = request.POST.get('username')
  exist = Account_Info.objects.filter(username=username).exists()

  return JsonResponse({'result':exist})

@login_required(login_url='accounts:login')
def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeCustomForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'accounts/password_update_complete.html')
    else:
        form = PasswordChangeCustomForm(user=request.user)

    context = {'form': form, }
    return render(request, 'accounts/update_password.html', context)

@login_required(login_url='accounts:login')
def purchase_records(request):
  user = Account_Info.objects.filter(username=request.user).first()
  purchase_records = PurchaseRequest.objects.filter(user=user)
  #총 사용 포인트 계산
  user_points_status = PointsStatus.objects.filter(user=user).first()


  return render(request, 'accounts/purchase_records.html', {'purchase_records':purchase_records, 'user_points_status':user_points_status})

def find_id(request):
  if request.method == 'POST':
    form = FindIdForm(request.POST)
    user_name = request.POST.get('name')
    user_mobile_num = request.POST.get('mobile_num')
    user_email = request.POST.get('email')
    if form.is_valid():
      if Account_Info.objects.filter(name=user_name): #등록된 사용자 이름이면!
        user_info = Account_Info.objects.filter(name=user_name).first()
        if user_info.mobile_num == user_mobile_num and user_info.email == user_email: #등록된 이름의 휴대폰 번호와 이메일이 일치하면
          user_id = user_info.username
          return render(request, 'accounts/find_id_complete.html', {'name':user_name, 'user_id':user_id})
        elif user_info.mobile_num == user_mobile_num and user_info.email != user_email:
          messages.error(request, '사용자 이메일이 일치하지 않네요 :(')
        elif user_info.mobile_num != user_mobile_num and user_info.email == user_email:
          messages.error(request, '사용자 휴대폰 번호가 일치하지 않네요 :(')
        else:
          messages.error(request, '사용자 휴대폰 번호와 이메일이 일치하지 않네요 :(')
      else:
        messages.error(request, '등록되지 않은 사용자입니다.')

    else:
      print(form.errors)
  else: #get method
    form = FindIdForm()
    
  context = {'form': form, }
  return render(request, 'accounts/find_id_form.html', context)



def reset_password(request):
  if request.method == 'POST':
    form = ResetPasswordForm(request.POST)
    user_email = request.POST.get('email')
    if form.is_valid(): #valid 시 랜덤 문자열 생성, 그걸로 비번 바꾸기, 이메일 보내기
      print(user_email)
      print(Account_Info.objects.filter(email=user_email))
      if Account_Info.objects.filter(email=user_email): #등록된 이메일이면!
        print('email exist')
        #랜덤 문자열 생성
        LENGTH = 8
        string_pool = string.ascii_letters + string.digits
        random_string = ""
        for i in range(LENGTH):
          random_string += random.choice(string_pool)
        
        #비밀번호 변경하기 (random_string)
        user = Account_Info.objects.filter(email=user_email).first()
        user.set_password(random_string)
        user.save()

        #이메일 전송
        subject = '[Brute Force] 임시 비밀번호를 확인해주세요.'
        message = random_string
        html_message = render_to_string('./accounts/email_template.html', {'temporary_password':random_string})
        
        send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=[user_email], html_message=html_message)
        return render(request, 'accounts/password_reset_complete.html')
      else: #등록된 이메일이 아니면!
        messages.error(request, "가입되지 않은 이메일입니다. 이메일을 다시 확인해주세요.")
        print(messages.error)
    else:
      print(form.errors)

  else:
    form = ResetPasswordForm()

  context = {'form': form, }
  return render(request, 'accounts/reset_password_form.html', context)


def my_study_group(request):
  return render(request, 'accounts/my_study_group.html')