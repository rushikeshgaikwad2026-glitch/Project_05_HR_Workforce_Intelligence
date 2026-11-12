
# ============================================================
# PROJECT 05: WORKFORCE INTELLIGENCE
# SCRIPT 02: DATA CLEANING
# ============================================================
# Objective:
# Clean the HR dataset and prepare it for analysis.
#
# Important:
# The original raw dataset will not be modified.
# All cleaning operations will be performed on a copy.
# ============================================================


# STEP 1: IMPORT LIBRARIES

import pandas as pd
import os


# STEP 2: DEFINE FILE PATHS

project_folder = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

raw_file = os.path.join(
    project_folder,
    "01_Raw_Data",
    "01_IBM_HR_Analytics",
    "WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

cleaned_folder = os.path.join(
    project_folder,
    "02_Cleaned_Data"
)

documentation_folder = os.path.join(
    project_folder,
    "06_Documentation"
)

os.makedirs(cleaned_folder, exist_ok=True)
os.makedirs(documentation_folder, exist_ok=True)

cleaned_file = os.path.join(
    cleaned_folder,
    "HR_Analytics_Cleaned.csv"
)

report_file = os.path.join(
    documentation_folder,
    "02_Data_Cleaning_Report.md"
)


# STEP 3: LOAD ORIGINAL DATASET

df = pd.read_csv(raw_file)

print("\n" + "=" * 60)
print("WORKFORCE INTELLIGENCE - DATA CLEANING")
print("=" * 60)

print("\nOriginal dataset loaded successfully.")

original_rows = len(df)
original_columns = len(df.columns)

print("Original Rows:", original_rows)
print("Original Columns:", original_columns)


# STEP 4: CREATE A WORKING COPY

cleaned_df = df.copy()


# STEP 5: CHECK MISSING VALUES

print("\n1. MISSING VALUE CHECK")

missing_values = cleaned_df.isnull().sum().sum()

print("Total Missing Values:", missing_values)

if missing_values > 0:
    print("Missing values found. Please investigate before cleaning.")
    raise ValueError("Data cleaning stopped due to missing values.")


# STEP 6: CHECK AND REMOVE DUPLICATE ROWS

print("\n2. DUPLICATE ROW CHECK")

duplicate_rows = cleaned_df.duplicated().sum()

print("Duplicate Rows Found:", duplicate_rows)

if duplicate_rows > 0:
    cleaned_df = cleaned_df.drop_duplicates()
    print("Duplicate rows removed.")
else:
    print("No duplicate rows found.")


# STEP 7: CHECK EMPLOYEE NUMBER UNIQUENESS

print("\n3. EMPLOYEE NUMBER CHECK")

if "EmployeeNumber" not in cleaned_df.columns:
    raise ValueError("EmployeeNumber column is missing.")

duplicate_employee_ids = cleaned_df["EmployeeNumber"].duplicated().sum()

print("Duplicate Employee Numbers:", duplicate_employee_ids)

if duplicate_employee_ids > 0:
    raise ValueError(
        "Duplicate EmployeeNumber values found. "
        "Please investigate before continuing."
    )


# STEP 8: REMOVE EXTRA SPACES FROM TEXT COLUMNS

print("\n4. TEXT CLEANING")

text_columns = cleaned_df.select_dtypes(
    include="str"
).columns

for column in text_columns:
    cleaned_df[column] = cleaned_df[column].str.strip()

print("Extra spaces removed from text columns.")


# STEP 9: CHECK BLANK TEXT VALUES

blank_values = 0

for column in text_columns:
    blank_values += (
        cleaned_df[column].eq("").sum()
    )

print("Blank Text Values:", blank_values)

if blank_values > 0:
    raise ValueError(
        "Blank text values found. Please investigate."
    )


# STEP 10: CHECK NEGATIVE NUMERIC VALUES

print("\n5. NEGATIVE VALUE CHECK")

numeric_columns = cleaned_df.select_dtypes(
    include="number"
).columns

negative_columns = []

for column in numeric_columns:
    if (cleaned_df[column] < 0).any():
        negative_columns.append(column)

if negative_columns:
    print("Columns containing negative values:", negative_columns)
    raise ValueError(
        "Negative values found. Please investigate before continuing."
    )
else:
    print("No negative numeric values found.")


# STEP 11: CHECK EMPLOYEE TENURE CONSISTENCY

print("\n6. EMPLOYEE TENURE CHECK")

tenure_checks = {
    "YearsAtCompany": "TotalWorkingYears",
    "YearsInCurrentRole": "YearsAtCompany",
    "YearsSinceLastPromotion": "YearsAtCompany",
    "YearsWithCurrManager": "YearsAtCompany"
}

tenure_violations = 0

for column, reference_column in tenure_checks.items():

    violations = (
        cleaned_df[column] > cleaned_df[reference_column]
    ).sum()

    print(column, "Violations:", violations)

    tenure_violations += violations

if tenure_violations > 0:
    raise ValueError(
        "Tenure inconsistencies found. Please investigate."
    )


# STEP 12: REMOVE CONSTANT COLUMNS

print("\n7. CONSTANT COLUMN REMOVAL")

constant_columns = []

for column in cleaned_df.columns:

    if cleaned_df[column].nunique() == 1:
        constant_columns.append(column)

print("Constant Columns Found:", constant_columns)

cleaned_df = cleaned_df.drop(columns=constant_columns)

print("Constant columns removed.")


# STEP 13: FINAL DATASET CHECK

print("\n8. FINAL DATASET SUMMARY")

final_rows = len(cleaned_df)
final_columns = len(cleaned_df.columns)

print("Final Rows:", final_rows)
print("Final Columns:", final_columns)

print("Remaining Missing Values:", cleaned_df.isnull().sum().sum())
print("Remaining Duplicate Rows:", cleaned_df.duplicated().sum())

print("\nRemaining Columns:")
print(cleaned_df.columns.tolist())


# STEP 14: SAVE CLEANED DATASET

cleaned_df.to_csv(cleaned_file, index=False)

print("\nCleaned dataset saved successfully.")
print(cleaned_file)


# STEP 15: GENERATE CLEANING REPORT

report = []

report.append("# Data Cleaning Report")
report.append("")
report.append("## Project: Workforce Intelligence")
report.append("")
report.append("## 1. Original Dataset")
report.append("")
report.append(f"- Original Rows: {original_rows}")
report.append(f"- Original Columns: {original_columns}")
report.append("")

report.append("## 2. Data Quality Checks")
report.append("")
report.append(f"- Missing Values: {missing_values}")
report.append(f"- Duplicate Rows Found: {duplicate_rows}")
report.append(f"- Duplicate Employee Numbers: {duplicate_employee_ids}")
report.append(f"- Blank Text Values: {blank_values}")
report.append(f"- Negative Value Columns: {negative_columns}")
report.append(f"- Tenure Violations: {tenure_violations}")
report.append("")

report.append("## 3. Columns Removed")
report.append("")

for column in constant_columns:
    report.append(f"- {column}")

if not constant_columns:
    report.append("- No columns removed.")

report.append("")

report.append("## 4. Final Dataset")
report.append("")
report.append(f"- Final Rows: {final_rows}")
report.append(f"- Final Columns: {final_columns}")
report.append(
    f"- Rows Removed: {original_rows - final_rows}"
)
report.append("")

report.append("## 5. Output File")
report.append("")
report.append("`02_Cleaned_Data/HR_Analytics_Cleaned.csv`")
report.append("")

report.append("## 6. Cleaning Notes")
report.append("")
report.append(
    "- Original raw data was preserved."
)
report.append(
    "- EmployeeNumber was retained as the employee identifier."
)
report.append(
    "- Constant columns were removed because they provide no "
    "analytical value."
)
report.append(
    "- No missing values were imputed."
)

with open(report_file, "w", encoding="utf-8") as file:
    file.write("\n".join(report))


# STEP 16: COMPLETION MESSAGE

print("\nCleaning report saved at:")
print(report_file)

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 60)
