import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import WebLink
from django.views.decorators.csrf import csrf_exempt
from apps.accounts.models import Account


@csrf_exempt
def add_Feed(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            created_by = data.get('created_by')
            name = data.get('name')
            url = data.get('url')
            category = data.get('category')

            # 아이디가 유저(Accounts)에 있는지 확인 필요
            if not Account.objects.filter(username = created_by).exists():
                return JsonResponse({'error': 'User does not exist'}, status=404)

            feeds = WebLink.objects.create(created_by = created_by, name = name, url = url, category = category)

            return JsonResponse({'message': 'Create Feed successfully', 'id' : feeds.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
    return JsonResponse({'error': 'Invalid request method'}, status=405)