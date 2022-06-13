from django.db import models
from accounts.models import Account_Info


class Question(models.Model):
    CATEGORY = (
        ("python", "파이썬"),
        ("datascience", "데이터 사이언스"),
        ("htmlcss", "웹 퍼블리싱"),
        ("etc", "기타"),
    )
    author = models.ForeignKey(Account_Info, on_delete=models.CASCADE)
    category = models.CharField(max_length=15, choices=CATEGORY)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.URLField(max_length=225, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.author) + "_" + str(self.title)


class Answer(models.Model):
    author = models.ForeignKey(
        Account_Info, on_delete=models.CASCADE, related_name="author_answer"
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    voter = models.ManyToManyField(Account_Info, related_name="voter_answer")
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.question) + "에 대한 " + str(self.author) + "의 답변"


class Comment(models.Model):
    author = models.ForeignKey(Account_Info, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
