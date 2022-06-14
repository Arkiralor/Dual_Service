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

### Mathematical Functions Registered

1. _Find all Prime Numbers less than or equal to a given number._
2. _Find all Factors of a given number._
3. _Find all Prime Factors of a given number._
4. _Convert a given base-10 Integer into its base-2 counterpart._
5. _Convert a given base-2 Number into its base-10 counterpart._
6. _Generate a random base-2 number, given the number of Bits._
7. _Generate 'n' terms of the Fibonacci Sequence._
8. _Generate 'n' terms of a Regular Arithmetic Progression, given the Starting Value and the Common Difference._
9. _Generate 'n' terms of a Regular Geometric Progression, given the Starting Value and the Common Ratio._
10. _Generate the Coordinate List of the parabolic path through 2D space, followed by a projectile, given the Angle of Projection, Initial Velocity of Projection and the Height of Projection._

## Simplified Algorithm

![Block Diagram Flowchart for the Algorithm](https://i.imgur.com/q0wddgC.png "Algorithm for the Application Set")

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
4. `pip install pip-tools`
5. `pip-compile Django_SC/requirements.in`
6. `pip install -r Django_SC/requirements.txt`
7. `./Django_SC/manage.py makemigrations`
8. `./Django_SC/manage.py migrate`
9. `./Django_SC/manage.py createsuperuser`
10. `cd Gorilla_SC/cmd/main`
11. `go build`
12. `cd ../../..`
13. `./statup_dj.sh`
14. Open another terminal and run `./startup_go.sh`

## Environments

The `.env` file formats for both the Django and Go environments.

### Django

```ENV
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
BINARY_TO_INT_URL = [string]
RANDOM_BINARY_URL = [string]
FIBONACCI_URL = [string]
REG_ARITH_SERIES_URL = [string]
REG_GEO_SERIES_URL = [string]
PROJECTILE_PATH_2D_URL = [string]
```

### Go

Currently, there are no environment variables required for the Go environment.

```.env
```

## Documentation

Link: [Postman Docs](https://documenter.getpostman.com/view/17779018/Uyr4JKHS)
