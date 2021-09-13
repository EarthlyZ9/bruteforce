from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core import validators
from django.forms import widgets
from .models import Account_Info
from django.core.validators import RegexValidator

YEARS = [x for x in range (1980, 2020)]


class PasswordChangeCustomForm(PasswordChangeForm):
  def __init__(self, user, *args, **kwargs):
    super(PasswordChangeCustomForm, self).__init__(user, *args, **kwargs)
    self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
    self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
    self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})


class UserForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder':'150자 이하, @/./+/-/_ 가능'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder':'최소 8자 이상의 문자와 숫자로 구성해주세요'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder':'확인을 위해 한 번 더 입력해주세요'})
        self.error_messages['password_mismatch'] = "비밀번호가 일치하지 않습니다."


  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control input-email', 'placeholder':'이메일주소를 입력해주세요.'}))
  mobile_num = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-mobile_num', 'placeholder':'-없이 휴대폰 번호를 입력해주세요.'}), validators=[
        RegexValidator(
            regex='^[0-9]{11}$',
            message='전화번호는 11자이어야 합니다',
            code='mobile_num_invalid',
        )
      ],
      label='휴대폰 번호')



  class Meta:
    model = Account_Info
    #유효성 검사 필드
    fields = ("name", "univ", "course", "email", "individual", "date_of_birth", "mobile_num", "purchase", "username", "recommender", "password1", "password2",  "privacy_policy_1", "privacy_policy_2")
    labels = {
      'name': '이름',
      'univ':'학교',
      'course':'코스',
      'individual':'혼자서 공부할래요',
      'date_of_birth':'생년월일',
      'mobile_num':'휴대폰 번호',
      'email': '이메일',
      'purchase':'구매했습니다',
      'recommender':'추천인',
      'username': '아이디',
      'privacy_policy_1': '개인정보 수집 및 이용에 동의합니다.',
      'privacy_policy_2': '개인정보 제3자 제공에 동의합니다.',
    }

    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control input-name', 'placeholder':'이름을 입력해주세요.'}),
      'univ': forms.TextInput(attrs={'class':'form-control input-univ', 'placeholder':'스터디 매칭을 희망하신다면 꼭 기입해주세요.'}),
      'course': forms.Select(attrs={'class':'form-select','placeholder':'코스를 선택해주세요.'}),
      'individual': forms.CheckboxInput(attrs={'class':'form-check-input input-individual', 'value':'True'}),
      'date_of_birth': forms.SelectDateWidget(attrs={'class':'form-control'}, years = YEARS),
      'purchase': forms.CheckboxInput(attrs={'class':'form-check-input input-purchase', 'value':'True', 'required':''}),
      'recommender': forms.TextInput(attrs={'class':'form-control input-recommender', 'placeholder':'김코딩(010XXXXXXXX)'}),
      'username':forms.TextInput(attrs={'class':'form-control input-username'}),
      'privacy_policy_1': forms.CheckboxInput(attrs={'class':'form-check-input input-privacy_policy_1', 'value':'True', 'required':''}),
      'privacy_policy_2': forms.CheckboxInput(attrs={'class':'form-check-input input-privacy_policy_2', 'value':'True', 'required':''}),
    }

class UpdateInfoForm(forms.ModelForm):

  mobile_num = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[
        RegexValidator(
            regex='^[0-9]{11}$',
            message='전화번호는 11자이어야 합니다',
            code='mobile_num_invalid',
        )
      ],
      label='휴대폰 번호')
  
  class Meta:
    model = Account_Info
    fields = ("mobile_num", "email", "bank_account","bank_name",)
    labels = {
      'mobile_num': '휴대전화 번호',
      'email': '이메일',
      'bank_account': '계좌번호',
      'bank_name': '은행명',
    }
    widgets = {
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'bank_account': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'-없이 계좌번호를 입력해주세요.', 'data-bs-toggle':'tooltip', 'data-bs-placement':'left', 'title':"계좌의 예금주는 회원님의 성함과 일치해야 합니다!"}),
      'bank_name': forms.Select(attrs={'class': 'form-control', 'placeholder':'은행을 선택하세요.', 'data-bs-toggle':'tooltip', 'data-bs-placement':'right', 'title':"계좌의 예금주는 회원님의 성함과 일치해야 합니다!"}), 
    }

class ResetPasswordForm(forms.Form):
  email = forms.EmailField()
