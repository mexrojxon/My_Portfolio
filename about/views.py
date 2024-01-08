from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView
import requests
from .form import ContactModelForm
from .models import *
from config.settings import TOKEN, ADMIN

class MainPageView(TemplateView):
    template_name = 'about/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self,  **kwargs).get_context_data()
        context['education'] = EducationModel.objects.all()
        context['experience'] = ExperienceModel.objects.all()
        context['portfolio'] = PortfolioModel.objects.all()
        context['social'] = SocialMediaModel.objects.all()
        context['resume'] = ResumeModel.objects.all()[:1]

        return context


def ContactView(request):
    contact = ContactModel.objects.all()
    context = {
        'contact': contact,
    }
    if request.method == "POST":
        ContactModel.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message"),
            phone=request.POST.get("phone" ),
        )
        token = TOKEN
        text = "Mexroj sizga portfolio saytingizdan xabar yuborishdi 📩: \n\n👤 Ism: " + str(request.POST.get('name', '')) + \
       '\n\n📧 Email: ' + str(request.POST.get("email", '')) + '\n\n📞 Telefon raqam: ' + str(request.POST.get("phone", '')) + \
       '\n\n📝 Xabari: ' + str(request.POST.get('message', ''))
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
        requests.get(url + str(ADMIN) + '&text=' + text)

    return render(request, 'about/index.html', context)


def error_404(request, exception):
    return render(request, 'about/error.html')
