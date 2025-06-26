-- Write your PostgreSQL query statement below
SELECT Project.project_id, ROUND(AVG(Employee.experience_years), 2) AS average_years 
FROM Project
LEFT JOIN Employee ON Employee.employee_id = Project.employee_id
GROUP BY Project.project_id