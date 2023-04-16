from django.shortcuts import render
from projects.models import Projects

def prjects_index(request):
    projects = Projects.objects.all
    context = {
        'projects' : projects
    }
    return render(request, 'project_index.html', context)
# Create your views here.
