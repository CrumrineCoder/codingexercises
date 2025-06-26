SELECT Employees.name as Employee
FROM Employee as Employees, Employee as Managers
WHERE Employees.managerId = Managers.id AND Employees.salary > Managers.salary