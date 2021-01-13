FROM python:3.7-alpine
MAINTAINER hanifalisohag@gmail.com
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /app
COPY ../.. /app
ENTRYPOINT ["python"]
CMD ["app.py"]