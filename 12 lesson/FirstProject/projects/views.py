from django.shortcuts import render
from projects.models import Projects

def projects_index(request):
    projects = Projects.objects.all()
    context = {
        'projects' : projects
    }
    return render(request, 'projects_index.html', context)

