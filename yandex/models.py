from django.db import models

class Point(models.Model):
    title = models.CharField("Название", max_length=1000)
    comment = models.CharField("Описание", max_length=1000, blank=True)
    url = models.CharField("Ссылка", max_length=1000)
    mode_keywords = models.BooleanField('Использовать ключевые слова по количеству ("Общее количество" не будет учитываться)', )
    keywords = models.TextField("Ключевые слова (1.слово-процент)", )
    total_number = models.IntegerField("Общее количество",)
    start_time = models.TimeField("Время начала", )
    end_time = models.TimeField("Время окончания", )
    activate = models.BooleanField("Активен", )
    created_at = models.DateTimeField("Время создания", auto_now_add=True)
    updated_at = models.DateTimeField("Время последнего редактирования", auto_now=True)
    pf1 = models.PositiveSmallIntegerField('Меню-%', default=0,)
    pf2 = models.PositiveSmallIntegerField('Товары и услуги-%',default=0,)
    pf3 = models.PositiveSmallIntegerField('Новости-%',default=0,)
    pf4 = models.PositiveSmallIntegerField('Фото-%',default=0,)
    pf5 = models.PositiveSmallIntegerField('Отзывы-%',default=0,)
    pf6 = models.PositiveSmallIntegerField('Посмотрел истории-%',default=0,)
    pf7 = models.PositiveSmallIntegerField('Посмотрел график работы-%',default=0,)
    pf8 = models.PositiveSmallIntegerField('Перешел на сайт-количество',default=0,)
    pf9 = models.PositiveSmallIntegerField('Построил маршрут-количество',default=0,)
    pf10 = models.PositiveSmallIntegerField('Позвонил-количество',default=0,)
    pf11 = models.PositiveSmallIntegerField('Посмотрел входы-количество',default=0,)
    
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Точка"
        verbose_name_plural = "Точки"
