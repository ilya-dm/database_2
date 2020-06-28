from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Tag, ArticleTags, Article


class ArticleTagsInlineInlineFormset(BaseInlineFormSet):
    def clean(self):
        set_main = False
        for form in self.forms:
            main = form.cleaned_data.get('main')
            if main:
                if set_main:
                    raise ValidationError('Основной раздел может быть только один!')
                set_main = True
        if not set_main:
            raise ValidationError('Укажите основной раздел!')
        return super().clean()


class ArticleTagsInline(admin.TabularInline):
    model = ArticleTags
    formset = ArticleTagsInlineInlineFormset

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagsInline]
