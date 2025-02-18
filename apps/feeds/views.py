import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.accounts.models import Account
from .models import WebLink

@csrf_exempt
def add_feed(request):
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

@csrf_exempt
def edit_Feed(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            created_by = data.get('created_by')  # 요청에서 username 가져오기
            feed_id = data.get('feed_id')
            name = data.get('name')
            url = data.get('url')
            category = data.get('category')

            # username이 존재하는지 확인하고, role도 함께 가져오기
            user = get_object_or_404(Account, username=created_by)
            user_role = user.role  # role 속성 가져오기

            # 유저의 권한이 충분하지 않다면 비승인
            if user_role != "admin":
                return JsonResponse({'message' : "Unauthorized User"}, status = 403)
            
            # 수정할 feed 가져오기
            feed = get_object_or_404(WebLink, id=feed_id)

            # feed 내용 업데이트
            feed.name = name
            feed.url = url
            feed.category = category
            feed.save()

            return JsonResponse({'message': 'Feed updated successfully', 'role': user_role}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def delete_feed(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

        except:
            return
