"""
    Service to work with stripe.
"""
import stripe


def create_stripe_session(
    secret_key: str,
    product_name: str,
    price: int,
    quantity: int = 1,
    currency: str = "usd",
) -> stripe.checkout.Session:
    """
    Creates and returns stripe session object.
    Supports only ONE line item (No more!)
    """
    stripe.api_key = secret_key
    return stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": currency,
                    "product_data": {
                        "name": product_name,
                    },
                    "unit_amount": price,
                },
                "quantity": quantity,
            }
        ],
        # Temporary for no env support!
        success_url=f"https://kirillzhosul.site/tests/stripe/item/{item_id}",
        cancel_url=f"https://kirillzhosul.site/tests/stripe/item/{item_id}",
        mode="payment",
    )
