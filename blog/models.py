from unicodedata import category

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _

class CategoryModel(models.Model):
    category = models.CharField(max_length=50, verbose_name=_('category'))
    created_at = models.DateTimeField(verbose_name=_('created_at'))

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class BlogTagModel(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    created_at = models.DateTimeField(verbose_name=_('created_at'))
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

class BlogPostModel(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('title'))
    description = RichTextUploadingField(null = True, verbose_name=_('description'))
    tag = models.ManyToManyField(BlogTagModel, related_name='post', verbose_name=_('tags'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
