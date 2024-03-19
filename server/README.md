## Go to the server directory

```bash
cd server
```

## Environment Variables

ssCopy the example environment file to a new file called `.env`:

```bash
cp .env.example .env
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
pytest ...... (TODO)
```
