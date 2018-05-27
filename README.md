# Log--Analysis

## Description
>In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

## Why this project?
* This project will stretch your SQL database skills. 
* Interacting with a live database both from the command line and from your code.
* Exploring a large database with over a million rows. 
* Building & refining complex queries & how to use them to draw business conclusions from data.   

## Download these resources before running the project
 - [Python](https://www.python.org)
 - [Vagrant](https://www.vagrantup.com)
 - [Virtual Machine](https://www.virtualbox.org)

## To run this project:
- Install Vagrant and VirtualBox
- Download the database file newsdata.sql from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
- Downlaod or Clone this repository.
- Copy the newsdata.sql file and content of this current repository.
- Now open terminal and write these commands to run virtual machine:
```
   * vagrant up
   * vagrant ssh
   * cd /vagrant
   * psql -d news -f newsdata.sql   
```
- Open database `psql news`
- Create the views
 * ### Create first_query_view
   ```
       CREATE OR REPLACE VIEW first_query_view
	   AS
       SELECT articles.title as Article, COUNT(*) as VIEW1 FROM articles
       INNER JOIN log on log.path
	   LIKE concat('%',articles.slug,'%')
       AND log.status LIKE '%200 OK%' 
	   GROUP BY Article,log.path
       ORDER BY VIEW1 DESC
   ``` 
Collumn name        |  type
------------------- | -------------
Article             |varchar2
VIEW1               |int

 * ### Create view second_query_view
   ```
       CREATE OR REPLACE VIEW second_query_view 
	   AS 
	   SELECT authors.name 
	   AS Name,Count(*) AS VIEW2
	   FROM authors,articles,log
       WHERE authors.id=articles.author 
	   AND log.status like '%200 OK%'
       AND log.path LIKE concat('%',articles.slug,'%')
       GROUP BY Name ORDER BY VIEW2 DESC
   ``` 
 Collumn name        |  type
 ------------------- | -------------
 Author              |varchar2
 VIEW2               |int
 
 * ### Create view third_query_view
   ```
       CREATE OR REPLACE VIEW third_query_view 
	   AS 
	   SELECT date(time) AS Date,
	   round(sum(case status when '200 OK' THEN 0 else 1 end)*100.0/count(status),1)
	   AS error FROM log 
	   GROUP BY Date ORDER BY error
   ``` 
 Collumn name        |  type
 ------------------- | -------------
 Date                |varchar2
 error               |int
 
- Run command `python query.py` wherever the file exist in your downloaded folder.





