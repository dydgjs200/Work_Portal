import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import WebLink
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_Feed(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            created_by = data.get('created_by')
            name = data.get('name')
            url = data.get('url')
            category = data.get('category')

            feeds = WebLink.objects.create(created_by = created_by, name = name, url = url, category = category)

            return JsonResponse({'message': 'Create Feed successfully', 'id' : feeds.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
    return JsonResponse({'error': 'Invalid request method'}, status=405)