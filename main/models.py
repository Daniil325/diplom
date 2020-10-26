from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField("Название организации", max_length=200)
    description = models.TextField('О компании')
    adress = models.CharField("Адрес организации", max_length=200)
    director = models.CharField("Директор организации", max_length=200)
    phone_number = models.CharField("Телефон", max_length=200)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    video = models.FileField(upload_to='filesInput/')
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse('main:main_detail',
                           args=[self.id, self.slug])

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Автор комментария', blank = True, null = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name='Статья', blank = True, null = True,related_name='comments_post')
    create_date = models.DateTimeField(default=timezone.now)
    text = models.TextField(verbose_name='Текст комментария')
