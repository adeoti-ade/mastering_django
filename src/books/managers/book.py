from django.db import models


class PublishedManager(models.Manager):
    """
    This class inherits from the django default manager and overwrites how the default get_queryset behaves
    """
    def get_queryset(self):
        """
        :return: instance with publication date being False
        """
        return super().get_queryset().exclude(publication_date__isnull=False)
