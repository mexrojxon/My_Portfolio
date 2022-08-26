from django.db import models
from django.db.models import FilePathField
from django.utils.translation import gettext_lazy as _


class ResumeModel(models.Model):
    resume = models.FileField(verbose_name=_('resume'), upload_to="resume/", )

    def __name__(self):
        return self.resume


class EducationModel(models.Model):
    place = models.CharField(max_length=100, verbose_name=_('place'))
    country = models.CharField(max_length=50, verbose_name=_('country'))
    faculty = models.CharField(max_length=70, verbose_name=_('faculty'), blank=True, null=True)
    start_date = models.DateField(verbose_name=_('start_date'))
    end_date = models.DateField(verbose_name=_('end_date'))
    short_description = models.CharField(max_length=255, verbose_name=_('short_description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    class Meta:
        verbose_name = _('education')
        verbose_name_plural = _('educations')

    def __str__(self):
        return self.place
