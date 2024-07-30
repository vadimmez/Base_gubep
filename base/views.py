from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Conference, Podpiska
from django.http import HttpResponseRedirect
from .forms import ConferenceForm, PodpiskaForm
from django.core.paginator import Paginator
from .filters import ConferenceFilter
from django.contrib.auth.decorators import login_required
import os
import threading


# обработка стартовой страницы
def index(request):
    qs = Conference.objects.all()
    f = ConferenceFilter(request.GET, queryset=qs)
    form = PodpiskaForm()
    paginator = Paginator(f.qs, 30)
    page = request.GET.get('page')
    conf_list = paginator.get_page(page)
    return render(request, 'base/index.html', {"conf_list": conf_list, "form": form, 'filter': f})


def send_email(email_list):
    send_mail("Новая запись о конференции",
              "Доброго времени суток пользователь. Уведомляю Вас, что на сайте Академии МВД была "
              "зарегистрирована "
              "новая конференция. https://www.nio.amia.by. Ресурс работает в тестовом режиме.",
              settings.EMAIL_HOST_USER,
              email_list,
              fail_silently=False)


@login_required
# обработка отправки формы в БД Конференций
def index2(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            emails = Podpiska.objects.all()
            email_list = list(set([item.email for item in emails]))

            thread = threading.Thread(target=send_email, args=[email_list])
            thread.start()

            # threads = [threading.Thread(target=send_email, args=([email],), daemon=True) for email in email_list]
            #
            # for thread in threads:
            #     thread.start()

            # for item in email_list:
            # send_mail("Новая запись о конференции",
            #           "Доброго времени суток пользователь. Уведомляю Вас, что на сайте Академии МВД была "
            #           "зарегистрирована "
            #           "новая конференция. https://www.nio.amia.by. Ресурс работает в тестовом режиме.",
            #           settings.EMAIL_HOST_USER,
            #           email_list,
            #           fail_silently=False)

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
