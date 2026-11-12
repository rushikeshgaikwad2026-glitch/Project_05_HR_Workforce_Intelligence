
# ============================================================
# PROJECT 05: WORKFORCE INTELLIGENCE
# SCRIPT 01: DATA UNDERSTANDING
# ============================================================
# Objective:
# Understand the structure, quality, and characteristics
# of the IBM HR Analytics Employee Attrition dataset.
#
# Important:
# This dataset contains fictional employee records.
# It is used as a workforce analytics case study and does
# not represent actual IBM employee information.
# ============================================================


# STEP 1: IMPORT REQUIRED LIBRARIES

import pandas as pd
import os


# STEP 2: DEFINE PROJECT FILE PATHS

# Get the main project folder
project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define raw dataset path
csv_path = os.path.join(
    project_folder,
    "01_Raw_Data",
    "01_IBM_HR_Analytics",
    "WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# Define documentation report path
report_folder = os.path.join(project_folder, "06_Documentation")

os.makedirs(report_folder, exist_ok=True)

report_path = os.path.join(
    report_folder,
    "01_Data_Understanding_Report.md"
)


# STEP 3: LOAD THE DATASET

df = pd.read_csv(csv_path)

print("\n" + "=" * 60)
print("WORKFORCE INTELLIGENCE - DATA UNDERSTANDING")
print("=" * 60)

print("\nDataset loaded successfully!")


# STEP 4: BASIC DATASET INFORMATION

print("\n1. DATASET DIMENSIONS")

print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])


# STEP 5: COLUMN INFORMATION

print("\n2. COLUMN NAMES")

for column in df.columns:
    print(column)


# STEP 6: DATA TYPES

print("\n3. DATA TYPES")

print(df.dtypes)


# STEP 7: FIRST FIVE RECORDS

print("\n4. FIRST FIVE RECORDS")

print(df.head())


# STEP 8: DATASET SUMMARY

print("\n5. NUMERICAL DATA SUMMARY")

print(df.describe())


# STEP 9: MISSING VALUE ANALYSIS

print("\n6. MISSING VALUE ANALYSIS")

missing_values = df.isnull().sum()

print(missing_values[missing_values > 0])

print("Total Missing Values:", df.isnull().sum().sum())


# STEP 10: DUPLICATE ANALYSIS

print("\n7. DUPLICATE ANALYSIS")

print("Duplicate Rows:", df.duplicated().sum())

if "EmployeeNumber" in df.columns:
    print(
        "Duplicate Employee Numbers:",
        df["EmployeeNumber"].duplicated().sum()
    )


# STEP 11: UNIQUE VALUES IN CATEGORICAL COLUMNS

print("\n8. CATEGORICAL COLUMN ANALYSIS")

categorical_columns = df.select_dtypes(
    include="str"
).columns

for column in categorical_columns:
    print("\n", column)
    print(df[column].value_counts())


# STEP 12: CONSTANT COLUMN ANALYSIS

print("\n9. CONSTANT COLUMN ANALYSIS")

constant_columns = []

for column in df.columns:
    if df[column].nunique() == 1:
        constant_columns.append(column)

print("Constant Columns:", constant_columns)


# STEP 13: EMPLOYEE ATTRITION DISTRIBUTION

print("\n10. EMPLOYEE ATTRITION DISTRIBUTION")

if "Attrition" in df.columns:
    print(df["Attrition"].value_counts())

    print("\nAttrition Percentage:")

    print(
        (df["Attrition"].value_counts(normalize=True) * 100).round(2)
    )


# STEP 14: NUMERICAL COLUMN ANALYSIS

print("\n11. NUMERICAL COLUMNS")

numerical_columns = df.select_dtypes(
    include=["int64", "float64"]
).columns

print("Total Numerical Columns:", len(numerical_columns))

for column in numerical_columns:
    print(
        column,
        "| Minimum:", df[column].min(),
        "| Maximum:", df[column].max(),
        "| Unique Values:", df[column].nunique()
    )


# STEP 15: GENERATE DATA UNDERSTANDING REPORT

report = []

report.append("# Data Understanding Report")
report.append("")
report.append("## Project: Workforce Intelligence")
report.append("")
report.append(
    "Dataset: IBM HR Analytics Employee Attrition & Performance"
)
report.append("")
report.append(
    "**Data note:** The dataset contains fictional employee "
    "records and is used only as an analytical case study."
)
report.append("")

report.append("## 1. Dataset Overview")
report.append("")
report.append(f"- Total Records: {df.shape[0]}")
report.append(f"- Total Columns: {df.shape[1]}")
report.append(
    f"- Numerical Columns: {len(numerical_columns)}"
)
report.append(
    f"- Categorical Columns: {len(categorical_columns)}"
)
report.append("")

report.append("## 2. Data Quality")
report.append("")
report.append(
    f"- Missing Values: {df.isnull().sum().sum()}"
)
report.append(
    f"- Duplicate Rows: {df.duplicated().sum()}"
)

if "EmployeeNumber" in df.columns:
    report.append(
        "- Duplicate Employee Numbers: "
        + str(df["EmployeeNumber"].duplicated().sum())
    )

report.append("")

report.append("## 3. Constant Columns")
report.append("")

if constant_columns:
    for column in constant_columns:
        report.append(f"- {column}")
else:
    report.append("- No constant columns found.")

report.append("")

report.append("## 4. Attrition Distribution")
report.append("")

if "Attrition" in df.columns:
    attrition_counts = df["Attrition"].value_counts()
    attrition_percentages = (
        df["Attrition"].value_counts(normalize=True) * 100
    ).round(2)

    for category in attrition_counts.index:
        report.append(
            f"- {category}: {attrition_counts[category]} "
            f"employees ({attrition_percentages[category]}%)"
        )

report.append("")

report.append("## 5. Dataset Limitations")
report.append("")
report.append(
    "- The dataset contains fictional employee records."
)
report.append(
    "- It represents a single employee-data snapshot."
)
report.append(
    "- It does not contain actual recruitment funnel or "
    "time-to-hire information."
)
report.append(
    "- It does not provide historical monthly or yearly "
    "workforce changes."
)
report.append(
    "- It cannot establish the causes of employee attrition "
    "on its own."
)
report.append("")

report.append("## 6. Next Step")
report.append("")
report.append(
    "Proceed to data cleaning after reviewing the data "
    "quality findings."
)


# SAVE REPORT

with open(report_path, "w", encoding="utf-8") as file:
    file.write("\n".join(report))


# STEP 16: FINAL MESSAGE

print("\n" + "=" * 60)
print("DATA UNDERSTANDING COMPLETED")
print("=" * 60)

print("\nReport saved at:")
print(report_path)
