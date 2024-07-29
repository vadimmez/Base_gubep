from django.db import models


class Country(models.Model):
    country = models.CharField(max_length=255, verbose_name="Страна")

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ("-id",)


class EventStatus(models.Model):
    status = models.CharField(max_length=255, verbose_name="Статус мероприятия")

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус мероприятия'
        verbose_name_plural = 'Статусы мероприятия'
        ordering = ("-id",)


class ParticipantStatus(models.Model):
    status = models.CharField(max_length=255, verbose_name="Статус участника")

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус участника'
        verbose_name_plural = 'Статусы участников'
        ordering = ("-id",)


class Conference(models.Model):
    naimenovanie = models.CharField(max_length=250, verbose_name="Наименование")
    uchregdenie = models.CharField(max_length=250, verbose_name="Учреждение")
    strana = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Страна")
    status_meropriatia = models.ForeignKey(EventStatus, on_delete=models.SET_NULL, verbose_name="Статус мероприятия",
                                           blank=True, null=True)
    status_uchastnikov = models.ForeignKey(ParticipantStatus, on_delete=models.SET_NULL,
                                           verbose_name="Статус участников",
                                           blank=True, null=True)
    data_podachi = models.DateField(verbose_name="Дата подачи")
    data_provedenia = models.DateField(verbose_name="Дата проведения")
    primechanie = models.CharField(max_length=250, verbose_name="Примечание")
    document = models.FileField(upload_to='documents/', blank=True, null=True, verbose_name="Документ")

    def __str__(self):
        return self.naimenovanie

    class Meta:
        verbose_name = 'Конференция'
        verbose_name_plural = 'Конференции'
        ordering = ("-id",)


class Podpiska(models.Model):
    email = models.EmailField(verbose_name="E-mail")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ("-id",)
