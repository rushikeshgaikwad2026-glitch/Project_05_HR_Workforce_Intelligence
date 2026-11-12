
# ============================================================
# PROJECT 05: WORKFORCE INTELLIGENCE
# SCRIPT 07: STATISTICAL ANALYSIS
# ============================================================
# Objective:
# Statistically examine associations between employee
# characteristics and attrition.
#
# Tests:
# 1. Chi-square test of independence
# 2. Mann-Whitney U test
#
# Important:
# Statistical association does not establish causation.
# P-values are exploratory and are not adjusted for
# multiple comparisons.
# ============================================================


# STEP 1: IMPORT LIBRARIES

import pandas as pd
import numpy as np
import os

from scipy.stats import chi2_contingency
from scipy.stats import mannwhitneyu


# STEP 2: DEFINE FILE PATHS

project_folder = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

csv_path = os.path.join(
    project_folder,
    "02_Cleaned_Data",
    "HR_Analytics_Cleaned.csv"
)

documentation_folder = os.path.join(
    project_folder,
    "06_Documentation"
)

os.makedirs(documentation_folder, exist_ok=True)


# STEP 3: LOAD DATASET

df = pd.read_csv(csv_path)

print("\n" + "=" * 65)
print("WORKFORCE INTELLIGENCE - STATISTICAL ANALYSIS")
print("=" * 65)

print("\nDataset loaded successfully!")
print("Total Employees:", len(df))


# STEP 4: DEFINE VARIABLES

categorical_variables = [
    "Department",
    "JobRole",
    "BusinessTravel",
    "Gender",
    "MaritalStatus",
    "OverTime",
    "JobSatisfaction",
    "EnvironmentSatisfaction",
    "RelationshipSatisfaction",
    "WorkLifeBalance",
    "JobInvolvement",
    "JobLevel",
    "StockOptionLevel"
]

numeric_variables = [
    "Age",
    "DailyRate",
    "DistanceFromHome",
    "HourlyRate",
    "MonthlyIncome",
    "NumCompaniesWorked",
    "PercentSalaryHike",
    "TotalWorkingYears",
    "TrainingTimesLastYear",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager"
]


# STEP 5: CHI-SQUARE TEST

print("\n" + "=" * 65)
print("1. CHI-SQUARE TEST: CATEGORICAL VARIABLES AND ATTRITION")
print("=" * 65)

chi_square_results = []

for column in categorical_variables:

    contingency_table = pd.crosstab(
        df[column],
        df["Attrition"]
    )

    chi2, p_value, degrees_freedom, expected = (
        chi2_contingency(contingency_table)
    )

    total = contingency_table.to_numpy().sum()

    minimum_dimension = min(contingency_table.shape) - 1

    if minimum_dimension > 0:
        cramers_v = np.sqrt(
            chi2 / (total * minimum_dimension)
        )
    else:
        cramers_v = np.nan

    result = {
        "Variable": column,
        "Chi_Square": round(chi2, 4),
        "Degrees_of_Freedom": degrees_freedom,
        "P_Value": p_value,
        "Cramers_V": round(cramers_v, 4),
        "Statistically_Significant": (
            "Yes" if p_value < 0.05 else "No"
        )
    }

    chi_square_results.append(result)

chi_square_df = pd.DataFrame(chi_square_results)

chi_square_df = chi_square_df.sort_values(
    by="P_Value"
).reset_index(drop=True)

print("\nChi-square test results:")
print(chi_square_df.to_string(index=False))


# STEP 6: MANN-WHITNEY U TEST

print("\n" + "=" * 65)
print("2. MANN-WHITNEY U TEST: NUMERIC VARIABLES AND ATTRITION")
print("=" * 65)

mann_whitney_results = []

employees_stayed = df[df["Attrition"] == "No"]
employees_left = df[df["Attrition"] == "Yes"]

for column in numeric_variables:

    stayed_values = employees_stayed[column].dropna()
    left_values = employees_left[column].dropna()

    statistic, p_value = mannwhitneyu(
        stayed_values,
        left_values,
        alternative="two-sided"
    )

    median_stayed = stayed_values.median()
    median_left = left_values.median()

    result = {
        "Variable": column,
        "Median_Stayed": round(median_stayed, 2),
        "Median_Left": round(median_left, 2),
        "U_Statistic": round(statistic, 2),
        "P_Value": p_value,
        "Statistically_Significant": (
            "Yes" if p_value < 0.05 else "No"
        )
    }

    mann_whitney_results.append(result)

