from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from .models import Conference, Podpiska
from django.http import HttpResponseRedirect
from .forms import ConferenceForm, PodpiskaForm


# обработка стартовой страницы
def index(request):
    conf_list = Conference.objects.all()
    form = PodpiskaForm()
    return render(request, 'base/index.html', {"conf_list": conf_list, "form": form})


# обработка отправки формы в БД Конференций
def index2(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            emails = Podpiska.objects.all()
            email_list = [item.email for item in emails]
            print(email_list)

            # for item in email_list:
            send_mail("Новая запись о конференции", "Доброго времени суток пользователь. Уведомляю Вас, что на сайте Академии МВД была "
                                                    "зарегистрирована "
                                                    "новая конференция. Ресурс работает в тестовом режиме.",
            settings.EMAIL_HOST_USER,
            email_list,
            fail_silently = False),

            return HttpResponseRedirect('/done')
    else:
        form = ConferenceForm()
    return render(request, 'base/form_conf.html', context={'form': form})


# добавление почты для подписки в модель Podpiska
def subscription(request):
    if request.method == 'POST':
        form = PodpiskaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PodpiskaForm()
    return render(request, 'base/index.html', context={'form': form})


# обработка успешной заполненной формы
def done(request):
    return render(request, 'base/done.html')

# тренировка
