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
                return JsonResponse({'error': 'Username and password are required'}, status=400)

            # 비밀번호 해싱 (보안 강화)
            hashed_password = make_password(password)

            # 유저 저장
            user = Account.objects.create(username=username, password=hashed_password)

            return JsonResponse({'message': 'User registered successfully', 'user_id': user.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)