# syntax=docker/dockerfile:1
FROM python:3.10.7-alpine

# Disable python buffering and bytecode *.pyc compiling. 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Project directory.
WORKDIR /srv/www

# Install requirements.
COPY requirements.txt /srv/www/
RUN pip install --upgrade pip
RUN pip install --upgrade --no-cache-dir -r requirements.txt

# Copy whole project.
COPY . /srv/www/

# Run project.
#CMD ["python", "manage.py", "runserver"]
# 1) This is native run.
# 2) Launching is done by docker compose (a bit weird for now).