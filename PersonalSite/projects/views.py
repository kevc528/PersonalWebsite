from django.shortcuts import render, redirect
from projects.models import Project, Comment, ProjectCategory


# Render page listing all of the projects
def project_list(request):
    return render(request, 'project_list.html',
                  {'projects': sorted(Project.objects.all(), reverse=True)})


# Render page specific for a project given the name
def project(request, name):
    project = Project.objects.filter(title=name)
    if len(project) != 0:
        project = project.first()
        return render(request, 'project.html', {'project': project})
    else:
        return redirect('project_list')


# Post route for posting a comment and redirecting back to the project
def comment(request, id):
    if request.method == 'POST':
        author = request.POST.get('author')
        print(author)
        comment = request.POST.get('comment')
        if comment != '':
            comment_obj = Comment(author=author, comment=comment)
            comment_obj.save()
            project = Project.objects.filter(id=id).first()
            project.comments.add(comment_obj)
        return redirect('/projects/' + project.title)
    else:
        return redirect('project_list')


# Get all of the projects under the given category name
def category(request, name):
    category = ProjectCategory.objects.filter(name=name)
    if len(category) != 0:
        category = category.first()
        projects = category.project_set.all()
        return render(request, 'category.html',
                      {'category': category,
                       'projects': sorted(projects, reverse=True)})
    else:
        return redirect('project_list')