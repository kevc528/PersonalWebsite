from django.shortcuts import render, redirect
from django.http import HttpResponse


# splash page for bio
def about(request):
    return render(request, 'about.html', {})


# download resume from file directory
def resume(request):
    filepath = '../resume.pdf'
    with open(filepath, 'rb') as fp:
        data = fp.read()
    filename = 'KevinChenResume.pdf'
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    response.write(data)
    return response
