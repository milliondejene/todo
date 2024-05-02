from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def task_list(request):
    return render(request, 'task_list.html')