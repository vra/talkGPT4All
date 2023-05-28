Build package and publish to pypi:
```bash
rm -rf dist/*
python3 -m build
python3 -m twine upload  dist/*
```
