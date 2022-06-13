from django.shortcuts import get_object_or_404, render, redirect
from ..models import Question
from ..forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

@login_required(login_url='accounts:login')
def create_question(request):
  if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('discussions:question-list')
  else:
      form = QuestionForm()
  context = {'form': form}
  return render(request, 'discussions/question_form.html', context)

@login_required(login_url='accounts:login')
def modify_question(request, question_id):
  question = get_object_or_404(Question, id=question_id)

  if request.method == "POST":
      form = QuestionForm(request.POST, instance=question)
      if form.is_valid():
          question = form.save(commit=False)
          question.author = request.user
          question.modify_date = timezone.now()  # 수정일시 저장
          question.save()
          return redirect('discussions:detail', question_id=question.id)
  else:
      form = QuestionForm(instance=question)
  context = {'form': form}
  return render(request, 'discussions/question_form.html', context)


@login_required(login_url='accounts:login')
def delete_question(request, question_id):
  question = get_object_or_404(Question, id=question_id)
  question.delete()
  return redirect('discussions:question-list')
