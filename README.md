# Django Rest API that uses Go via Gorilla Microservice

A Django Rest API that uses Go via Gorilla Microservice to execute mathematically intensive tasks.

## Working Theory

Python is a great language for writing web applications. However, it is not a great language for writing complex mathematical algorithms. Go, on the other hand, is a great language for writing complex mathematical algorithms as it is compiled to native code; so even if the time complexity of the algorithm remains the same, the performance of the algorithm will be much better in
the real world.

As Go also has a built-in HTTP server, it is possible to write a REST API in Go. We will use Gorilla/Mux to build our 
Web APIs.

The Django Web-Apllication that we will build in Python will be used for basic tasks, such as:

- User Authentication
- User Registration
- Caching Results, etc.

The Go Web-Application that we will build in Go will be used for more complex tasks, such as:

- Computing the list of Prime Numbers in a given range.
- Computing the Factors of a given number.
- Computing the Prime Factors of a given number, etc.

## Simplified Algorithm

![Block Diagram Flowchart for the Algorithm](https://imgur.com/a/bZPdv4O)

In our Django application, we will have models to store the returned data from the Go Web-Application.

If a user inputs a query to a particular path in the Django app, it will first search the model for the query and return the result.

If however, the query is not found in the model, it will then hit the Go Web-Application and return the result.

In this way, the query is returned with the least possible time-delay and the highest possible performance.

For a given request to the Django API:

```python
def find_something(request):
    query = request.GET.get('query')
    qryset = SomeModel.objects.filter(query=query).first()
    if not qryset:
        resp = SomeClass.query_handler(query)
        resp_deserialized = SomeSerializer(data = resp)
        resp_deserialized.save()
        return Response(
            resp_deserialized.data,
            status = 200
        )
    serialized = SomeSerializer(qryset)
    return Response(
        serialized.data,
        status = 200
    )
    
```

The `query_handler()` for its part executes the following steps:

```python
def query_handler(query):
    if...else(task in query)
    url = task.url
    resp = SameClass.make_request(url, params = query, headers)
    return resp.json()
```


## Setup

1. `python -m venv env`
2. `source env/bin/activate`
3. `python -m pip install --upgrade pip`
4. `pip install -r requirements.txt`
5. `./web_application_8000/manage.py makemigrations`
6. `./web_application_8000/manage.py migrate`
7. `./web_application_8000/manage.py createsuperuser`
8. `cd microservice_7000/cmd/main`
9. `go build`
10. `cd ../../..`
11. `./statup_dj.sh`
12. Open another terminal and run `./startup_go.sh`

## Environments

The `.env` file formats for both the Django and Go environments.

### Django

```.env
## DATABASE SETTINGS
PGDATABASE = [string]
PGUSER = [string]
PGPASSWORD = [string]
PGHOST = [string]
PGPORT = [string]

## SITE SETTINGS
SECRET_KEY = [string]
DEBUG = true/false
LANGUAGE_CODE = [string]
TIME_ZONE = [string]
USE_I18N = true/false
USE_TZ = true/false

## External APIs
GO_BASE_URL = [string]
PRIME_LIST_URL = [string]
FIND_FACTORS_URL = [string]
PRIME_FACTORS_URL = [string]
INT_TO_BINARY_URL = [string]
RANDOM_BINARY_URL = [string]
RANDOM_BINARY_URL = [string]
```

### Go

Currently, there are no environment variables required for the Go environment.

```.env
```

## Documentation

Link: [Postman Docs](https://documenter.getpostman.com/view/17779018/Uyr4JKHS)
