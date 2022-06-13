from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentForm
from ..models import Answer, Comment


@login_required(login_url="accounts:login")
def create_answer_comment(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect(
                "{}#comment_{}".format(
                    resolve_url(
                        "discussions:detail", question_id=comment.answer.question.id
                    ),
                    comment.id,
                )
            )
    else:
        form = CommentForm()
    context = {"form": form}
    return render(request, "discussions/comment_form.html", context)


@login_required(login_url="accounts:login")
def modify_answer_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        messages.error(request, "댓글 수정 권한이 없습니다 :(")
        return redirect(
            "{}#comment_{}".format(
                resolve_url("pybo:detail", question_id=comment.answer.question.id),
                comment.id,
            )
        )

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return render(request, "discussions/complete.html")
    else:
        form = CommentForm(instance=comment)
    context = {"form": form}
    return render(request, "discussions/comment_form.html", context)


@login_required(login_url="accounts:login")
def delete_answer_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        messages.error(request, "댓글 삭제 권한이 없습니다 :(")
        return redirect("discussions:detail", question_id=comment.answer.question.id)
    else:
        comment.delete()
    return redirect("discussions:detail", question_id=comment.answer.question.id)
