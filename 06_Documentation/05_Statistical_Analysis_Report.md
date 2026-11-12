# Statistical Analysis Report

## Project: Workforce Intelligence

This report examines statistical associations between employee characteristics and attrition using the IBM HR Analytics dataset.

## Dataset Overview

- Total employees: 1470
- Employees who stayed: 1233
- Employees who left: 237

## Statistical Methods

1. Chi-square test of independence for categorical variables.
2. Mann-Whitney U test for numeric variables.

## Chi-square Test Results

| Variable                 |   Chi_Square |   Degrees_of_Freedom |     P_Value |   Cramers_V | Statistically_Significant   |
|:-------------------------|-------------:|---------------------:|------------:|------------:|:----------------------------|
| OverTime                 |      87.5643 |                    1 | 8.15842e-21 |      0.2441 | Yes                         |
| JobRole                  |      86.1903 |                    8 | 2.75248e-15 |      0.2421 | Yes                         |
| JobLevel                 |      72.529  |                    4 | 6.63468e-15 |      0.2221 | Yes                         |
| StockOptionLevel         |      60.5983 |                    3 | 4.37939e-13 |      0.203  | Yes                         |
| MaritalStatus            |      46.1637 |                    2 | 9.45551e-11 |      0.1772 | Yes                         |
| JobInvolvement           |      28.492  |                    3 | 2.86318e-06 |      0.1392 | Yes                         |
| BusinessTravel           |      24.1824 |                    2 | 5.60861e-06 |      0.1283 | Yes                         |
| EnvironmentSatisfaction  |      22.5039 |                    3 | 5.12347e-05 |      0.1237 | Yes                         |
| JobSatisfaction          |      17.5051 |                    3 | 0.0005563   |      0.1091 | Yes                         |
| WorkLifeBalance          |      16.3251 |                    3 | 0.00097257  |      0.1054 | Yes                         |
| Department               |      10.796  |                    2 | 0.00452561  |      0.0857 | Yes                         |
| RelationshipSatisfaction |       5.2411 |                    3 | 0.154972    |      0.0597 | No                          |
| Gender                   |       1.117  |                    1 | 0.290572    |      0.0276 | No                          |

## Mann-Whitney U Test Results

| Variable                |   Median_Stayed |   Median_Left |   U_Statistic |     P_Value | Statistically_Significant   |
|:------------------------|----------------:|--------------:|--------------:|------------:|:----------------------------|
| TotalWorkingYears       |              10 |             7 |        191654 | 2.39957e-14 | Yes                         |
| MonthlyIncome           |            5204 |          3202 |        191600 | 2.95083e-14 | Yes                         |
| YearsAtCompany          |               6 |             3 |        189639 | 2.91619e-13 | Yes                         |
| YearsInCurrentRole      |               3 |             2 |        187007 | 4.42956e-12 | Yes                         |
| YearsWithCurrManager    |               3 |             2 |        185860 | 1.80675e-11 | Yes                         |
| Age                     |              36 |            32 |        185362 | 5.30434e-11 | Yes                         |
| DistanceFromHome        |               7 |             9 |        127996 | 0.00238705  | Yes                         |
| DailyRate               |             817 |           699 |        159179 | 0.0290046   | Yes                         |
| YearsSinceLastPromotion |               1 |             1 |        157847 | 0.0411791   | Yes                         |
| TrainingTimesLastYear   |               3 |             2 |        157436 | 0.0472957   | Yes                         |
| NumCompaniesWorked      |               2 |             1 |        139292 | 0.242365    | No                          |
| PercentSalaryHike       |              14 |            14 |        151494 | 0.365515    | No                          |
| HourlyRate              |              66 |            66 |        147646 | 0.79763     | No                          |

## Interpretation Guidelines

- A p-value below 0.05 indicates statistical evidence of an association or difference under the assumptions of the test.
- Cramér's V describes the strength of association for chi-square results.
- Median values help compare numeric variables between employees who stayed and left.
- Statistical significance does not establish causation or business importance.
- P-values are exploratory and have not been adjusted for multiple comparisons.
- Results apply to this fictional employee dataset and should not be treated as evidence about a real company's workforce.