mann_whitney_df = pd.DataFrame(mann_whitney_results)

mann_whitney_df = mann_whitney_df.sort_values(
    by="P_Value"
).reset_index(drop=True)

print("\nMann-Whitney U test results:")
print(mann_whitney_df.to_string(index=False))


# STEP 7: IDENTIFY SIGNIFICANT RESULTS

print("\n" + "=" * 65)
print("3. STATISTICALLY SIGNIFICANT RESULTS")
print("=" * 65)

significant_categorical = chi_square_df[
    chi_square_df["P_Value"] < 0.05
]

significant_numeric = mann_whitney_df[
    mann_whitney_df["P_Value"] < 0.05
]

print("\nCategorical variables with p-value below 0.05:")

if len(significant_categorical) > 0:
    print(
        significant_categorical[
            ["Variable", "P_Value", "Cramers_V"]
        ].to_string(index=False)
    )
else:
    print("No statistically significant variables found.")

print("\nNumeric variables with p-value below 0.05:")

if len(significant_numeric) > 0:
    print(
        significant_numeric[
            ["Variable", "Median_Stayed", "Median_Left", "P_Value"]
        ].to_string(index=False)
    )
else:
    print("No statistically significant variables found.")


# STEP 8: SAVE RESULTS TO CSV

chi_square_path = os.path.join(
    documentation_folder,
    "03_Chi_Square_Test_Results.csv"
)

mann_whitney_path = os.path.join(
    documentation_folder,
    "04_Mann_Whitney_Test_Results.csv"
)

chi_square_df.to_csv(
    chi_square_path,
    index=False
)

mann_whitney_df.to_csv(
    mann_whitney_path,
    index=False
)


# STEP 9: CREATE SUMMARY REPORT

report_path = os.path.join(
    documentation_folder,
    "05_Statistical_Analysis_Report.md"
)

with open(report_path, "w", encoding="utf-8") as file:

    file.write("# Statistical Analysis Report\n\n")

    file.write("## Project: Workforce Intelligence\n\n")

    file.write(
        "This report examines statistical associations "
        "between employee characteristics and attrition "
        "using the IBM HR Analytics dataset.\n\n"
    )

    file.write("## Dataset Overview\n\n")

    file.write(f"- Total employees: {len(df)}\n")
    file.write(
        f"- Employees who stayed: {len(employees_stayed)}\n"
    )
    file.write(
        f"- Employees who left: {len(employees_left)}\n\n"
    )

    file.write("## Statistical Methods\n\n")

    file.write(
        "1. Chi-square test of independence for categorical "
        "variables.\n"
    )

    file.write(
        "2. Mann-Whitney U test for numeric variables.\n\n"
    )

    file.write("## Chi-square Test Results\n\n")

    file.write(
        chi_square_df.to_markdown(index=False)
    )

    file.write("\n\n## Mann-Whitney U Test Results\n\n")

    file.write(
        mann_whitney_df.to_markdown(index=False)
    )

    file.write("\n\n## Interpretation Guidelines\n\n")

    file.write(
        "- A p-value below 0.05 indicates statistical "
        "evidence of an association or difference under "
        "the assumptions of the test.\n"
    )

    file.write(
        "- Cramér's V describes the strength of association "
        "for chi-square results.\n"
    )

    file.write(
        "- Median values help compare numeric variables "
        "between employees who stayed and left.\n"
    )

    file.write(
        "- Statistical significance does not establish "
        "causation or business importance.\n"
    )

    file.write(
        "- P-values are exploratory and have not been "
        "adjusted for multiple comparisons.\n"
    )

    file.write(
        "- Results apply to this fictional employee dataset "
        "and should not be treated as evidence about a "
        "real company's workforce.\n"
    )


# STEP 10: FINAL MESSAGE

print("\n" + "=" * 65)
print("STATISTICAL ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 65)

print("\nFiles saved:")

print(chi_square_path)
print(mann_whitney_path)
print(report_path)
    
print("\nAll statistical tests completed.")
