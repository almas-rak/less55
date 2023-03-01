from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoice(TextChoices):
    ACTIVE = 'ACTIVE', 'Активная'
    NOT_ACTIVE = 'NOT_ACTIVE', 'Неактивная'


# Create your models here.
class Article(models.Model):
    status = models.CharField(verbose_name='Статус', choices=StatusChoice.choices, max_length=20,
                              default=StatusChoice.ACTIVE)
    title = models.CharField(max_length=200, null=False, verbose_name="Заголовок")
    text = models.TextField(max_length=3000, null=False, verbose_name="Текст")
    author = models.CharField(max_length=200, null=False, verbose_name="Автор")
    is_deleted = models.BooleanField(verbose_name='удалено', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def __str__(self):
        return f"{self.author} - {self.title}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey('Article', verbose_name='Статья', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(max_length=3000, null=False, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")

    def __str__(self):
        return f'{self.text} - {self.created_at}'
