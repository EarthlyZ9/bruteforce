from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Account_Info(AbstractUser):
  COURSE_CHOICES = (
    ('python', '파이썬'),
    ('datascience', '데이터 사이언스'),
    ('htmlcss', '웹 퍼블리싱')
  )

  BANK_LIST = (
    ('kb', '국민'),
    ('nh', '농협'),
    ('sinhan', '신한'),
    ('sc', 'SC제일'),
    ('kakao', '카카오뱅크'),
    ('ibk', 'IBK기업'),
    ('hana','하나'),
    ('woori', '우리'),
    ('dgb', '대구'),
    ('bnk_busan','부산'),
    ('kj','광주'),
    ('kfcc', '새마을'),
    ('bnk_kn', '경남'),
    ('post', '우체국'),
    ('cu', '신협'),
    ('sh', '수협'),
    ('citi','씨티'),
    ('kbank','케이뱅크'),
    ('sj','산림조합')
  )

  PRIVACY_POLICY_CONTENT_1 = """[개인정보 수집 및 이용 동의서]
  
1. 개인정보 수집 및 이용 목적
「BruteForce : 코딩 인터넷 기초교육 연계」 프로 그램의 전반적인 업무에 필요한 개인정보를 수집하고 이용하고자 합니다.

2. 개인정보 수집 및 이용 항목 
회원 가입 시에 '아아디, 비밀번호, 성명, 생년월일, 휴대전화번호, 이메일, 재학중인 학교명'을 필수항목으로 수집합니다.

3. 수집된 개인정보의 보유 및 이용기간 
수집된 개인정보는 개인정보를 제공한 날로부터 약 3개월간 보관되며, BurteForce 활동이 완료되는 시점에 즉시 파기됩니다. 

4. 비동의 시 불이익 
내용 해당 프로젝트 지원자는 개인정보 수집 및 이용 동의를 거절하실 수 있으며, 이 경우에는 프로그램 참여가 어려울 수 있습니다. 


본인은 「BruteForce : 코딩 인터넷 기초교육 연계」 프로그램의 전반적인 업무에 필요한 개인정보를 아래와 같이 수집 및 이용토록 하는 것에 동의합니다. 
"""
  PRIVACY_POLICY_CONTENT_2 = """[제 3자 개인정보 동의서]

1. 개인정보 제 3자 제공 목적 
「BruteForce : 코딩 인터넷 기초교육 연계」 프로그램 참여자들이 강의를 프로모션 가격으로 이용할 수 있도록 이에 필요한 개인정보를 코딩 교육 플랫폼을 제공하는 기업 ‘코드잇’ 에게 제공하고자 합니다. 

2. 개인정보 수집 및 이용 항목 
가. 일반정보 : 성명, 연락처, 네이버 계정, 코드잇 계정
나. 민감정보 및 고유식별정보 : 연락처, 네이버 계정, 코드잇 계정


3. 제공된 개인정보의 보유 및 이용기간 
제공된 개인정보는 개인정보를 제공한 날로부터 약 3개월간 보관되며, BurteForce 활동이 완료되는 시점에 즉시 파기됩니다. 

4. 비동의 시 불이익 내용 
해당 프로젝트 지원자는 개인정보 수집 및 이용 동의를 거절하실 수 있으며, 이 경우에는 코드잇 이용권 할인 프로모션이 제공되지 않음을 유의하시기 바랍니다. 


본인은 「BruteForce : 코딩 인터넷 기초교육 연계」 프로그램의 전반적인 업무에 필요한 개인정보를 아래와 같이 제 3자에게 제공하는 것에 동의합니다.

해당 프로젝트 지원자는 개인정보 수집 및 이용 동의를 거절하실 수 있으며, 이 경우에는 코드잇 멤버십 할인 프로모션이 제공되지 않음을 유의하시기 바랍니다.
"""

  name = models.CharField(max_length=10)
  date_of_birth = models.DateField()
  season = models.IntegerField(blank=True, null=True, default=8)
  course = models.CharField(max_length=15, choices=COURSE_CHOICES)
  individual = models.BooleanField(default=False, null = True, blank=True, help_text="파이썬 코스를 개인 단위로 수강하고자 하시는 분들은 체크해주세요! (데이터 사이언스 코스의 경우 스터디 활동이 필수이며, 웹 퍼블리싱 코스는 개인 단위로 이루어집니다.)")
  univ = models.CharField(max_length=15, null=True, blank=True)
  mobile_num = models.CharField(max_length=11)
  recommender = models.CharField(max_length=100, null=True, blank=True)
  purchase = models.BooleanField(default=False, help_text="BruteForce 프로그램에 참여하기 위해서는 멤버십 구매가 필요합니다. 구매를 완료하셨다면 체크해주세요!")
  privacy_policy_1 = models.BooleanField(default=False, help_text=PRIVACY_POLICY_CONTENT_1)
  privacy_policy_2 = models.BooleanField(default=False, help_text=PRIVACY_POLICY_CONTENT_2)
  signup_date = models.DateField(auto_now_add=True, null=True)
  bank_account = models.CharField(max_length=30, null=True, blank=True, default="입력전")
  bank_name = models.CharField(max_length=20, choices=BANK_LIST, null=True, blank=True, default="입력전")
  season = models.IntegerField(blank=True, default='7', null=True)
  group = models.IntegerField(blank=True, null=True)

  REQUIRED_FIELDS =['name', 'date_of_birth','course','univ','mobile_num']

  def __str__(self):
    return str(self.season) + '_' + str(self.username)
