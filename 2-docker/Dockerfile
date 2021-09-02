FROM python:3.8.1-slim-buster as app
LABEL maintainer="ERICK GUBI <egubi@vmware.com>"

WORKDIR /main

COPY requirements.txt requirements.txt
ENV BUILD_DEPS="build-essential" \
    APP_DEPS="curl libpq-dev"

RUN pip install -r requirements.txt 

RUN apt-get update \
  && apt-get install -y ${BUILD_DEPS} ${APP_DEPS} --no-install-recommends \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /usr/share/doc && rm -rf /usr/share/man \
  && apt-get purge -y --auto-remove ${BUILD_DEPS} 

COPY . .

EXPOSE 8000

CMD ["gunicorn","-b","0.0.0.0:8000","--access-logfile","-","main.app:app"]
