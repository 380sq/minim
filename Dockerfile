FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
COPY . /var/www/
RUN pip install -r /var/www/requirements.txt