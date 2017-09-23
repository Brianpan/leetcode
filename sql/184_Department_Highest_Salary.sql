#---------Tags---------
#AggregateFunction
#----------------------

#---------Notes---------
# Two JOIN but may not be efficient but have to do so
# 
#-----------------------

# Write your MySQL query statement below
SELECT d2.Department, d3.Employee AS Employee, d2.Salary AS Salary
FROM (SELECT d.Name AS Department, MAX(Salary) AS Salary
FROM Employee AS e
INNER JOIN Department AS d ON e.DepartmentId=d.id
GROUP BY d.Id) AS d2
INNER JOIN 
 (SELECT d.Name AS Department, e.Name AS Employee, e.Salary AS Salary
FROM Employee AS e
INNER JOIN Department AS d ON e.DepartmentId=d.id) AS d3
ON (d3.Department=d2.Department AND d3.Salary=d2.Salary);

