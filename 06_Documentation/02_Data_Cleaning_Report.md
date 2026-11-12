# Data Cleaning Report

## Project: Workforce Intelligence

## 1. Original Dataset

- Original Rows: 1470
- Original Columns: 35

## 2. Data Quality Checks

- Missing Values: 0
- Duplicate Rows Found: 0
- Duplicate Employee Numbers: 0
- Blank Text Values: 0
- Negative Value Columns: []
- Tenure Violations: 0

## 3. Columns Removed

- EmployeeCount
- Over18
- StandardHours

## 4. Final Dataset

- Final Rows: 1470
- Final Columns: 32
- Rows Removed: 0

## 5. Output File

`02_Cleaned_Data/HR_Analytics_Cleaned.csv`

## 6. Cleaning Notes

- Original raw data was preserved.
- EmployeeNumber was retained as the employee identifier.
- Constant columns were removed because they provide no analytical value.
- No missing values were imputed.