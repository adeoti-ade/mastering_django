from django.db import models
from uuid import uuid4
from .managers.book import PublishedManager


class BaseModel(models.Model):
    """
    This is an abstract base that defines the common id, created_at and updated_at fields
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NameModel(BaseModel):
    """
    This is another abstract base that inherits  from the BaseModel. It defines first_name and
    last_name field for models that requires it while inheriting fields from the BaseModel
    """
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Publisher(NameModel):
    """
    This class is the model that defines the publisher table. it inherits from the NameModel to include first_name,
    last_name, id, created_at and updated_at then add additional fields
    """
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    state_province = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Author(NameModel):
    """
    This class is the model that defines the author table. it inherits from the NameModel to include first_name,
    last_name, id, created_at and updated_at then add additional fields
    """
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(BaseModel):
    """
    This class is the model that defines the book table table.
    """
    title = models.CharField(max_length=100, null=True, blank=True)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title


class Messages(Book):
    """
    This is a multi table inheritance model. it defines gospel messages that are also books,
    but have extra fields not pertaining to normal books.
    """
    case_study = models.CharField(max_length=100, null=True, blank=True)
    references = models.CharField(max_length=200, null=True, blank=True)

    @property
    def get_references(self):
        return self.references.split(",")
