import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.accounts.models import Account
from .models import WebLink

@csrf_exempt
def add_Feed(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            created_by_username = data.get('created_by')  # username 값
            name = data.get('name')
            url = data.get('url')
            category = data.get('category')

            # username으로 Account 객체 가져오기
            created_by = get_object_or_404(Account, username=created_by_username)

            # ForeignKey 필드는 객체를 저장해야 함
            feeds = WebLink.objects.create(
                created_by=created_by, name=name, url=url, category=category
            )

            return JsonResponse({'message': 'Create Feed successfully', 'id': feeds.id}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
