# Polizogo Python Lib

It contains varius utilities that may be usefull.

## Enviroment

Add Optional (Extra) Dependencies
```bash
uv add --optional imutils opencv-python numpy
uv sync --extra imutils
uv sync --all-extras
```



## Test

Run the tests !
```bash
uv run pytest
uv run pytest -s # For stdout of the code
uv run --all-extras pytest
```
