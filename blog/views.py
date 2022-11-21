from django.http import request
from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from hitcount.models import HitCount
from hitcount.views import HitCountDetailView
from django.db.models import Q

from about.models import SocialMediaModel
from blog.form import CommentModelForm
from blog.models import BlogPostModel, CategoryModel, TagModel


class BlogListView(ListView):
    model = BlogPostModel
    template_name = 'blog/blog.html'
    count_hit = True



    def get_context_data(self, **kwargs):
        context = super(BlogListView, self, **kwargs).get_context_data()
        context['post'] = BlogPostModel.objects.all().order_by('-id')
        context['social'] = SocialMediaModel.objects.all()
        context['categories'] = CategoryModel.objects.all()
        context['tags'] = TagModel.objects.all()
        context['q'] = self.request.GET.get('q', '')
        context.update({
            'popular_posts': BlogPostModel.objects.order_by('-hit_count_generic__hits')[:3],
        })

        return context

    def get_queryset(self):
        qs = BlogPostModel.objects.order_by('-pk')
        tag = self.request.GET.get('tag')
        if tag:
            return qs.filter(tag__title=tag)
        return qs


        # qs = BlogPostModel.objects.all()
        # q = self.request.GET.get('q')
        # if q:
        #     qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
        #     return qs
        # qs = BlogPostModel.objects.order_by('-pk')
        #
        # return qs


class BlogDetailView(HitCountDetailView):
    model = BlogPostModel
    template_name = 'blog/blog-detail.html'
    context_object_name = 'single_post'
    slug_field = 'slug'
    count_hit = True
    social = SocialMediaModel.objects.all()


class BlogCommentView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(BlogPostModel, pk=self.kwargs.get('slug'))
        return super(BlogCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail')
