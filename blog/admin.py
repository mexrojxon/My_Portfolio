from django.contrib import admin
from .models import *
admin.site.register(CategoryModel)
admin.site.register(TagModel)
admin.site.register(BlogPostModel)
admin.site.register(CommentModel)

