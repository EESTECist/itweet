from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from .models import Post, Comment


class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'maki1/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['user'] = self.request.user

        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(PostListView, self).get(request, *args, **kwargs)

        else:
            return HttpResponseRedirect('/login')


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'maki1/detail.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['comments'] = self.get_object().comment_set.all()
        context['user'] = self.request.user

        return context

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(PostDetailView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login')
