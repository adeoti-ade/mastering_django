import factory
import factory.django
from books.models import Publisher, Book

import factory

factory.Faker._DEFAULT_LOCALE = 'en_US'


class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publisher

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    address = factory.Faker('address')
    state_province = factory.Faker('state')
    country = factory.Faker('country')
    website = factory.Faker('url')


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publisher

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    address = factory.Faker('address')
    state_province = factory.Faker('state')
    country = factory.Faker('country')
    website = factory.Faker('url')


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker("title")
    authors = factory.SubFactory(AuthorFactory)
    publisher = factory.SubFactory(PublisherFactory)


class PublisherWithBookFactory(PublisherFactory):

    @factory.post_generation
    def players(obj, create, extracted, **kwargs):
        """
        If called like: PublisherFactory(book=4) it generates a Publisher with 4
        books.  If called without `books` argument, it generates a
        random amount of books for this team
        """
        if not create:
            # Build, not create related
            return

        if extracted:
            for n in range(extracted):
                BookFactory(team=obj)
        else:
            import random
            number_of_units = random.randint(1, 10)
            for n in range(number_of_units):
                BookFactory(team=obj)
