from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Event, Task
import json

@method_decorator(csrf_exempt, name='dispatch')
class CalendarView(View):
    def get(self, request):
        events = list(Event.objects.values())
        return JsonResponse(events, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        event = Event.objects.create(title=data['title'], date=data['date'])
        return JsonResponse({'id': event.id, 'title': event.title, 'date': event.date})
    
    def put(self, request, id):
        data = json.loads(request.body)
        event = get_object_or_404(Event, id=id)
        event.title = data['title']
        event.date = data['date']
        event.save()
        return JsonResponse({'id': event.id, 'title': event.title, 'date': event.date})
    
    def delete(self, request, id):
        event = get_object_or_404(Event, id=id)
        event.delete()
        return JsonResponse({'result': 'Event deleted'})

@method_decorator(csrf_exempt, name='dispatch')
class TaskView(View):
    def get(self, request):
        tasks = list(Task.objects.values())
        return JsonResponse(tasks, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        task = Task.objects.create(task=data['task'], completed=data['completed'])
        return JsonResponse({'id': task.id, 'task': task.task, 'completed': task.completed})
    
    def put(self, request, id):
        data = json.loads(request.body)
        task = get_object_or_404(Task, id=id)
        task.task = data['task']
        task.completed = data['completed']
        task.save()
        return JsonResponse({'id': task.id, 'task': task.task, 'completed': task.completed})
    
    def delete(self, request, id):
        task = get_object_or_404(Task, id=id)
        task.delete()
        return JsonResponse({'result': 'Task deleted'})