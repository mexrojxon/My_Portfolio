from unicodedata import category

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from hitcount.models import HitCount


class CategoryModel(models.Model):
    category = models.CharField(max_length=50, verbose_name=_('category'))
    created_at = models.DateTimeField(verbose_name=_('created_at'))

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class TagModel(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    created_at = models.DateTimeField(verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class BlogPostModel(models.Model):
    title = models.CharField(max_length=300, verbose_name=_('title'))
    description = RichTextUploadingField(null=True, verbose_name=_('description'))
    image = models.ImageField(upload_to='blog/', verbose_name=_('image'))

    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        related_name='post'
    )
    tag = models.ManyToManyField(
        TagModel,
        related_name='post',
        verbose_name=_('tags')
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    slug = models.SlugField(unique=True, max_length=100)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(BlogPostModel, self).save(*args, **kwargs)


class CommentModel(models.Model):
    post = models.ForeignKey(
        BlogPostModel,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('post')
    )
    name = models.CharField(max_length=64, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    comment = models.TextField(verbose_name=_('comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.name
