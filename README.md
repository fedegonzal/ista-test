# ISTA programming test

## Introduction

This is a programming test for the ISTA interview process. The goal is to create a simple web application showing basic information in a HTML table, based on a csv file and a SQLite database.

To address it, I used the following approach:

1. Reduce the complexity of both data sources to a single one. I did it with a Python script, you can found it here: [data/sqlite2json.py](data/sqlite2json.py). I made two version as outputs: 
   - [JSON file](data/data.json) useful to work with Javascript on the frontend.
   - [SQLite database](data/data_fixed.sqlite3) useful to work with Rails on server side.

## Requirements

You can run each application separately, but you need to install some dependencies first.

### Python script

Needed to reproduce the creation of JSON and SQLite simplified versions (provided here in the repo). Just need Python 3.6 or higher installed and run the script:
```python sqlite2json.py```
