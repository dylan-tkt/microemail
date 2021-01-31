# Sample Mail Microservice

FastAPI 0.63

## Introduction

This is just a quick test project to see what FastAPI can do. Note that this does not make any DB calls.

### Installation

Set some basic SMTP info first:

```sh
export SMTP_PASSWORD=sdasdasd SMTP_USERNAME=123123 SMTP_SERVER=whatever.com EMAIL_PORT=2525
```

Then clone the repo and paste these commands and it should run.

```sh
pipenv install
pipenv run uvicorn main:app --reload
```

### Deployment

A simple deployment (which additionally would need Circus or Gunicorn or Supervisor or some other other process manager):

Clone first of course, then create a .env file in the project directory with the SMTP aliases described in the installation step.

```shell
pipenv install
uvicorn --uds /tmp/uvicorn.sock --proxy-headers --env-file $(pwd)/.env main:app &
```

Check you have a file at this point -> `ls /tmp/uvicorn.sock`

Nginx file:

```nginx
upstream uvicorn {
    server unix:/tmp/uvicorn.sock;
}

server {
    server_name whatever-url.com;
    listen 80;

    charset utf-8;
    client_max_body_size 1M;

    location / {
        proxy_pass http://uvicorn;
        proxy_set_header Host $http_host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
        proxy_buffering off;
    }
}
```
