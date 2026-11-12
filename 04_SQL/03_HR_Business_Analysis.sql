
-- ============================================================
-- PROJECT 05: WORKFORCE INTELLIGENCE
-- SQL BUSINESS ANALYSIS
-- Database: hr_workforce_intelligence
-- Table: hr_employee_attrition
-- ============================================================

USE hr_workforce_intelligence;


-- ============================================================
-- 1. OVERALL WORKFORCE OVERVIEW
-- ============================================================

SELECT
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    SUM(CASE WHEN Attrition = 'No' THEN 1 ELSE 0 END) AS Employees_Stayed,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate_Percent,
    ROUND(AVG(Age), 1) AS Average_Age,
    ROUND(AVG(MonthlyIncome), 2) AS Average_Monthly_Income
FROM hr_employee_attrition;


-- ============================================================
-- 2. DEPARTMENT-WISE ATTRITION
-- ============================================================

SELECT
    Department,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate_Percent
FROM hr_employee_attrition
GROUP BY Department
ORDER BY Attrition_Rate_Percent DESC;


-- ============================================================
-- 3. JOB ROLE-WISE ATTRITION
-- ============================================================

SELECT
    JobRole,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate_Percent
FROM hr_employee_attrition
GROUP BY JobRole
ORDER BY Attrition_Rate_Percent DESC;


-- ============================================================
-- 4. OVERTIME AND ATTRITION
-- ============================================================

SELECT
    OverTime,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS Employees_Left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate_Percent
FROM hr_employee_attrition
GROUP BY OverTime
ORDER BY Attrition_Rate_Percent DESC;


-- ============================================================
-- 5. AGE GROUP-WISE ATTRITION
-- ============================================================

SELECT
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        WHEN Age BETWEEN 46 AND 55 THEN '46-55'
        ELSE '56+'
    END AS Age_Group,

    COUNT(*) AS Total_Employees,

    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        AS Employees_Left,

    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate_Percent

FROM hr_employee_attrition
GROUP BY Age_Group
ORDER BY MIN(Age);


-- ============================================================
-- 6. SALARY COMPARISON: STAYED VS LEFT
-- ============================================================

SELECT
    Attrition,
    COUNT(*) AS Total_Employees,
    ROUND(AVG(MonthlyIncome), 2) AS Average_Monthly_Income,
    MIN(MonthlyIncome) AS Minimum_Monthly_Income,
    MAX(MonthlyIncome) AS Maximum_Monthly_Income
FROM hr_employee_attrition
GROUP BY Attrition;


-- ============================================================
-- 7. JOB SATISFACTION AND ATTRITION
-- ============================================================

SELECT
    JobSatisfaction,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        AS Employees_Left,

    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate_Percent

FROM hr_employee_attrition
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;


-- ============================================================
-- 8. WORK-LIFE BALANCE AND ATTRITION
-- ============================================================

SELECT
    WorkLifeBalance,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        AS Employees_Left,

    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate_Percent

FROM hr_employee_attrition
GROUP BY WorkLifeBalance
ORDER BY WorkLifeBalance;


-- ============================================================
-- 9. JOB LEVEL AND ATTRITION
-- ============================================================

SELECT
    JobLevel,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        AS Employees_Left,

    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate_Percent,

    ROUND(AVG(MonthlyIncome), 2) AS Average_Monthly_Income

FROM hr_employee_attrition
GROUP BY JobLevel
ORDER BY JobLevel;


-- ============================================================
-- 10. TENURE AND ATTRITION
-- ============================================================

SELECT
    CASE
        WHEN YearsAtCompany BETWEEN 0 AND 2 THEN '0-2 Years'
        WHEN YearsAtCompany BETWEEN 3 AND 5 THEN '3-5 Years'
        WHEN YearsAtCompany BETWEEN 6 AND 10 THEN '6-10 Years'
        ELSE 'Above 10 Years'
    END AS Tenure_Group,

    COUNT(*) AS Total_Employees,

    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        AS Employees_Left,

    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate_Percent

FROM hr_employee_attrition
GROUP BY Tenure_Group
ORDER BY MIN(YearsAtCompany);


-- ============================================================
-- 11. BUSINESS TRAVEL AND ATTRITION
-- ============================================================

SELECT
    BusinessTravel,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        AS Employees_Left,

    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate_Percent

FROM hr_employee_attrition
GROUP BY BusinessTravel
ORDER BY Attrition_Rate_Percent DESC;


-- ============================================================
-- 12. PERFORMANCE RATING AND ATTRITION
-- ============================================================

SELECT
    PerformanceRating,
    COUNT(*) AS Total_Employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        AS Employees_Left,

    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate_Percent

FROM hr_employee_attrition
GROUP BY PerformanceRating
ORDER BY PerformanceRating;
