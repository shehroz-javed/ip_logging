FROM python:3.10.14-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /ip_logging
WORKDIR /ip_logging

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /ip_logging/
# RUN chmod +x manage.py

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
