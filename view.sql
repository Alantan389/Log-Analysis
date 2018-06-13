
 CREATE VIEW counterrors AS 
 SELECT COUNT(*) 
 AS num,time ::date AS date
 FROM log
 WHERE status='404 NOT FOUND' 
 GROUP BY date 
 ORDER BY num DESC;
  
 
 CREATE VIEW countallrequests AS
 SELECT count(*) as num, time::date AS date
 FROM log
 GROUP BY date
 ORDER BY num DESC;
 

 CREATE VIEW error_percentage AS 
 SELECT counterrors.num::double precision/countallrequests.num::double precision *100 
 AS result,counterrors.date 
 FROM counterrors,countallrequests 
 WHERE counterrors.date=countallrequests.date 
 ORDER BY result DESC;
