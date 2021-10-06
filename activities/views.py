from typing import ValuesView
from django.http.response import HttpResponse
import json
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models  import Material, Week, WeeklyStudies, HtmlFruits
from adminpage.models import PointsStatus, Progress, WeeklyActivityPoints
from accounts.models import Account_Info
import datetime
from .forms import WeeklyStudiesForm
from django.http import JsonResponse
from django.utils import timezone
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from django.views.generic import View


# Create your views here.
def rankings(request):
  user = request.user
  date_now = datetime.datetime.now()
  week = Week.objects.filter(season=user.season, start_date__lte=date_now, end_date__gt=date_now).first()

  python_top_ten = PointsStatus.objects.filter(user__course = 'python').order_by('total_points')[:10]
  ds_top_ten = PointsStatus.objects.filter(user__course = 'datascience').order_by('total_points')[:10]
  htmlcss_top_ten = PointsStatus.objects.filter(user__course = 'htmlcss').order_by('total_points')[:10]

  return render(request, 'activities/rankings.html', {'python_top_ten':python_top_ten, 'ds_top_ten':ds_top_ten, 'htmlcss_top_ten':htmlcss_top_ten, 'week':week})

@login_required(login_url='accounts:login')
def study_log(request):
  user = request.user
  submit_records = WeeklyStudies.objects.filter(user=user).order_by('week')
  weekly_records = WeeklyActivityPoints.objects.filter(user=user).order_by('week_num')
  progress = Progress.objects.filter(user=user).first()
  #progress = Progress.objects.filter(user=user).order_by('')
  return render(request, 'activities/study_log.html', {'submit_records':submit_records, 'progress':progress, 'weekly_records':weekly_records})


def htmlcss_fruits(request):
  #Get으로 페이지 가져옴 디폴트값은 1
  page = request.GET.get('page','1')
  #검색어 가져옴
  kw = request.GET.get('kw','')
  #정렬기준 가져옴
  topic = request.GET.get('topic','all')


  #생성날짜 순으로 정렬해서 모델에서 가져옴
  html_fruits = HtmlFruits.objects.order_by('create_date')

  # 정렬
  if topic == 'semi1':
      html_fruits = HtmlFruits.objects.filter(topic='semi1')
  elif topic == 'semi2':
      html_fruits = HtmlFruits.objects.filter(topic='semi2')
  elif topic == 'semi3':
      html_fruits = HtmlFruits.objects.filter(topic='semi3')
  elif topic == 'final':
      html_fruits = HtmlFruits.objects.filter(topic='final')
  else:  # all
      html_fruits = HtmlFruits.objects.order_by('create_date')

  #들어온 검색어로 검색.
  if kw:
      #제목, 내용 , 글쓴이, 답변이
      #filter함수에서는 모델속서에 접근하기위해 언더바두개씀
      html_fruits = html_fruits.filter(
          Q(user__icontains=kw) |
          Q(topic__icontains=kw)
      ).distinct()

  #페이지처리
  paginator = Paginator(html_fruits, 10)
  page_obj = paginator.get_page(page)

  context = {'html_fruits': page_obj,'page':page,'kw':kw,'topic':topic}
  #데이터를 템플릿에 적용하여 HTML로 변환
  return render(request, 'activities/html_fruits.html', context)


#자바스크립트에서 온 요청 처리, 피드백 보여주기 rightdiv
def load_feedbacks(request):
  author = request.GET.get('author')
  topic = request.GET.get('topic')
  #user_feedbacks = Feedbacks.objects.filter(feedback_to__author_id=author, feeback_to__topic=topic)
  fruit = HtmlFruits.objects.filter(author__username=author, topic=topic).first()
  
  return render(request, 'activities/feedbacks.html', {'fruit': fruit})

#피드백 등록
@login_required(login_url='accounts:login')
def create_feedback(request, fruit_id):
  fruit = get_object_or_404(HtmlFruits, id=fruit_id)
  fruit.feedbacks_set.create(author=request.user, content=request.POST.get('content'), create_date=timezone.now())
  return render(request, 'activities/feedbacks.html', {'fruit': fruit})

#칭찬하기
@login_required(login_url='accounts:login')
def vote_fruit(request, fruit_id):
  user = request.user
  fruit = get_object_or_404(HtmlFruits, id=fruit_id)
  if user == fruit.author:
    message ='본인이 작성한 글은 추천할 수 없어요 :('
  elif fruit.voter.filter(id = user.id):
    message ='이미 칭찬하셨네요!'
  else:
      fruit.voter.add(request.user)
      message = '칭찬하셨습니다!'
  
  ret = {
    'message': message,
    'counts': fruit.voter.count(),
  }
  
  return HttpResponse(json.dumps(ret), content_type="application/json")


@login_required(login_url='accounts:login')
def material_list(request):
    #Get으로 페이지 가져옴 디폴트값은 1
    page = request.GET.get('page','1')
    #검색어 가져옴
    kw = request.GET.get('kw','')
    #정렬기준 가져옴
    category = request.GET.get('category','all')


    #생성날짜 순으로 정렬해서 모델에서 가져옴
    material_list = Material.objects.order_by('num')

    # 정렬
    if category == 'python':
        material_list = Material.objects.filter(category='python')
    elif category == 'datascience':
        material_list = Material.objects.filter(category='datascience')
    elif category == 'htmlcss':
        material_list = Material.objects.filter(category='htmlcss')
    elif category == 'common':
        material_list = Material.objects.filter(category='common')
    else:  # all
        material_list = Material.objects.order_by('-num')

    #들어온 검색어로 검색.
    if kw:
        #제목, 내용 , 글쓴이, 답변이
        #filter함수에서는 모델속서에 접근하기위해 언더바두개씀
        material_list = material_list.filter(
            Q(title__icontains=kw) |
            Q(file_type__icontains=kw) |
            Q(content__icontains=kw)  |
            Q(category__icontains=kw)
        ).distinct() #

    #페이지처리
    paginator = Paginator(material_list, 10)
    page_obj = paginator.get_page(page)

    #context 
    user = request.user
    date_now = datetime.datetime.now()
    week = Week.objects.filter(season=user.season, start_date__lte=date_now, end_date__gt=date_now).first()

    context = {'material_list': page_obj,'page':page,'kw':kw,'category':category, 'week':week}
    #데이터를 템플릿에 적용하여 HTML로 변환
    return render(request, 'activities/material_list.html', context)


class FileDownLoadView(SingleObjectMixin, View):
  queryset = Material.objects.all()

  def get(self, request, pk):
    object = self.get_object()
    file_path = object.file.path
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename={object.get_filename()}'

    return response



@login_required(login_url='accounts:login')
def weekly_studies(request):
  user = request.user
  post_data = request.POST
  date_now = datetime.datetime.now()
  week = Week.objects.filter(season=user.season, start_date__lte=date_now, end_date__gt=date_now).first()
  weekly_studies_inst = WeeklyStudies.objects.filter(user=user, week=week).first()
  if request.method=='POST':
    print(request.POST)
    if weekly_studies_inst: 
      updated_request = post_data.copy()
      updated_request.update({'user':user, 'week':week})
      form = WeeklyStudiesForm(updated_request, request.FILES, instance=weekly_studies_inst)
    else: 
      updated_request = post_data.copy()
      updated_request.update({'user':user, 'week':week})
      form = WeeklyStudiesForm(updated_request, request.FILES)
      
    if form.is_valid():
      form.save()
      return redirect('activities:weekly-studies')
    else:
      print(form.errors)

  else:
    return render(request, 'activities/weekly_studies.html', {'week':week, 'weekly_studies':weekly_studies_inst})






