"""PersonalSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from about.views import about, resume
from projects.views import project_list, project, comment, category
from contact.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', about, name='about'),
    path('resume/', resume, name='resume'),
    path('projects/', project_list, name='project_list'),
    path('contact/', contact, name='contact'),
    path('projects/<str:name>', project, name='project'),
    path('comment/<str:id>', comment, name='comment'),
    path('projects/category/<str:name>', category, name='category')
]