<<<<<<< HEAD
FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 pyarrow

WORKDIR /app

COPY ingest_taxi_data.csv.py ingest_taxi_data.csv.py

ENTRYPOINT [ "python", "-u", "ingest_taxi_data.csv.py" ]
=======
FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY ingest_data.py ingest_data.py 

ENTRYPOINT [ "python", "ingest_data.py" ]
>>>>>>> class/main
