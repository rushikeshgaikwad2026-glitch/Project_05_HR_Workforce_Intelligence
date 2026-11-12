
-- ============================================================
-- PROJECT 05: WORKFORCE INTELLIGENCE
-- STEP 1: DATABASE TABLE CREATION
-- ============================================================

-- Select the database created in MySQL Workbench
USE hr_workforce_intelligence;

-- Create the employee table
CREATE TABLE IF NOT EXISTS hr_employee_attrition (

    EmployeeNumber INT PRIMARY KEY,

    Age INT,
    Attrition VARCHAR(10),
    BusinessTravel VARCHAR(50),
    DailyRate INT,
    Department VARCHAR(100),
    DistanceFromHome INT,
    Education INT,
    EducationField VARCHAR(100),
    EnvironmentSatisfaction INT,
    Gender VARCHAR(20),
    HourlyRate INT,
    JobInvolvement INT,
    JobLevel INT,
    JobRole VARCHAR(100),
    JobSatisfaction INT,
    MaritalStatus VARCHAR(30),
    MonthlyIncome INT,
    MonthlyRate INT,
    NumCompaniesWorked INT,
    OverTime VARCHAR(10),
    PercentSalaryHike INT,
    PerformanceRating INT,
    RelationshipSatisfaction INT,
    StockOptionLevel INT,
    TotalWorkingYears INT,
    TrainingTimesLastYear INT,
    WorkLifeBalance INT,
    YearsAtCompany INT,
    YearsInCurrentRole INT,
    YearsSinceLastPromotion INT,
    YearsWithCurrManager INT

);

-- Verify table creation
SHOW TABLES;

-- Check table structure
DESCRIBE hr_employee_attrition;


SHOW VARIABLES LIKE 'local_infile';