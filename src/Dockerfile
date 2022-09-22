# syntax=docker/dockerfile:1
FROM python:3.10.7-alpine

# Disable python buffering and bytecode *.pyc compiling. 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Project directory.
WORKDIR /srv

# Install requirements.
COPY requirements.txt /srv/
RUN pip install --upgrade pip
RUN pip install --upgrade --no-cache-dir -r requirements.txt

# Copy whole project.
COPY . /srv/

# Run project with Gunicorn process manager.
# By default, Gunicorn will use Uvicorn ASGI workers.
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
#CMD ["gunicorn", "project.asgi:application", "-c", "gunicorn.conf.py"]