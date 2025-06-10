FROM python:3.11-slim

WORKDIR /app
COPY . ./

RUN pip install -r requirements/production.txt

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
