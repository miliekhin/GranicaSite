# pull official base image
FROM python:3.11.3-slim-bullseye

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
#  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN addgroup --system django \
    && adduser --system django --ingroup django

# Requirements are installed here to ensure they will be cached.
COPY kppshka/requirements.txt /requirements.txt
RUN pip3 install --upgrade pip setuptools Twisted[tls,http2]
RUN pip3 install --no-cache-dir -r /requirements.txt \
    && rm /requirements.txt

COPY kppshka/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chown django /entrypoint.sh
COPY --chown=django:django ./kppshka /app

USER django
WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]