from django.db import models

class WebLink(models.Model):
    CATEGORY = [
        ('personal', '개인 즐겨 찾기'),
        ('work', '업무 활용 자료'),
        ('refer', '참고 자료'),
        ('edu', '교육 및 학습 자료'),
        ('others', '기타 자료')
    ]
    id = models.AutoField(primary_key=True)
    created_by = models.CharField(max_length=20)       # 작성한 사용자
    name = models.CharField(max_length=100)     # 웹 링크 이름
    url = models.CharField(max_length=200)      # 주소 길이
    category = models.CharField(max_length=20, choices=CATEGORY, default='personal')

    def __str__(self):
        return self.name