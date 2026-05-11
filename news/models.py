from django.db import models

class Article(models.Model):
    title = models.CharField('Название', max_length=50, default='-')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата выпуска')

    def __str__(self):
        return f'ШОК: {self.title}' # отображение записей news aka Article (их заголовков)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'