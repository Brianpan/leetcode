#---------Tags---------
#UseOffset
#UseParams
#----------------------

#---------Notes---------
# 要注意如果有相同的情況發生, 要使用distinct
# 用offset 和設變數
#-----------------------

# My Solution
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT IF(COUNT(e.D_Salary) < N, NULL, MIN(e.D_Salary)) FROM 
        (SELECT DISTINCT(Salary) AS D_Salary FROM Employee ORDER BY Salary DESC LIMIT N) AS e
      
  );
END

# Good enough Solution
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE x INT;
  SET x = N - 1;
  
  RETURN(
    SELECT DISTINCT(Salary) FROM Employee ORDER BY Salary DESC
    LIMIT 1 OFFSET x
  );
END