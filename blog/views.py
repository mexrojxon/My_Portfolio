from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from hitcount.models import HitCount
from hitcount.views import HitCountDetailView

from about.models import SocialMediaModel
from blog.models import BlogPostModel


class BlogListView(TemplateView):
    template_name = 'blog/blog.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self, **kwargs).get_context_data()
        context['post'] = BlogPostModel.objects.all().order_by('-id')
        context['social'] = SocialMediaModel.objects.all()

        return context


class BlogDetailView(HitCountDetailView):
    model = BlogPostModel
    template_name = 'blog/blog-detail.html'
    context_object_name = 'single_post'
    slug_field = 'slug'
    count_hit = True
