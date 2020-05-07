from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_list(request):
    return render(request, 'project_list.html', {'projects': sorted(Project.objects.all(), reverse=True)})