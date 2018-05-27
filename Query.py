#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2

DBNAME = 'news'

# Queries we need to perform

queryQ = ['1.What are the most popular three articles of all time?',
          '2.Who are the most popular article authors of all time?',
          '3.On which days did more than 1% of requests lead to errors?']

# Queries

query1 = """Select * from first_query_view LIMIT 3"""

query2 = """Select * from second_query_view LIMIT 4"""

query3 = """SELECT * FROM third_query_view WHERE error > 1"""


# Running the query and returning results

def query_exe(query):
    """Return all posts from the 'database', most recent first."""

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # Query execution

    c.execute(query)

    # Fetching result

    res = c.fetchall()
    db.close()
    return res


# Printing query

def print_query(results, n):
    """prints Question 3 ,fetches results, and prints result"""

    print queryQ[n - 1]

    # Loop to fetch and print values of result

    for i in results:
        Article = i[0]
        Views = i[1]
        if n == 3:
            print '\t %s --- %.1f' % (Article, Views) + '  % errors'
        else:
            print '\t %s --- %d' % (Article, Views) + '  views'


# This method takes in queries and does all the work for us

def printqueryresult(query, i):
    """runs and prints results"""

    results = query_exe(query)
    print_query(results, i)


printqueryresult(query1, 1)
printqueryresult(query2, 2)
printqueryresult(query3, 3)
