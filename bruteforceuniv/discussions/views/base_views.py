from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.db.models import Q
from ..models import Question
from django.contrib.auth.decorators import login_required


def question_list(request):
    # Get으로 페이지 가져옴 디폴트값은 1
    page = request.GET.get("page", "1")
    # 검색어 가져옴
    kw = request.GET.get("kw", "")
    # 정렬기준 가져옴
    category = request.GET.get("category", "all")

    # 생성날짜 순으로 정렬해서 모델에서 가져옴
    question_list = Question.objects.order_by("-create_date")

    # 정렬
    if category == "python":
        question_list = Question.objects.filter(category="python")
    elif category == "datascience":
        question_list = Question.objects.filter(category="datascience")
    elif category == "htmlcss":
        question_list = Question.objects.filter(category="htmlcss")
    elif category == "etc":
        question_list = Question.objects.filter(category="etc")
    else:  # all
        question_list = Question.objects.order_by("-create_date")

    # 들어온 검색어로 검색.
    if kw:
        # 제목, 내용 , 글쓴이, 답변이
        # filter함수에서는 모델속서에 접근하기위해 언더바두개씀
        question_list = question_list.filter(
            Q(title__icontains=kw)
            | Q(category__icontains=kw)
            | Q(content__icontains=kw)
            | Q(author__icontains=kw)
        ).distinct()  #

    # 페이지처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {"question_list": page_obj, "page": page, "kw": kw, "category": category}
    # 데이터를 템플릿에 적용하여 HTML로 변환
    return render(request, "discussions/question_list.html", context)


@login_required(login_url="accounts:login")
def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {"question": question}
    return render(request, "discussions/question_detail.html", context)
