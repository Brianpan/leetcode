#---------Tags---------
#ConsecutiveNumber
#SelectMoreThanOneTable
#----------------------

#---------Notes---------
# Select more than one table to do so
# 
#-----------------------

# My initiated Solution
# Use IN and JOIN
# I think the answer is not really good
SELECT id, date, people FROM
stadium WHERE
id IN (
    SELECT s.id FROM
    (SELECT id FROM stadium
     WHERE people >= 100) AS s INNER JOIN 
    (SELECT id FROM stadium
     WHERE people >= 100) AS s2 ON
     s.id=s2.id-1 
     INNER JOIN (SELECT id FROM stadium
     WHERE people >= 100) AS s3 ON
     s.id=s3.id-2
)
OR
id IN (
    SELECT s2.id FROM
    (SELECT id FROM stadium
     WHERE people >= 100) AS s INNER JOIN 
    (SELECT id FROM stadium
     WHERE people >= 100) AS s2 ON
     s.id=s2.id-1 
     INNER JOIN (SELECT id FROM stadium
     WHERE people >= 100) AS s3 ON
     s.id=s3.id-2
)
OR
id IN (
    SELECT s3.id FROM 
    (SELECT id FROM stadium
     WHERE people >= 100) AS s INNER JOIN 
    (SELECT id FROM stadium
     WHERE people >= 100) AS s2 ON
     s.id=s2.id-1 
     INNER JOIN (SELECT id FROM stadium
     WHERE people >= 100) AS s3 ON
     s.id=s3.id-2
);

# A better solution
SELECT DISTINCT t1.* FROM 
stadium AS t1, stadium AS t2, stadium AS t3
WHERE t1.people >= 100  AND t2.people >= 100 AND t3.people >= 100
AND 
  # t1 t2 #t3
( (t2.id -t1.id = 1 AND t3.id-t2.id=1)
OR
  # t3 t1 t2
  (t2.id-t1.id=1 AND t1.id-t3.id=1)
OR
  # t3 t2 t1
  (t1.id-t2.id=1 AND t2.id-t3.id=1)
)
ORDER BY t1.id;
