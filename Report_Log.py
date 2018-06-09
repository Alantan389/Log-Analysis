import psycopg2

query1= "SELECT title,COUNT(*) AS num FROM articles,log WHERE log.path LIKE concat('%',articles.slug) GROUP BY articles.title ORDER BY num DESC LIMIT 3;"
query2= "SELECT authors.name, COUNT(*) AS num FROM authors LEFT JOIN articles ON authors.id = articles.author LEFT JOIN log ON log.path like concat('/article/%', articles.slug) GROUP BY authors.name ORDER BY num DESC LIMIT 3;"
query3= "SELECT result,time FROM error_percentage WHERE error_percentage.result>1;"


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news1")



# what are the most popular three articles of all time ?
def most_3_articles(query1):
	db = connect()
	cursor = db.cursor()
	cursor.execute(query1)
	return cursor.fetchall()
	db.close()

def run_python1():
	print('\n The most popular three articles of all time are :')
	count=1
	for i in most_3_articles(query1):
		print ('(' + str(count) + ') ' + "<"+str(i[0])+">" + " ranking in No."+(str(count)) +" with total " + str(i[1]) + " views")
		count+=1


# waht are the most 3 popular authors ?
def alltime_popular_authors(query2):
	db = connect()
	cursor = db.cursor()
	cursor.execute(query2)
	return cursor.fetchall()
	db.close()

def run_python2():
	print('\nThe morst 3 popular authors are :')
	count = 1
	for i in alltime_popular_authors(query2):
		print ('(' + str(count) + ') ' + "Author, "+str(i[0]) + " with total " + str(i[1]) + " views")
		count += 1




# On which days did more than 1% of requests lead to errors?
def days_error(query3):
	db = connect()
	cursor = db.cursor()
	cursor.execute(query3)
	return cursor.fetchall()
	db.close()

def run_python3():
	print('\nThe error precentage result:')
	count=1
	for i in days_error(query3):
		print ('(' + str(count) + ') ' +"On "+str(i[1])+", The error precentage is "+str(round(i[0])) +"%"+" which over 1.0% of the requests.")
		count+=1
        

print 
run_python1()
run_python2()
run_python3()



