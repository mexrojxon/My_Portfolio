from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from .form import ContactModelForm
from .models import EducationModel, ExperienceModel, PortfolioModel, SocialMediaModel


class MainPageView(TemplateView):
    template_name = 'about/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self, **kwargs).get_context_data()
        context['education'] = EducationModel.objects.all()
        context['experience'] = ExperienceModel.objects.all()
        context['portfolio'] = PortfolioModel.objects.all()
        context['social'] = SocialMediaModel.objects.all()


        return context

class ContactView(CreateView):
    form_class = ContactModelForm
    template_name = 'about/index.html'

    def get_success_url(self):
        return reverse('about:main')

