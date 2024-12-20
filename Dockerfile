FROM python:3.13.0

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "./manage.py", "runserver", "0.0.0.0:80"]