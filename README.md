[![Python package](https://github.com/joegasewicz/bobtail-logger/actions/workflows/python-package.yml/badge.svg)](https://github.com/joegasewicz/bobtail-logger/actions/workflows/python-package.yml)
[![Upload Python Package](https://github.com/joegasewicz/bobtail-logger/actions/workflows/python-publish.yml/badge.svg)](https://github.com/joegasewicz/bobtail-logger/actions/workflows/python-publish.yml)
# Bobtail Logger
Logging middleware for Bobtail

### Install
```
pip install bobtail-logger
```

### Usage
```python
### Usage
```python
from bobtail_logger import BobtailLogger

app = Bobtail(routes=routes)
app.use(BobtailLogger())

```

Colors
```python
from bobtail_logger import BobtailLogger, Colors

b = BobtailLogger(colors={"color": Colors.RED})
# Errors will always be displayed in `Color.RED`
```