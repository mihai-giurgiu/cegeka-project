# CV Data Flask REST API

## How to start

### CLI

#### Linux
```sh
FLASK_APP=cegeka_restapi.py flask [education|experience|personal]
```

#### Windows
```sh
py -m flask [education|experience|personal]
```

### REST API

#### Linux
```sh
FLASK_APP=cegeka_restapi.py flask run
```

#### Windows
```sh
py .\cegeka_restapi.py

curl http://127.0.0.1:5000/[education|experience|personal]
```
