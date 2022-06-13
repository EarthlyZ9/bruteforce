from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse
import json

from ..models import Answer

@login_required(login_url='accounts:login')
def vote_answer(request, answer_id):
  user = request.user
  answer = get_object_or_404(Answer, id=answer_id)
  if user == answer.author:
    message ='본인이 작성한 글은 추천할 수 없어요 :('
  elif answer.voter.filter(id = user.id):
    message ='이미 추천하셨네요!'
  else:
      answer.voter.add(request.user)
      message = '추천하셨습니다!'
  
  ret = {
    'message': message,
    'counts': answer.voter.count(),
  }
  
  return HttpResponse(json.dumps(ret), content_type="application/json")