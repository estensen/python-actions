# python-actions
Test running Python script with GitHub Actions

## Install locally
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ pre-commit install
```

## Run locally
```
(venv) $ python3 create_deployment.py login estensen/login "login app"
Adding deployment file...
{'login': {'docker-image': 'estensen/login', 'description': 'login app'}}
(venv) $ python3 deploy.py
Pipelines in producton: {'id'}
Deploying...
Deployed {'login': {'docker-image': 'estensen/login', 'description': 'login app'}}
```

## Deploy
Add deployment to `pipeline.yaml`:
```
(venv) $ python3 create_deployment.py login estensen/login "login app"
Adding deployment file...
```

Commit and push `pipeline.yaml`. An Action will run `deploy.py` which will put the pipeline into production and move the configuration to `pipelines.yaml` so all pipelines can be recreated with one deployment.
