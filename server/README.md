Install conda environment

```bash
conda env create -f environment.yml
```

Activate conda environment

```bash
conda activate venv
```

Install dev dependencies

```bash
poetry install
```

Install product dependencies

```bash
poetry install --only main
```

Add package

```bash
poetry add <package>
```

Add dev package

```bash
poetry add <package> --group dev
```

Start server

```bash
python main.py
```

Check format code

```bash
black ./ --check
isort ./ --profile black --check
```

Format code

```bash
black ./
isort ./ --profile black
```

Check lockfile

```bash
poetry check --lock
```

Lockfile

```bash
poetry lock
```

Linter

```bash
pylint ./src
```

Test

```bash
pytest ...... (TODO)
```
