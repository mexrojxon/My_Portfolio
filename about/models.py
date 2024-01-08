from django.db import models
from django.db.models import FilePathField, Model
from django.utils.translation import gettext_lazy as _


class ResumeModel(models.Model):
    resume = models.FileField(verbose_name=_('resume'), upload_to="resume/", )
    resume_link = models.URLField(null=True, blank=True)

    def __text__(self):
        return self.resume


class EducationModel(models.Model):
    place = models.CharField(max_length=100, verbose_name=_('place'))
    country = models.CharField(max_length=50, verbose_name=_('country'))
    faculty = models.CharField(max_length=70, verbose_name=_('faculty'), blank=True, null=True)
    start_date = models.DateField(verbose_name=_('start_date'))
    end_date = models.DateField(verbose_name=_('end_date'), null=True, blank=True)
    short_description = models.TextField(verbose_name=_('short_description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        if self.end_date:
            return str(self.end_date)
        return "Present"

    class Meta:
        verbose_name = _('education')
        verbose_name_plural = _('educations')

    def __str__(self):
        return self.place


class ExperienceModel(models.Model):
    company = models.CharField(max_length=80, verbose_name=_('company'))
    position = models.CharField(max_length=50, verbose_name=_('position'))
    short_description = models.TextField(verbose_name=_('short_description'))
    start_date = models.DateField(verbose_name=_('start_date'))
    end_date = models.DateField(verbose_name=_('end_date'), null=True, blank=True)
    created_at = models.DateTimeField(verbose_name=_('created_at'), auto_now_add=True)

    def __str__(self):
        if self.end_date:
            return str(self.end_date)
        return "Present"

    class Meta:
        verbose_name = _('Experience')
        verbose_name_plural = _('Experiences')

    def __str__(self):
        return self.company


class PortfolioModel(models.Model):
    project_name = models.CharField(max_length=100, verbose_name=_('project_name'))
    project_link = models.URLField(verbose_name=_('project_link'))
    image = models.ImageField(upload_to='projects/', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    class Meta:
        verbose_name = _('portfolio')
        verbose_name_plural = _('portfolios')

    def __str__(self):
        return self.project_name


class ContactModel(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(verbose_name=_('phone'), max_length = 13, null=True, blank=True, )
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


class SocialMediaModel(models.Model):
    instagram = models.URLField(null=True, blank=True, )
    telegram = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    blog = models.URLField(null=True, blank=True)

    def __str__(self):
        return """All links"""
