from django.db import models
from apps.accounts.models import Account

class WebLink(models.Model):
    CATEGORY = [
        ('personal', '개인 즐겨 찾기'),
        ('work', '업무 활용 자료'),
        ('refer', '참고 자료'),
        ('edu', '교육 및 학습 자료'),
        ('others', '기타 자료')
    ]

    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE, to_field='username')
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY, default='personal')

    editors = models.ManyToManyField(Account, related_name="editable_links", blank=True)

    def __str__(self):
        return self.name
