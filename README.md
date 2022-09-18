# Django Stripe API.

Test task for one of the companies. Implements Stripe API with Django.
Main goal is to have endpoint `/item/<item_id>` that will return HTML with item information (from server database) and buy button,
that will fetch another route (API) (`/buy/<item_id)` that will return Stripe Session ID that is used to redirect user to payment screen.

## How to try project?

Project is being deployed to production by GitHub workflow (deploy action). You can try project [here](https://kirillzhosul.site/tests/stripe) (Click!) \
[Test item with id 1!](https://kirillzhosul.site/tests/stripe/item/1)

## Methods.

[`/item/<id>`](https://kirillzhosul.site/tests/stripe/item/): Returns HTML page with item information and button to buy selected item. \
[`/buy/<id>`](https://kirillzhosul.site/tests/stripe/buy/): Returns Stripe Session ID (Actually, item page fetches that endpoint to redirect by own). \
[`/admin/*`](https://kirillzhosul.site/tests/stripe/admin/): Project supports Django-Admin to work with models (Items, Discounts etc). \
[`/`](https://kirillzhosul.site/tests/stripe/): Simple index page.

## How to run?

Project uses Docker, to run simply:
`cd src && docker-compose up`. This will run Docker, Database and server with Gunicorn with Uvicorn workers!

## How to configure?

You can modify environment variables inside `/src/.server.env` file that will be passed to the server with Docker. Look at the Django / App chapters.
`STRIPE_API_PUBLISHABLE_KEY`, `STRIPE_API_SECRET_KEY` is Stripe keys that may be found [here](https://dashboard.stripe.com/test/dashboard).
`URL_PREFIX` is used only for under proxy urls. All other settings refers to default Django fields.

## Technologies.

- Python / Django (No DRF cause main goal is not to make API).
- Gunicorn with Uvicorn workers (ASGI).
- Stripe API for payments.
- Docker / Docker-Compose
- PostgreSQL (with PgBouncer) / Django ORM
- GitHub Workflows (CI/CD)
- Nginx on the server side as the proxy server.
- Ubuntu as the server OS.
