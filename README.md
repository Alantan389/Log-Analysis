
## Logs Analysis

### Purpose of this project :
Build an internal reporting tool that will use information from the database to discover the different aspects of the business. Use the data to figure out reader's preference.

### Outcome
##### print out the answer for three query questions.
1.What are the most popular three articles of all time?
2.Who are the most popular article authors of all time?
3.On which days did more than 1% of requests lead to errors?



### Technical support tools

1.PostgreSQL
2.Python
3.Vagrant and Virtual Box


### The purpose of the tools
PostgreSQL - Data storage, create relative tables to organize data to sort out useful data
Python - Query and interact with data from PostgreSQL database. Present the outcome to the user.
Vagrant an virtual box - Provided a virtual envirment to run PostgreSQL.
Skills
1. vagrant
2. Python DB-API
3. Joining tables, The select...where statement, Select clauses,
4. Views
5. The select statement, SQL string functions, Aggregate functions



### How to do it?
#### <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip/">1. Clone the databse.</a>


#### <a href="https://www.vagrantup.com">2. Download and set up Vagrant, Virtual Box.</a>


#### <a href="https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile">3. Configure Vagrant </a>


#### 4. Access to vagrant and link up to the newsdata.sql file :
input "vagrant up" to start the VM. 
Input "vagrant ssh" to log into the VM. c. "cd /vagrant" to change to your vagrant directory. d. "psql -d news -f newsdata.sql" to load the data and create the tables.

#### 5. Create correlate tables and views.
run "psql -d news -f views.sql" to create the views.

#### 6. Use DB-API method to query tables with python codes.

#### 7. Run python script in by inputting "python your_file.py" in the terminal




### Tables:
aticles
authors
log





### View:
counterrors
countallrequests
error_percentage
#### 1.counterrors
CREATE VIEW counterrors AS SELECT COUNT(*) AS num,time ::date AS date FROM log WHERE status='404 NOT FOUND' GROUP BY date ORDER BY num DESC;

#### 2. countallrequests
CREATE VIEW countallrequests AS SELECT count(*) as num, time::date AS date FROM log GROUP BY date ORDER BY num DESC;

#### 3. error_percentage
CREATE VIEW error_percentage AS SELECT counterrors.num::double precision/countallrequests.num::double precision *100 AS result,counterrors.date FROM counterrors,countallrequests WHERE counterrors.date=countallrequests.date ORDER BY result DESC;




### Python codes review

##### Make sure your code meets the pep8 requirement

##### Autopep8 automatically formats Python code to conform to the PEP 8 style Github guide. It uses the pep8 utility to determine what parts of the code need to be formatted. autopep8 is capable of fixing most of the formatting issues that can be reported by pep8.





### How to set up Python Pep8 Autoformat

#### Installation
1.pip install pycodestyle 
2.pip install --upgrade autopep8
3.easy_install -ZU autopep8


#### Execution
1. $ autopep8 yourfile.py


### How to test your code style and modify them.

#### 1 CD to your file in terminal
#### 2 autopep8 yourfile.py
#### 3 pycodestyle yourfile.py


-------------------------------------------------------------------

another way to complete project through jupyter note book + download psql and data into local computer.

here are the steps:

connect jupyter note book to local psql schemer

1.download psql to local computer
2.download database (newsdata.sql)
3.create database and table(test1) for further upload newsdata.sql
4.excute newsdata.sql into psql in local computer
5.download psql to python3
6.connect python to local psql table
7.excute python code

