from django.db import models
from django.db.models import FilePathField
from django.utils.translation import gettext_lazy as _


class ResumeModel(models.Model):
    resume = models.FileField(verbose_name=_('resume'), upload_to="resume/",)

    def __name__(self):
        return self.resume
