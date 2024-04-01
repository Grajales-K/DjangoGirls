from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    # this _str_ double underscore is called dunder
        
    def __str__(self):
        return self.title


>>> from blog.models import Post
>>> Post.objects.all()
<QuerySet [<Post: Resume-Building Workshop>, <Post: Backend Study Group [Online]: Designing Data-Intensive Applications (Chapter 4)>, <Post: learning python>]>
>>> 


➜  djangogirls git:(main) git status
On branch main
nothing to commit, working tree clean
➜  djangogirls git:(main) 