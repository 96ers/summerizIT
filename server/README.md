# Run server locally
## Go to the server directory

```bash
cd server
```

## Environment Variables

Copy the `.env.example` file to `.env` and update the values as per your needs.:

```bash
cp .env.example .env
```

## Run MySQL and phpmyadmin containers
```bash
sudo docker-compose up -d
```

## Install Dependencies

Install development dependencies

```bash
poetry install
```

Install production dependencies

```bash
poetry install --only main
```

## Add new dependency

To add a new package:

```bash
poetry add <package>
```

To add a new development package:

```bash
poetry add <package> --group dev
```

## Dependency Lockfile

Check lockfile

```bash
poetry check --lock
```

Update Lockfile

```bash
poetry lock
```

## Running server

```bash
python main.py
```

# Run server via Docker

Make sure you have [Docker](https://docs.docker.com/engine/install/), [docker compose](https://docs.docker.com/compose/install/) in your machine.

## Copy the `.env.example` into `.env`
```bash
cp .env.example .env
```

To run server via Docker, you need to specify environment variables in .env file
`MYSQL_HOST`=mysql

And unbine the line `host='0.0.0.0'` in `main.py`

## Build and run image

This is only for the first time you deploy server via docker

```bash
sudo docker compose up --build
```

## Run server

```bash
sudo docker compose up
```

Go to [0.0.0.0:9999](http://0.0.0.0:9999)

## Code Formatting and Linting

Check code formatting

```bash
black ./ --check
isort ./ --profile black --check
```

Format code

```bash
black ./
isort ./ --profile black
```

Linting

```bash
pylint ./src
```

## Testing

```bash
pytest 
```
