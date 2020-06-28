from django.db import models


class Tag(models.Model):
    name = models.TextField(null=True, verbose_name='Тематический раздел')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class ArticleTags(models.Model):
    article = models.ForeignKey("Article", on_delete=models.CASCADE, )
    scope = models.ForeignKey("Tag", on_delete=models.CASCADE, )
    main = models.BooleanField(default=False, verbose_name='Основной раздел')


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    scopes = models.ManyToManyField(Tag, through=ArticleTags, verbose_name='Разделы')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
