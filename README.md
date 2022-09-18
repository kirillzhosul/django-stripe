# Django Stripe API.

Test task for one of the companies. Implement Stripe API with Django.
Main goal is to have endpoint `/item/<item_id>` that will return HTML with item information (from server database) and buy button,
that will fetch another route (API) (`/buy/<item_id)` that will return Stripe Session ID that is used to redirect user to payment screen.
[Test item with id 1!](https://kirillzhosul.site/tests/stripe/item/1)

## How to try project?

Project is deployed under my domain with test cases. You can try project [here](https://kirillzhosul.site/tests/stripe) (Click!) \
Notice that deployed version should not give you access to the admin, this is simple showcase to try project without configuring it.

## Methods.

[`/item/<id>`](https://kirillzhosul.site/tests/stripe/item/): Returns HTML page with item information and button to buy selected item. \
[`/buy/<id>`](https://kirillzhosul.site/tests/stripe/buy/): Returns Stripe Session ID (Actually, item page fetches that endpoint to redirect by own). \
[`/admin/*`](https://kirillzhosul.site/tests/stripe/admin/): Project supports Django-Admin to work with models (Items, Discounts etc).

## How to run?

Project uses Docker, to run simply:
`cd src && docker-compose up`. Notice that if you try to simply run `python manage.py runserver` this will just fail!

## How to configure?

You can modify environment variables inside `/src/.env` file that will be passed to the server with Docker.

## Technologies.

- Python / Django (No DRF cause main goal is not to make API) / Gunicorn (with Uvicorn)
- Stripe API (Under test mode)
- Docker / Docker-Compose (Requirements of the test tasks)
- PostgreSQL (with PgBouncer) / Django ORM (Inside Docker)
- GitHub Workflows (CI/CD, Should be implemented later)
