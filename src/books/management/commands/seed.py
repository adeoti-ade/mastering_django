from django.core.management.base import BaseCommand
from books.management.factory.book import PublisherFactory


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--publisher',
                            default=200,
                            type=int,
                            help='The number of fake publisher to create.')

    def handle(self, *args, **options):
        for _ in range(options['publisher']):
            PublisherFactory.create()
