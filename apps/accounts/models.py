from django.db import models

class Account(models.Model):
    ROLE_CHOICE = [
        ('user', '일반 사용자'),
        ('admin', '관리자'),
    ]
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICE, default='user')

    def __str__(self):
        return self.username