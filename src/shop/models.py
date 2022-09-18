from django.db import models


class Item(models.Model):
    """Item model that represents a single item on the site. Like storage."""

    item_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=64, verbose_name="Item name to display"
    )  # About ~=64 characters long.
    description = models.TextField(verbose_name="Description of item to display")
    # May be decimal field.
    price = models.IntegerField(verbose_name="Price of item for checkout")
