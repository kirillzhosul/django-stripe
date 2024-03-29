from django.db import models


class Item(models.Model):
    """Item model that represents a single item on the site. Like storage."""

    item_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=64, verbose_name="Item name to display"
    )  # About ~=64 characters long.
    description = models.TextField(verbose_name="Description of item to display")
    # May be decimal field.
    price = models.IntegerField(
        verbose_name="Price of item for checkout (/100!) 250 => 2.5$"
    )

    def get_display_price(self) -> float:
        """Returns display price (as model price is stripe-like format price)"""
        return self.price / 100

    def get_display_title(self) -> str:
        return f"{self.name} (Item №{self.item_id})"

    def __str__(self):
        return self.get_display_title()

    def __repr__(self):
        return self.get_display_title()


# May be implemented later:
#
# Item.currency for storing currency of the item.
#
# class Order(models.Model):
#   """Order model that contains different items to buy."""
#
# class Discount(models.Model):
# """Discount model for the Order."""
#
# class Tax(models.Model): pass
# """Tax model for the Order."""
