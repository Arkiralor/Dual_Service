FROM python:slim-buster
FROM golang:1.14-buster

WORKDIR /dual_service

COPY requirements.txt .
# RUN python3.8 -n venv env
# RUN source env/bin/activate
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

## DATABASE SETTINGS
ENV PGDATABASE = "sample_db"
ENV PGUSER = "prithoo"
ENV PGPASSWORD = "password"
ENV PGHOST = "localhost"
ENV PGPORT = "5432"

## SITE SETTINGS
ENV SECRET_KEY = "279925a82fc67a9b4dace78505dcde702266359b277154e7066fba5cf71381e2"
ENV DEBUG = true
ENV LANGUAGE_CODE = 'en-us'
ENV TIME_ZONE = 'Asia/Kolkata'
ENV USE_I18N = true
ENV USE_TZ = true

## External APIs
ENV GO_BASE_URL = "http://localhost:7000/api/v1/"
ENV PRIME_LIST_URL = "prime_list"
ENV FIND_FACTORS_URL = "find_factors"
ENV PRIME_FACTORS_URL = "prime_factors"
ENV INT_TO_BINARY_URL = "int_to_binary"
ENV BINARY_TO_INT_URL = "binary_to_int"
ENV RANDOM_BINARY_URL = "random_binary"
ENV FIBONACCI_URL = "fibonacci"
ENV REG_ARITH_SERIES_URL = "arith_series"
ENV REG_GEO_SERIES_URL = "geo_series"

COPY Django_SC .
COPY Gorilla_SC .

RUN chmod +x startup_dj.sh
RUN chmod +x startup_go.sh

RUN ./startboth.sh


