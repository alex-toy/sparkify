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
    here are filepaths to two files in this dataset :

    ```
    song_data/A/B/C/TRABCEI128F424C983.json
    song_data/A/A/B/TRAABJL12903CDCF1A.json
    ```

    - If you don't have python3 and you are working on your mac: install it from [python.org](https://www.python.org/downloads/)
    - If you don't have python3 and are working on an ubuntu-like system: install from package manager:

        ```
        $ apt-get update
        $ apt-get -y install python3 python3-pip python3-venv
        ```

State and justify your database schema design and ETL pipeline.

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

