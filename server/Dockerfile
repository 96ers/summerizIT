FROM python:3.11-slim as requirements-stage

WORKDIR /tmp

# Python will not try to write .pyc file
ENV PYTHONDONTWRITEBYTECODE 1 
# Python does not buffer our console output
ENV PYTHONUNBUFFERED 1

# Install poetry
RUN pip install poetry

# Copy poetry's files config
COPY ./pyproject.toml ./poetry.lock /tmp/

# Generate requirements.txt
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM python:3.11-slim as python3.11

# main workdir
WORKDIR /server

# Copy requirements.txt into /server directory
COPY --from=requirements-stage /tmp/requirements.txt /server/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

# Copy code to /server directory
COPY . /server/

# Copy all variables
RUN cp /server/.env.example /server/.env

CMD [ "python", "main.py" ]