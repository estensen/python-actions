# python-actions
Deploy pipelines automatically with GitHub Actions

## Deploy
Add deployment (currently dummy config) to `pipeline.yaml`:
```
(venv) $  python3 create_deployment.py auth3 estensen/hello.py "hello world app"
Adding deployment file...
Deployment created!
{'auth3': {'docker-image': 'estensen/hello.py', 'description': 'hello world app'}}
```

Commit, push and create a pull request with `pipeline.yaml`. An Action will run `deploy.py` which will put the pipeline into production and move the configuration to `pipelines.yaml` so all pipelines can be recreated with one deployment later if necessary.

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

## Test locally
```
$ pytest
============================ test session starts =============================
...
collected 1 item

test_hello.py .                                                        [100%]

============================= 1 passed in 0.01s ==============================
```
