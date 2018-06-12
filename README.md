
# Logs Analysis


## Purpose of this project : 
Build an internal reporting tool that will use information from the database to discover different aspect of the business. Use the data to figure out reader's preference. 



## Outcome 
print out the answer for three query querions. 
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?




## Technical support tools
1. PostgreSQL
2. Python 
3. Vagrant and virtual Box 




## The purpose of the tools
1. PostgreSQL - Data storage, create relative tables to ogernize data inorder to sort out useful data
2. Python - Query and interact with data from PostgreSQL database . Present the outcome to user.
3. Vagrant an virtual box - Provided a virtual envirment to run PostgreSQL. 



## Skills
1. vagrnat
2. Python DB-API 
3. Joining tables, The select...where statement, Select clauses,
4. Views
5. The select statement, SQL string functions , Aggregate functions




## How to do it ?
#### 1. Clone the databses.
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

#### 2. Download and set up Vagrant,Virtual Box. 
https://www.vagrantup.com

#### 3. Configer Vagrant 
(https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile)

#### 4. Access to vagrant and link up to the newsdata.sql file :
a. input "vagrant up" to start the VM.
b. input "vagrant ssh" to log into the VM.
c. "cd /vagrant" to change to your vagrant directory.
d. "psql -d news -f newsdata.sql" to load the data and create the tables.

#### 5. Create correlate tables and views.
run "psql -d news -f views.sql" to create the views.

#### 6. Use DB-API metho to query table with python codes.

#### 7. Run python script in by inputing "python your_file.py" in the terminal 




## Tables:
1. aticles
2. authors
3. log


## View:
1. counterrors
2. countallrequests
3. error_percentage

#### 1.counterrors 
 CREATE VIEW counterrors AS 
 SELECT COUNT(*) 
 AS num,time ::date AS date
 FROM log
 WHERE status='404 NOT FOUND' 
 GROUP BY date 
 ORDER BY num DESC;
  
#### 2. countallrequests
 CREATE VIEW countallrequests AS
 SELECT count(*) as num, time::date AS date
 FROM log
 GROUP BY date
 ORDER BY num DESC;
 
#### 3. error_percentage
 CREATE VIEW error_percentage AS 
 SELECT counterrors.num::double precision/countallrequests.num::double precision *100 
 AS result,counterrors.date 
 FROM counterrors,countallrequests 
 WHERE counterrors.date=countallrequests.date 
 ORDER BY result DESC;
	









