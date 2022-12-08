from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView
import requests
from .form import ContactModelForm
from .models import EducationModel, ExperienceModel, PortfolioModel, SocialMediaModel, ContactModel


class MainPageView(TemplateView):
    template_name = 'about/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self,  **kwargs).get_context_data()
        context['education'] = EducationModel.objects.all()
        context['experience'] = ExperienceModel.objects.all()
        context['portfolio'] = PortfolioModel.objects.all()
        context['social'] = SocialMediaModel.objects.all()

        return context


# class ContactView(CreateView):
#     form_class = ContactModelForm
#     template_name = 'about/index.html'
#
#     def get_success_url(self):
#         return reverse('about:main')

def ContactView(request):
    contact = ContactModel.objects.all()
    context = {
        'contact': contact,
    }
    if request.method == "POST":
        ContactModel.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            message=request.POST.get("message"),
        )
        token = "5969435093:AAEdqNeGE7tQ3DcCIp50MpXxIEjyX_DYvqI"
        text = "Mexroj sizga portfolio saytingizdan xabar yuborishdi 📩: \n\n 👤 Ism: " + request.POST.get('name') + \
               '\n ' \
               + '\n 📧 Email: ' + str(request.POST.get("email")) + '\n 📞 Telefon raqam: ' + str(
            request.POST.get("phone")) + '\n 📝 Xabari: ' + request.POST.get('message')
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
        requests.get(url + str(674182086) + '&text=' + text)
    return render(request, 'about/index.html', context)


def error_404(request, exception):
    return render(request, 'about/error.html')
