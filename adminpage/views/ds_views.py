from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from accounts.models import Account_Info
from activities.models import WeeklyStudies, Week
from points.models import PurchaseRequest
from ..models import AdditionalPoints, PointsStatus, WeeklyActivityPoints, Progress
from django.db.models import Q
from django.core.paginator import Paginator
import datetime

@staff_member_required
def ds_points(request): 
  date_now = datetime.datetime.now()
  cal_week = Week.objects.filter(start_date__lte=date_now, end_date__gte=date_now).first()
  week = cal_week.week_num - 1 #보통 자정이 지나고 week가 넘어간 뒤에 집계를 누르므로
  ds_user_list = Account_Info.objects.filter(course='datascience').order_by('name') 

  for ds_user in ds_user_list:

    
    
    if not ds_user.weeklyactivitypoints_set.filter(week_num=week): #처음으로 집계를 누른 상태일 때

      ds_user_study_record = ds_user.weeklystudies_set.filter(week=week).first() #해당 주차 학습을 했는지

      
      #WeeklyActivityPoints 에 create
      data = dict()
      data['week_num'] = week
      data['user'] = ds_user
      if ds_user_study_record: #해당 주차 제출함
        if ds_user_study_record.week.week_num >= 9: 
          if ds_user_study_record.attendance:
            data['attendance'] = 100
          if ds_user_study_record.file:
            data['weekly_studies'] = 300
        else:
          if ds_user_study_record.attendance:
            data['attendance'] = 100
          if ds_user_study_record.file:
            data['weekly_studies'] = 200
        c = WeeklyActivityPoints(**data)
        c.save()
      else: #해당 주차 제출 안함 -> model defalut 값인 0으로 채움
        WeeklyActivityPoints.objects.create(week_num=week, user=ds_user)

    

    ds_user_weekly_studies = ds_user.weeklyactivitypoints_set.all() #현재까지 기록된 주차별 학습 활동 점수 
    ds_user_progress_record = ds_user.progress_set.all().first() #현재까지 기록된 진도율 점수 (유저 당 record 하나)
    ds_user_additional_record = ds_user.additionalpoints_set.all().first() #현재까지 기록된 추가 점수 (유저 당 record 하나)
    
    #합계 구하기 - 주차별 활동
    weekly_ap = 0
    for record in ds_user_weekly_studies:
      weekly_ap = weekly_ap + record.attendance
      weekly_ap = weekly_ap + record.weekly_studies

    #합계 구하기 - 진도율
    if ds_user_progress_record: #진도율 기록이 있으면 계산
      progress_ap =  ds_user_progress_record.progress1 +  ds_user_progress_record.progress2 +  ds_user_progress_record.progress3 +  ds_user_progress_record.progress4
    else:
      Progress.objects.create(user=ds_user) #아예 없으면 default 값인 0으로 채운 기록 만들기
      ds_user_progress_record = ds_user.progress_set.all().first()
      progress_ap =  ds_user_progress_record.progress1 +  ds_user_progress_record.progress2 +  ds_user_progress_record.progress3 +  ds_user_progress_record.progress4

    #합계 구하기 - 추가 점수
    if ds_user_additional_record:
      additional_ap = ds_user_additional_record.additional_points
    else:
      AdditionalPoints.objects.create(user=ds_user)
      ds_user_additional_record = ds_user.additionalpoints_set.all().first()
      additional_ap = ds_user_additional_record.additional_points

    #총합 구하기
    total_ap = weekly_ap + progress_ap + additional_ap

    #집계 시점까지 사용한 총 포인트 계산
    purchase_records = PurchaseRequest.objects.filter(user=ds_user)
    #총 사용 포인트 계산
    used_ap = 0
    if purchase_records:
      for record in purchase_records:
        used_ap += record.purchase_option.price


    #PointsStatus 값 create or update
    user_points_status = ds_user.pointsstatus_set.filter(user=ds_user).first()
    if user_points_status: #값 있을 때 -> update
      user_points_status.total_points = total_ap
      user_points_status.used_points = used_ap
    else: #값 없을 때 -> create
      points_data = dict()
      points_data['user'] = ds_user
      points_data['total_points'] = total_ap
      points_data['used_points'] = used_ap
      m = PointsStatus(**points_data)
      m.save()


  #paging, search, dropdown
  
  #Get으로 페이지 가져옴 디폴트값은 1
  page = request.GET.get('page','1')
  #검색어 가져옴
  kw = request.GET.get('kw','')
  

  #들어온 검색어로 검색.
  if kw:
    #검색 내용
    #filter함수에서는 모델속서에 접근하기위해 언더바두개씀
    ds_user_list = ds_user_list.filter(
        Q(username__icontains=kw) |
        Q(name__icontains=kw)
    ).distinct() 

  #페이지처리
  paginator = Paginator(ds_user_list, 30)
  page_obj = paginator.get_page(page)

  #week_list 
  week_list = range(1, week + 1)

  context = {'ds_user_list': page_obj, 'page':page,'kw':kw, 'weekly_ap':weekly_ap, 'progress_ap':progress_ap,'additional_ap':additional_ap,'total_ap':total_ap, 'week_list':week_list}
  #데이터를 템플릿에 적용하여 HTML로 변환
  return render(request, 'adminpage/ds_points.html', context=context)