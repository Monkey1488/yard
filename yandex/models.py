from django.db import models

class Point(models.Model):
    
    title = models.CharField("Название", max_length=1000)
    url = models.CharField("Ссылка", max_length=1000)
    keywords = models.TextField("Ключевые слова (слово-%", )
    total_number = models.IntegerField("Общее количество",)
    start_time = models.TimeField("Время начала", )
    end_time = models.TimeField("Время окончания", )
    activate = models.BooleanField("Активен", )
    created_at = models.DateTimeField("Время создания", auto_now_add=True)
    updated_at = models.DateTimeField("Время последнего редактирования", auto_now=True)
    # pf1 = models.IntegerField(max_length=3)
    # pf2 = models.IntegerField(max_length=3)
    # pf3 = models.IntegerField(max_length=3)
    # pf4 = models.IntegerField(max_length=3)
    # pf5 = models.IntegerField(max_length=3)
    
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Точка"
        verbose_name_plural = "Точки"
