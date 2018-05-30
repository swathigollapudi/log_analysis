# log_analysis
Second project in fullstack nanodegree course is log analysis
-This project is to create python program using psycopg2(ie,used to connect to database) that prints out the reports required based on the data in the database 
## To build:
we need
-python 
-vagrant
-virtual box
-postgres
## Setup:
  Firstly,create a vagrant folder on desktop and open command prompt or terminal in that path
#### installation commands of vagrant
  ###### -vagrant-v
  ###### -vagrant init ubuntu/trusty64
  ###### -vagrant up
  ###### -vagrant ssh
#### Now,install postgres by a command:
  ###### -sudo apt -get install python-psycopg2
#### To,change to postgres folder we need to use command:
  ###### -sudo -i -u postgres
#### Then,to connect to postgres database command is:
  ###### -psql
#### Then,to display all the files in this directory command is:
  ###### -\l
#### Then create of user with some password:
  ###### -create user username with password="---"
#### To display all the roles:
  ###### -\du
#### To create different roles in the database created is:
  ###### -alter user demo with Superuser
  ###### -alter user demo with Createrole
  ###### -alter user demo with replication
#### To connect to other database we need to use command:
  ###### -\c database name
#### To exit from one database we need to use command:
  ###### -\q or exit 
#### To go to vagrant path:
  ###### -sudo -i -u vagrant
#### Now,create vagrant database:
  ###### -Createdb vagrant
#### Now,open database vagrant by:
  ###### -psql
#### Then create database named news:
  ###### -Createdb news
#### Now, to connect vagrant database to news database:
  ###### -/c news
#### To,fetch sql files we use: 
  ###### -psql -d news-f sqlfilename
#### Here, newsdata.sqlis fetched to news database which mainly contains three tables:
  ###### -articles
  ###### -authors
  ###### -log
## First question in this project is What are the most popular three articles of all time? 
  #### -I created view named noofviews
  ##### query:
    create view noofviews as select title,author,count(*) as views from articles,log where log.path like concat('%',articles.slug) group by articles.title,articles.author order by views desc;
## First question in this project is Who are the most popular article authors of all time?
  #### -I created view named viewauthor
  ##### query:
    create view viewauthor as select name,count(*) as views from articles,authors,log where articles.author=authors.id and log.path like concat('%',articles.slug) group by name order by views desc;
## First question in this project is On which days did more than 1% of requests lead to errors?
#### I created three views as follows
    create view firstview as select count(status) as count1, date(TIME) as date from log where status!='200 OK' group by date order by count1 desc;
    create view secondview as select count(status) as count2,date(TIME) as date from log group by date order by count desc;
    create view finalview as select firstview.date as date,((100.00*count1)/count2) as perc from firstview natural join secondview  where firstview.date=secondview.date group by firstview.date,perc order by perc desc;
#### For running all these queries we need to create python program and I created project.py as my python file
#### In this firstly,
  ###### -import psycopg2
  ###### -Then database connection
  ###### -I used try except approach all over the python program
  ###### -Create cursor object
  ###### -Then after creating and select queries I fetched the data with this cur object
  ###### -Then close connections
## To run:
  #### -In vagrant path run command
  ###### **python project.py
