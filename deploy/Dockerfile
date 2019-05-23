FROM python:3.6

WORKDIR /root

RUN mkdir -p /root/www/imhio

WORKDIR www/imhio

COPY requirements.txt /root/www/imhio/requirements.txt

RUN pip install -r requirements.txt

COPY . /root/www/imhio

CMD ["./docker-entrypoint.sh"]
