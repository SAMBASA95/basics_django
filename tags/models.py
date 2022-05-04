from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# from basics.storefront.store.models import Product
# Don't import Product model from store models.py instead


# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=300)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product)
    # Importing the Product model from store app will be a bad way connection between
    # two app models / database because it can get deleted or can get change in future

    # To do so we need a generic way of connecting two apps
    # in which we use contentType

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
