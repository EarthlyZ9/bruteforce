from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from accounts.models import Account_Info
from django.db.models import Q
from django.core.paginator import Paginator
from ..forms import StudyGroupAssignForm, ProgressPointsFileForm
from ..models import StudyGroupAssign, Progress
import csv

# Create your views here.
@staff_member_required
def admin_page(request):
  
  if request.method == 'POST' and 'study_group' in request.POST: #스터디 그룹 배정
    group_assign_form = StudyGroupAssignForm(request.POST, request.FILES)
    print(request.FILES.get('file'))

    csv_file = request.FILES['file']
    decoded_file = csv_file.read().decode('utf-8').splitlines()

    #csv parcing
    read_file = csv.DictReader(decoded_file)
    for row in read_file:
      username = row['userid']
      group = int(row['group'])
      print(group)
      user = Account_Info.objects.filter(username=username).first()
      user.group = group
      user.save()

    if group_assign_form.is_valid():
      print('in')
      group_assign_form.save()
      return redirect('admin-page:admin-main')
    else:
      print(group_assign_form.errors)

  elif request.method == 'POST' and 'apply_progress' in request.POST: #스터디 그룹 배정
    progress_points_form = ProgressPointsFileForm(request.POST, request.FILES)
    print(request.FILES.get('progress_csv_file'))

    period = request.POST.get('period')
    csv_file = request.FILES['progress_csv_file']
    decoded_file = csv_file.read().decode('utf-8').splitlines()

    #csv parcing
    read_file = csv.DictReader(decoded_file)
    
    
    for row in read_file:
      username = row['userid']
      points = int(row['points'])
      print(username, points)
      user = Progress.objects.filter(user__username=username).first()
      if period == '1':
        user.progress1 = points
        user.save()
      elif period == '2':
        user.progress2 = points
        user.save()
      elif period == '3':
        user.progress3 = points
        user.save()
      elif period == 'final':
        user.progress4 = points
        user.save()

    if progress_points_form.is_valid():
      print('in')
      progress_points_form.save()
      return redirect('admin-page:admin-main')
    else:
      print(progress_points_form.errors)

    #
  else: # POST
    return render(request, 'adminpage/admin_page.html')

@staff_member_required
def user_info(request):
  #Get으로 페이지 가져옴 디폴트값은 1
  page = request.GET.get('page','1')
  #검색어 가져옴
  kw = request.GET.get('kw','')
  #정렬기준 가져옴
  course = request.GET.get('course','all')


  #생성날짜 순으로 정렬해서 모델에서 가져옴
  user_list = Account_Info.objects.order_by('name')

  # 정렬
  if course == 'python':
      user_list = Account_Info.objects.filter(course='python')
  elif course == 'datascience':
      user_list = Account_Info.objects.filter(course='datascience')
  elif course == 'htmlcss':
      user_list = Account_Info.objects.filter(course='htmlcss')
  else:  # all
      user_list = Account_Info.objects.order_by('name')

  #들어온 검색어로 검색.
  if kw:
    #제목, 내용 , 글쓴이, 답변이
    #filter함수에서는 모델속서에 접근하기위해 언더바두개씀
    user_list = user_list.filter(
        Q(username__icontains=kw) |
        Q(name__icontains=kw) |
        Q(course__icontains=kw) |
        Q(individual__icontains=kw) |
        Q(mobile_num__icontains=kw)  |
        Q(recommender__icontains=kw) |
        Q(bank_account__icontains=kw) |
        Q(bank_name__icontains=kw)  |
        Q(date_of_birth__icontains=kw)  |
        Q(individual__icontains=kw)
    ).distinct() #

  #페이지처리
  paginator = Paginator(user_list, 20)
  page_obj = paginator.get_page(page)

  context = {'user_list': page_obj,'page':page,'kw':kw,'course':course}
  #데이터를 템플릿에 적용하여 HTML로 변환
  return render(request, 'adminpage/user_info.html', context)

@staff_member_required
def weekly_studies(request):
  #Get으로 페이지 가져옴 디폴트값은 1
  page = request.GET.get('page','1')
  #검색어 가져옴
  kw = request.GET.get('kw','')
  #정렬기준 가져옴
  course = request.GET.get('course','all')


  #생성날짜 순으로 정렬해서 모델에서 가져옴
  user_reverse = Account_Info.objects.order_by('name')

  # 정렬
  if course == 'python':
      user_reverse = Account_Info.objects.filter(course='python')
  elif course == 'datascience':
      user_reverse = Account_Info.objects.filter(course='datascience')
  elif course == 'htmlcss':
      user_reverse = Account_Info.objects.filter(course='htmlcss')
  else:  # all
      user_reverse = Account_Info.objects.order_by('name')

  #들어온 검색어로 검색.
  if kw:
    #검색 내용
    #filter함수에서는 모델속서에 접근하기위해 언더바두개씀
    user_reverse = user_reverse.filter(
        Q(username__icontains=kw) |
        Q(name__icontains=kw)
    ).distinct() 

  #페이지처리
  paginator = Paginator(user_reverse, 20)
  page_obj = paginator.get_page(page)

  context = {'user_reverse': page_obj, 'page':page,'kw':kw,'course':course}
  #데이터를 템플릿에 적용하여 HTML로 변환
  return render(request, 'adminpage/weekly_studies_status.html', context)