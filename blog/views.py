from django.http import request
from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from hitcount.models import HitCount
from hitcount.views import HitCountDetailView
from django.db.models import Q
import requests
from about.models import SocialMediaModel
from blog.form import CommentModelForm
from blog.models import BlogPostModel, CategoryModel, TagModel, CommentModel

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
    
    social = SocialMediaModel.objects.all()
    popular_posts = BlogPostModel.objects.order_by('-hit_count_generic__hits')[:3]
    categories = CategoryModel.objects.all()
    tags = TagModel.objects.all()
    context = {
        "post" : post,
        "social": social,
        "popular_posts": popular_posts,
        "categories":categories,
        "tags":tags

       }
    return render(request, 'blog/blog.html', context )

class BlogDetailView(HitCountDetailView):
    model = BlogPostModel
    template_name = 'blog/blog-detail.html'
    context_object_name = 'single_post'
    slug_field = 'slug'
    count_hit = True
    social = SocialMediaModel.objects.all()


# class BlogCommentView(CreateView):
#     form_class = CommentModelForm
#
#     def form_valid(self, form):
#         form.instance.post = get_object_or_404(BlogPostModel, pk=self.kwargs.get('slug'))
#         return super(BlogCommentView, self).form_valid(form)
#
#     def get_success_url(self):
#         return reverse('blog:detail')

# def BlogCommentView(request, pk):
#     comment = CommentModel.objects.all()

#     context = {
#         'comment': comment,
#     }
#     if request.method == "POST":
#         CommentModel.objects.create(
#             name=request.POST.get("name"),
#             email=request.POST.get("email"),
#             comment=request.POST.get("comment"),
#         )
#         token = token
#         text = "Mexroj sizga portfolio saytingizdan xabar yuborishdi 📩: \n\n 👤 Ism: " + request.POST.get('name') + \
#                '\n ' \
#                + '\n 📧 Email: ' + str(request.POST.get("email")) + '\n  📝 Xabari: ' + request.POST.get('comment')
#         url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
#         requests.get(url + str(674182086) + '&text=' + text)
#     return render(request, 'blog/blog-detail.html', context)
