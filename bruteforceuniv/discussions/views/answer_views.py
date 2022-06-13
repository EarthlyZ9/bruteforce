from django.shortcuts import get_object_or_404, render, redirect, resolve_url
from ..models import Question, Answer
from ..forms import AnswerForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse

@login_required(login_url='accounts:login')
def create_answer(request, question_id):
  question = get_object_or_404(Question, id=question_id)
  if request.method == "POST":
    form = AnswerForm(request.POST)
    if form.is_valid():
      answer = form.save(commit=False)
      answer.author = request.user
      answer.create_date = timezone.now()
      answer.question = question
      answer.save()
      return redirect('{}#answer_{}'.format(resolve_url('discussions:detail', question_id=question.id), answer.id))
  else:
      form = AnswerForm()
  context = {'question': question, 'form': form}
  return render(request, 'discussions/question_detail.html', context)

@login_required(login_url='accounts:login')
def modify_answer(request, answer_id):
  answer = get_object_or_404(Answer, id=answer_id)

  if request.method == "POST":
    form = AnswerForm(request.POST, instance=answer)
    if form.is_valid():
      answer = form.save(commit=False)
      answer.author = request.user
      answer.modify_date = timezone.now()
      answer.save()
      return render(request, 'discussions/complete.html')
  else:
      form = AnswerForm(instance=answer)
  context = {'answer': answer, 'form': form}
  return render(request, 'discussions/answer_form.html', context)


@login_required(login_url='accounts:login')
def delete_answer(request, answer_id):
  answer = get_object_or_404(Answer, pk=answer_id)
  answer.delete()
  return redirect('discussions:detail', question_id=answer.question.id)