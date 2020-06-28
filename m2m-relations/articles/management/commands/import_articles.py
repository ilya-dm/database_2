import json

from django.core.management.base import BaseCommand
from django.utils import text

from articles.models import Article


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('articles.json', encoding='utf-8') as jsonfile:
            articles = json.load(jsonfile)
            for line in articles:

                article = Article(image=line['fields']['image'],
                                  title=line['fields']['title'],
                                  text=line['fields']['text'],
                                  published_at=line['fields']['published_at'])
                article.save()

