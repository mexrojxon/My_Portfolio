from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from about.models import SocialMediaModel

class BlogListView(TemplateView):
    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self, **kwargs).get_context_data()
        context['social'] = SocialMediaModel.objects.all()

        return context
