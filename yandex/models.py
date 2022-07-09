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
    pf1 = models.CharField('Меню', default="0", max_length=4)
    pf2 = models.CharField('Товары и услуги', default="0", max_length=4)
    pf3 = models.CharField('Новости',default="0", max_length=4)
    pf4 = models.CharField('Фото',default="0", max_length=4)
    pf5 = models.CharField('Отзывы',default="0", max_length=4)
    pf6 = models.CharField('Посмотрел истории',default="0", max_length=4)
    pf7 = models.CharField('Посмотрел график работы',default="0", max_length=4)
    pf8 = models.CharField('Перешел на сайт',default="0", max_length=4)
    pf9 = models.CharField('Построил маршрут',default="0", max_length=4)
    pf10 = models.CharField('Позвонил',default="0", max_length=4)
    pf11 = models.CharField('Посмотрел входы',default="0", max_length=4)
    
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Точка"
        verbose_name_plural = "Точки"
