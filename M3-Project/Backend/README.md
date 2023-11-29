
Create virtual env
```bash
python -m venv .venv

```

Save venv dependencies to .txt
```bash
pip freeze > requirements.txt
```

install dep into current env
```bash
pip install -r requirements.txt
```

Deploy app
```bash
gcloud app deploy
```