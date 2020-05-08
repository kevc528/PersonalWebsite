from django.db import models


# Create your models here.
class ProjectCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=200)
    comment = models.TextField()
    post_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author

    def __lt__(self, other):
        return self.post_time < other.post_time


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    category = models.ManyToManyField(ProjectCategory)
    comments = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return self.title

    def __lt__(self, other):
        return self.end_date < other.end_date
