from django.db import models

# Create your models here.
# from django.utils import timezone
# import datetime
#
# # Create your models here.

class Photo(models.Model):
    photo_file = models.ImageField(upload_to='imgs', max_length=50, default='imgs/def.jpg')


class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length = 200)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')
    photo = models.ForeignKey(Photo, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.article_title

#     def recently_pub(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days = 7)

    class Meta():
        verbose_name = 'Стих'
        verbose_name_plural = 'Стихи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('Автор комментария', max_length = 50)
    comment_text = models.CharField('Комментарий', max_length = 200)

    def __str__(self):
        return self.author_name

    class Meta():
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'