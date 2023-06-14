from django.http import request
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from hitcount.models import HitCount
from hitcount.views import HitCountDetailView
from django.db.models import Q
import requests
from about.models import SocialMediaModel
from blog.form import CommentForm
from blog.models import BlogPostModel, CategoryModel, TagModel, CommentModel
from django.core.paginator import Paginator


def BlogListView(request):
    if "search" in request.GET:
        search = request.GET["search"]
        post = BlogPostModel.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
    elif "tag" in request.GET:
        tag = request.GET["tag"]
        post = BlogPostModel.objects.filter(tag__title=tag)
    elif "category" in request.GET:
        category = request.GET["category"]
        post = BlogPostModel.objects.filter(category__category=category)
    else:
        post = BlogPostModel.objects.all().order_by('-id')
    paginator = Paginator(post, 4)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    social = SocialMediaModel.objects.all()
    popular_posts = BlogPostModel.objects.order_by('-hit_count_generic__hits')[:3]
    categories = CategoryModel.objects.all()
    tags = TagModel.objects.all()
    context = {
        "post": post,
        "social": social,
        "popular_posts": popular_posts,
        "categories": categories,
        "tags": tags,


    }
    return render(request, 'blog/blog.html', context)


class BlogDetailView(HitCountDetailView):
    model = BlogPostModel
    template_name = 'blog/blog-detail.html'
    context_object_name = 'single_post'
    slug_field = 'slug'
    count_hit = True

    def post_comment(request, slug):
        if request.method == 'POST':
            post = BlogPostModel.objects.get(slug=slug)
            name = request.POST.get('name')
            email = request.POST.get('email')
            comment = request.POST.get('comment')

            comment_obj = CommentModel.objects.create(
                post=post,
                name=name,
                email=email,
                comment=comment
                )
            comment_obj.save()

        return redirect('blog:detail', slug=slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = CommentModel.objects.filter(post=post)
        context['comments'] = comments
        return context
