# Project generation tutorial

## Create distribution

```bash
python setup.py sdist bdist_wheel
```

## Install it

```bash
python -m pip install --upgrade --force-reinstall dist/sqt-*.*.*-py3-none-any.whl
```

or 

```bash
python -m pip install --upgrade -e .
```

replace * with the version you are using

## Publish it on pypi (only administrator is allowed to do this)

python -m twine upload dist/*

