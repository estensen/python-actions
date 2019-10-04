# python-actions
Test running Python script with GitHub Actions

## Install
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Run
```
(venv) $ python3 create_deployment.py login estensen/login "login app"
Adding deployment file...
{'login': {'docker-image': 'estensen/login', 'description': 'login app'}}
(venv) $ python3 deploy.py
Pipelines in producton: {'id'}
Deploying...
Deployed {'login': {'docker-image': 'estensen/login', 'description': 'login app'}}
```
