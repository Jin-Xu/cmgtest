FROM python:3.7-alpine
ADD . /app
RUN pip install -e /app
ENV FLASK_APP=/app/cmgtest/app.py
ENV FLASK_ENV=development
CMD flask run --host=0.0.0.0
