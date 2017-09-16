#---------Tags---------
#NestedQuery
#AggregatedFunction
#----------------------

#---------Notes---------
# Write your MySQL query statement below
# use MySQL 沒有except
# 用nest query
# MySQL Aggregate
#-----------------------

# My Solution IN may not use INDEX
SELECT MAX(Salary) AS SecondHighestSalary FROM Employee 
WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee)
ORDER BY Salary ASC;

# Best Solution 
SELECT MAX(c.Salary) AS SecondHighestSalary FROM
(SELECT Salary FROM Employee WHERE Salary != 
(SELECT MAX(Salary) FROM Employee)
);