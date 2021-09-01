FROM python:3.8.1-slim-buster as app
LABEL maintainer="ERICK GUBI <egubi@vmware.com>"

WORKDIR /main

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

COPY . .

EXPOSE 8000

CMD ["gunicorn","-b","0.0.0.0:8000","--access-logfile","-","main.app:app"]
