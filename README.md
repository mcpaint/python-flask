# python-flask

## Platform
- Python3
- Flask

## venv
```bash
python3 -m venv ./venv
```

## venv activate / deactivate
```bash
# activate
source ./venv/bin/activate
# deactivate
deactivate
```
 

## Install Python Package
``` bash
pip install -r requirements.txt
```

## Start
``` bash
# phase : dev, alpha, sandbox, beta, real
# default: dev
export FLASK_CONFIGURATION=dev; python run.py
```