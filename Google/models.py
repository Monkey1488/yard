from django.db import models

class GPoint(models.Model):
    title = models.CharField("Название", max_length=1000)
    comment = models.CharField("Описание", max_length=1000, blank=True)
    url = models.CharField("Ссылка", max_length=1000)
    mode_keywords = models.BooleanField('Использовать ключевые слова по количеству', )
    keywords = models.TextField("Ключевые слова (1.слово-процент)", )
    total_number = models.IntegerField("Общее количество",)
    start_time = models.TimeField("Время начала", )
    end_time = models.TimeField("Время окончания", )
    activate = models.BooleanField("Активен", )
    created_at = models.DateTimeField("Время создания", auto_now_add=True)
    updated_at = models.DateTimeField("Время последнего редактирования", auto_now=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Точка"
        verbose_name_plural = "Точки"
