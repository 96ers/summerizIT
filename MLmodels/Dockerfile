FROM python:3.11-slim as python

WORKDIR /ml

# Python will not try to write .pyc file
ENV PYTHONDONTWRITEBYTECODE 1 
# Python does not buffer our console output
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /ml/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /ml/

CMD ["python", "server.py"]