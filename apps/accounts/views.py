from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Account
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password

@csrf_exempt  # CSRF 우회 (테스트용)
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # JSON 데이터 파싱
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return JsonResponse({'error': '아이디와 비밀번호를 입력해주세요'}, status=400)
            
            # 아이디 중복 체크
            if Account.objects.filter(username = username).exists():
                return JsonResponse({'error' : '이미 중복된 아이디 입니다.'}, status=400)
            
            # 비밀번호 해싱을 통한 보안 강화
            hashed_password = make_password(password)

            # 유저 저장
            user = Account.objects.create(username=username, password=hashed_password)

            return JsonResponse({'message': 'User registered successfully', 'user_id': user.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)