#!/usr/bin/env python

import psycopg2

query1 = """SELECT title,COUNT(*) AS num
FROM articles,log
WHERE log.path ='/article/'|| articles.slug
GROUP BY articles.title
ORDER BY num DESC LIMIT 3;"""


query2 = """SELECT authors.name, COUNT(*) AS num
FROM authors LEFT JOIN articles
ON authors.id = articles.author
LEFT JOIN log
ON log.path ='/article/'|| articles.slug
GROUP BY authors.name
ORDER BY num DESC LIMIT 3;"""


query3 = """SELECT result,date
FROM error_percentage
WHERE error_percentage.result>1;"""


# Connect to the PostgreSQL database. Returns a database connection.
def connect():
    try:
        return psycopg2.connect("dbname=news")
    except (Exception, psycopg2.DatabaseError)as error:
        print(error)


# What are the most popular three articles of all time ?
def most_3_articles(query1):
    db = connect()
    cursor = db.cursor()
    cursor.execute(query1)
    run1 = cursor.fetchall()
    db.close()
    return run1


def formatted1():
    print('\n The most popular three articles of all time are :')
    for count, i in enumerate(most_3_articles(query1), 1):
        print ('(' + str(count) + ') ' + "<"+str(i[0])+">"
               + " rank in No."+(str(count))
               + " with total " + str(i[1]) + " views")


# What are the most 3 popular authors ?
def alltime_popular_authors(query2):
    db = connect()
    cursor = db.cursor()
    cursor.execute(query2)
    run2 = cursor.fetchall()
    db.close()
    return run2


def formatted2():
    print('\nThe morst 3 popular authors are :')
    count = 1
    for count, i in enumerate(alltime_popular_authors(query2), 1):
        print ('(' + str(count) + ') ' + "Author, "+str(i[0]) + " with total "
               + str(i[1]) + " views")


# On which days did more than 1% of requests lead to errors?
def days_error(query3):
    db = connect()
    cursor = db.cursor()
    cursor.execute(query3)
    run3 = cursor.fetchall()
    db.close()
    return run3


def formatted3():
    print('\nThe error precentage result:')
    for count, i in enumerate(days_error(query3), 1):
        print ('(' + str(count) + ') ' + "On "+str(i[1])
               + ", The error precentage is " + str(round(i[0], 2))
               + "%"+" which over 1.0% of the requests.")


if __name__ == "__main__":
    print
    formatted1()
    formatted2()
    formatted3()
