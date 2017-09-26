#---------Tags---------
#UseJoin
#UseParams
#----------------------

#---------Notes---------
# Use two join to implement
# Use param to check
#
#-----------------------

# My Solution (40%)
# Write your MySQL query statement below
SELECT DISTINCT(f.Num) AS ConsecutiveNums
FROM (SELECT l1.Num AS Num FROM Logs AS l1 
        INNER JOIN Logs AS l2 ON l1.Id=(l2.Id-1)
        INNER JOIN Logs AS l3 ON l1.Id=(l3.Id-2)
        WHERE l1.Num=l2.Num AND l1.Num=l3.Num
   ) AS f;

# Use param's implementation (98%)
SELECT DISTINCT(Num) AS ConsecutiveNums
FROM (SELECT Num,@count:=IF(@pre=(@pre:=Num), @count+1, 1) AS s
		FROM Logs, (SELECT @count:=0, @pre:= -1) AS INIT
) AS t
WHERE t.s > 2;