from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
from django_markdown.models import MarkdownField


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликован'),
    )
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    # image = models.ImageField()
    body = MarkdownField()
    # body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
# TODO возм вернуть арги
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.slug,]
                       )


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', verbose_name='Пост')
    name = models.CharField(max_length=80, verbose_name='Имя')
    email = models.EmailField(verbose_name='E-Mail')
    body = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, verbose_name='Отображается')

    class Meta:
        ordering = ('created',)
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return '{} прокомментировал {}'.format(self.name, self.post)

