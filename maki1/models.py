from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id', )
        get_latest_by = 'id'

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        #return reverse('posts:detail', kwargs={'id': self.id})
        pass

    def is_valid(self):
        if len(content) > 10:
            return True

        return False


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)

    class Meta:
        ordering = ('-id', )
        get_latest_by= 'id'

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        #return reverse('posts:detail', kwargs={'id': self.post.id})
        pass
