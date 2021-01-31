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
