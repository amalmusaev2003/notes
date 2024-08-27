FROM python:3.11-slim

RUN mkdir /notes

WORKDIR /notes

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /notes/docker/app.sh

CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]