#---------Tags---------
#UseInnerJoin
#UseParams
#----------------------

#---------Notes---------
# Inner Join with a distinct & param to get rank
#-----------------------

# My Solution
SET @rownum=0;
SELECT s.Score, s2.Rank 
    FROM Scores AS s
    INNER JOIN 
(SELECT s.Score AS Score, (@rownum:=@rownum+1) AS Rank
    FROM (SELECT DISTINCT(Score) FROM Scores ORDER BY Score DESC) AS s) AS s2
    ON s.Score = s2.Score ORDER BY s.Score DESC;

# A Simpler Solution
SELECT Score, (SELECT COUNT(*) FROM Scores WHERE Score >= s.Score) AS Rank FROM Scores AS s
ORDER BY s.Score DESC;