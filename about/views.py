from django.shortcuts import render
from django.views.generic import TemplateView
from .models import EducationModel

class MainPageView(TemplateView):
    template_name = 'about/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self, **kwargs).get_context_data()
        context['education'] = EducationModel.objects.all()

        return context