# Data Engineering project 1 - Data Modelling with Postgres

By Alessio Rea

==============================

You need to have Python 3.6.3 installed for this project

# General explanation

## 1. Purpose of the project

The purpose of the project is to build an ETL pipeline which transfers data from files in two local directories into tables in Postgres using Python and SQL. Data in postgres is modelled according to a star schema with fact and dimension tables for easy and fast analysis.


## 2. Database schema design and ETL pipeline

In this project, initial dataset comes from two json files :

- First : Song Dataset
    
    Here are filepaths to two files that could be found in such a dataset :

    ```
    song_data/A/B/C/TRABCEI128F424C983.json
    song_data/A/A/B/TRAABJL12903CDCF1A.json
    ```

    Here is an example of what a single song file may looks like :

    ```
    {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
    ```

- Second : Log Dataset
    
    Here are filepaths to two files that could be found in such a dataset :

    ```
    log_data/2018/11/2018-11-12-events.json
    log_data/2018/11/2018-11-13-events.json
    ```
    
    Those files contain the following features : 'artist', 'auth', 'firstName', 'gender', 'itemInSession', 'lastName',
       'length', 'level', 'location', 'method', 'page', 'registration',
       'sessionId', 'song', 'status', 'ts', 'userAgent', 'userId'


## 3. Example queries and results for song play analysis

Provide example queries and results for song play analysis


# Project Organization 
----------------------

    ├── README.md               <- The top-level README for users and developers using this project.
    ├── create_tables.py        <- Python script allowing to create database, create / drop tables with appropriate schema
    ├── etl.ipynb               <- Notebook for step by step testing
    ├── requirements.txt        <- install psycopg2 for local use
    ├── sql_queries.py          <- SQL queries
    ├── test.ipynb              <- unitary tests for creation, deletion, insertion steps
    ├── etl.py                  <- Python script allowing to create tables based on json files
    ├── stack.yml               <- Docker container for postgres image
    ├── data                    <- json files containing data




# Getting started

## 1. Clone this repository

```
$ git clone <this_project>
$ cd <this_project>
```

## 2. Install requirements

```
$ pip install -r requirements.txt
```
--------

