# ISTA programming test

## Introduction

This is a programming test for the ISTA interview process. The goal is to create a simple web application showing basic information in a HTML table, based on a csv file and a SQLite database.

To address it, I used the following approach:

1. Reduce the complexity of both data sources to a single one. I did it with a Python script, you can found it here: [data/sqlite2json.py](data/sqlite2json.py). I made two version as outputs: 
   - [JSON file](data/data.json) useful to work with Javascript on the frontend.
   - [SQLite database](data/data_fixed.sqlite3) useful to work with Rails on server side.

2. I made several mini-applications just to test it with different technologies:
   - Plain Javascript + DataTable plugin
   - VueJS without DataTable, doing interactive sortering by myself
   - Ruby on Rails classic serverside sorting. MVC without migrations

## Run the applications on internet

You can run the applications on internet, just click on the following links:
- [Plain Javascript](https://fedegonzal.github.io/ista-test/javascript/)
- [VueJS](https://fedegonzal.github.io/ista-test/vuejs/dist/)
- Rails: no deployed version yet, sorry.

## Requirements to run the applications locally

You can run each application separately, but you need to install some dependencies first.

### Python script

Needed to reproduce the creation of JSON and SQLite simplified versions (provided here in the repo). Just need Python 3.6 or higher installed and run the script:
```python sqlite2json.py```

### Plain Javascript

Just open the file [javascript/index.html](javascript/index.html) in your browser using a local webserver. You can use ```npm http-server``` to do it (you need node installed and later you can do ```npm install http-server -g``` to install the local webserver).

### VueJS

To run the VueJS version of the application:
1. Install VueJS and it's dependencies (lodash for sorting). You can do it with npm: ```npm install```
2. Go to the folder [vuejs](vuejs) and run the local webserver: ```npm run dev```

### Ruby on Rails

Finally, to run the Rails version of the application you need to install [Ruby language](https://www.ruby-lang.org/en/) and [Rails Framework](https://rubyonrails.org/). 

Then, go to the folder [railsapp](railsapp) and run the local webserver: ```bin/rails server```

I put a copy of SQLite fixed version (made with the Python script) in the folder [railsapp/db](railsapp/db). You can use it to test the application (it's filename is data.sqlite3).
