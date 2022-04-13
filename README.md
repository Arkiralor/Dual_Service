# Django Rest API that uses Go via Gorilla Microservice

A Django Rest API that uses Go via Gorilla Microservice to execute mathematically intensive tasks.

## Installation

1. `python -m venv env`
2. `source env/bin/activate`
3. `python -m pip install --upgrade pip`
4. `pip install -r requirements.txt`
5. `./web_application_8000/manage.py makemigrations`
6. `./web_application_8000/manage.py migrate`
7. `./web_application_8000/manage.py createsuperuser`
8. `cd microservice_7000/cmd/main`
9. `go build`
10. `cd ../..`
11. `./statup_dj.sh`
12. Open another terminal and run `./startup_go.sh`

## Documentation

Link: [Postman Docs](https://documenter.getpostman.com/view/17779018/Uyr4JKHS)
