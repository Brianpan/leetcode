#---------Tags---------
#UseUnion
#UseCase
#----------------------

#---------Notes---------
# Use Mod & Union to generate the records
#-----------------------


# Write your MySQL query statement below
( SELECT (id+1) AS id, student FROM seat WHERE MOD(id, 2)=1 AND id!=(SELECT COUNT(*) FROM seat) )
   UNION
( SELECT id, student FROM seat WHERE MOD(id, 2)=1 AND id=(SELECT COUNT(*) FROM seat))
   UNION
( SELECT (id-1) AS id, student FROM seat WHERE MOD(id, 2)=0 )
ORDER BY id ASC;

# Good enough solution
SELECT
( CASE WHEN MOD(id, 2) != 0 AND id != counts THEN id+1
  WHEN MOD(id, 2) != 0 AND id = counts THEN id
  ELSE id - 1
  END
) AS id, student FROM seat, (SELECT COUNT(*) AS counts FROM seat) AS seat_counts
ORDER BY id ASC;