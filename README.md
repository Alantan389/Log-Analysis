
Logs Analysis

Purpose of this project : 
Build an internal reporting tool that will use information from the database to discover different aspect of the business. Use the data to find out reader's favious. 


Outcome 
print out the answer for three query querions. 
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?


Technical suppor tools
1. PostgreSQL
2. Python 
3. Vagrant and virtual Box 


Skills
1. vagrnat and virtual set up
2. Python DB-API 
3. Joining tables, The select...where statement, Select clauses,
4. Views
5. The select statement, SQL string functions , Aggregate functions



The purpose of the tools
1. PostgreSQL - Data storage, create relative tables to ogernize data inorder to sort out useful data
2. Python - Query and interact with data from PostgreSQL database . Present the outcome to user.
3. Vagrant an virtual box - Provided a virtual envirment to run PostgreSQL. 


How to fillfull the project ?
1. Clone the databses.
2. Download , set up configer Vagrant and Virtual Box.
3. Create database.
4. Create correlate tables and views.
5. Use DB-API metho to query table with python codes.




Datails for fillfulling the project.

Vagrant and Virtual :
input "vagrant up" to start up the VM.
input "vagrant ssh" to log into the VM.
"cd /vagrant" to change to your vagrant directory.
"psql -d news -f newsdata.sql" to load the data and create the tables.

PosterSQL :
\c tablename
create correlate tables
create correlate views

Python :
DB-API 



Tables:
1. aticles
2. authors
3. log

View:
1. counterrors
2. allrequests
3. countallrequests
4. error_percentage

------------------------------------------------------------------------------------------------------------------------------
 1. CREATE VIEW counterrors AS SELECT COUNT(*) AS num,time FROM allerror GROUP BY time ORDER BY num DESC;
 2. CREATE VIEW allrequests AS SELECT time ::date,status FROM log ORDER BY time;
 3. CREATE VIEW countallrequests AS SELECT count(*) as num,time FROM allrequests GROUP BY time ORDER BY num DESC;
 4. CREATE VIEW error_percentage AS SELECT counterrors.num::double precision/countallrequests.num::double precision *100 AS result,counterrors.time FROM counterrors,countallrequests WHERE counterrors.time=countallrequests.time ORDER BY result DESC;









