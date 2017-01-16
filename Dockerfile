FROM python:2-onbuild
RUN apt-get update -y

EXPOSE 5000

CMD ["gunicorn", "--bind=0.0.0.0:5000", "app:app", "--access-logfile=-", "--log-level=info"]
