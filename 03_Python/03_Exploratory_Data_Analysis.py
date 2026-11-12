
# ============================================================
# PROJECT 05: WORKFORCE INTELLIGENCE
# SCRIPT 03: EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================
# Objective:
# Explore employee demographics, workforce distribution,
# compensation, experience, and attrition patterns.
#
# Dataset:
# HR_Analytics_Cleaned.csv
#
# Important:
# This dataset contains fictional employee records.
# Findings are descriptive and do not prove causation.
# ============================================================


# STEP 1: IMPORT REQUIRED LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt
import os


# STEP 2: DEFINE FILE PATHS

project_folder = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

csv_path = os.path.join(
    project_folder,
    "02_Cleaned_Data",
    "HR_Analytics_Cleaned.csv"
)

image_folder = os.path.join(
    project_folder,
    "07_Images",
    "EDA_Charts"
)

os.makedirs(image_folder, exist_ok=True)


# STEP 3: LOAD CLEANED DATASET

df = pd.read_csv(csv_path)

print("\n" + "=" * 60)
print("WORKFORCE INTELLIGENCE - EXPLORATORY DATA ANALYSIS")
print("=" * 60)

print("\nCleaned dataset loaded successfully!")

print("Total Employees:", len(df))
print("Total Columns:", len(df.columns))


# STEP 4: EMPLOYEE DEMOGRAPHICS

print("\n1. EMPLOYEE DEMOGRAPHICS")

print("\nAverage Employee Age:")
print(round(df["Age"].mean(), 2))

print("\nAge Distribution:")
print(df["Age"].describe())

print("\nGender Distribution:")
print(df["Gender"].value_counts())

print("\nMarital Status Distribution:")
print(df["MaritalStatus"].value_counts())


# STEP 5: WORKFORCE DISTRIBUTION

print("\n2. WORKFORCE DISTRIBUTION")

print("\nDepartment Distribution:")
print(df["Department"].value_counts())

print("\nJob Role Distribution:")
print(df["JobRole"].value_counts())

print("\nBusiness Travel Distribution:")
print(df["BusinessTravel"].value_counts())


# STEP 6: EXPERIENCE ANALYSIS

print("\n3. EMPLOYEE EXPERIENCE ANALYSIS")

print(
    "Average Total Working Years:",
    round(df["TotalWorkingYears"].mean(), 2)
)

print(
    "Average Years at Company:",
    round(df["YearsAtCompany"].mean(), 2)
)

print(
    "Average Years in Current Role:",
    round(df["YearsInCurrentRole"].mean(), 2)
)

print(
    "Average Years with Current Manager:",
    round(df["YearsWithCurrManager"].mean(), 2)
)


# STEP 7: COMPENSATION ANALYSIS

print("\n4. COMPENSATION ANALYSIS")

print(
    "Average Monthly Income:",
    round(df["MonthlyIncome"].mean(), 2)
)

print(
    "Median Monthly Income:",
    round(df["MonthlyIncome"].median(), 2)
)

print(
    "Minimum Monthly Income:",
    df["MonthlyIncome"].min()
)

print(
    "Maximum Monthly Income:",
    df["MonthlyIncome"].max()
)


# STEP 8: ATTRITION ANALYSIS

print("\n5. ATTRITION ANALYSIS")

attrition_count = df["Attrition"].value_counts()

print("\nAttrition Count:")
print(attrition_count)

attrition_percentage = (
    df["Attrition"].value_counts(normalize=True) * 100
).round(2)

print("\nAttrition Percentage:")
print(attrition_percentage)


# STEP 9: ATTRITION BY DEPARTMENT

print("\n6. ATTRITION BY DEPARTMENT")

department_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"]
)

department_attrition["Total Employees"] = (
    department_attrition.sum(axis=1)
)

department_attrition["Attrition Rate (%)"] = (
    department_attrition["Yes"]
    / department_attrition["Total Employees"]
    * 100
).round(2)

print(department_attrition)


# STEP 10: ATTRITION BY JOB ROLE

print("\n7. ATTRITION BY JOB ROLE")

job_role_attrition = df.groupby("JobRole").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

job_role_attrition["Attrition_Rate_Percent"] = (
    job_role_attrition["Employees_Left"]
    / job_role_attrition["Total_Employees"]
    * 100
).round(2)

print(job_role_attrition.sort_values(
    by="Attrition_Rate_Percent",
    ascending=False
))


# STEP 11: ATTRITION BY OVERTIME

print("\n8. ATTRITION BY OVERTIME")

overtime_attrition = pd.crosstab(
    df["OverTime"],
    df["Attrition"],
    normalize="index"
) * 100

print(overtime_attrition.round(2))


# STEP 12: ATTRITION BY AGE GROUP

print("\n9. ATTRITION BY AGE GROUP")

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 65],
    labels=[
        "18-25",
        "26-35",
        "36-45",
        "46-55",
        "56-65"
    ]
)

age_attrition = df.groupby(
    "AgeGroup",
    observed=False
).agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

age_attrition["Attrition_Rate_Percent"] = (
    age_attrition["Employees_Left"]
    / age_attrition["Total_Employees"]
    * 100
).round(2)

print(age_attrition)


# STEP 13: VISUALIZATION 1 - AGE DISTRIBUTION

plt.figure(figsize=(9, 5))

plt.hist(
    df["Age"],
    bins=15,
    edgecolor="black"
)

plt.title("Employee Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "01_Age_Distribution.png")
)

plt.close()


# STEP 14: VISUALIZATION 2 - DEPARTMENT DISTRIBUTION

department_counts = df["Department"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    department_counts.index,
    department_counts.values
)

plt.title("Employee Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "02_Department_Distribution.png")
)

plt.close()


# STEP 15: VISUALIZATION 3 - ATTRITION BY DEPARTMENT

department_rate = (
    df.groupby("Department")
    .apply(
        lambda x: (x["Attrition"] == "Yes").mean() * 100,
        include_groups=False
    )
)

plt.figure(figsize=(8, 5))

plt.bar(
    department_rate.index,
    department_rate.values
)

plt.title("Attrition Rate by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "03_Attrition_by_Department.png")
)

plt.close()


# STEP 16: VISUALIZATION 4 - ATTRITION BY OVERTIME

overtime_rate = (
    df.groupby("OverTime")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

plt.figure(figsize=(7, 5))

plt.bar(
    overtime_rate.index,
    overtime_rate.values
)

plt.title("Attrition Rate by Overtime")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "04_Attrition_by_Overtime.png")
)

plt.close()


# STEP 17: VISUALIZATION 5 - MONTHLY INCOME DISTRIBUTION

plt.figure(figsize=(9, 5))

plt.hist(
    df["MonthlyIncome"],
    bins=20,
    edgecolor="black"
)

plt.title("Employee Monthly Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "05_Monthly_Income_Distribution.png")
)

plt.close()


# STEP 18: VISUALIZATION 6 - ATTRITION BY JOB ROLE

job_role_rate = (
    df.groupby("JobRole")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values()
)

plt.figure(figsize=(10, 6))

plt.barh(
    job_role_rate.index,
    job_role_rate.values
)

plt.title("Attrition Rate by Job Role")
plt.xlabel("Attrition Rate (%)")
plt.ylabel("Job Role")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "06_Attrition_by_Job_Role.png")
)

plt.close()


# STEP 19: VISUALIZATION 7 - YEARS AT COMPANY

plt.figure(figsize=(9, 5))

plt.hist(
    df["YearsAtCompany"],
    bins=15,
    edgecolor="black"
)

plt.title("Employee Tenure Distribution")
plt.xlabel("Years at Company")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "07_Employee_Tenure_Distribution.png")
)

plt.close()


# STEP 20: FINAL MESSAGE

print("\n" + "=" * 60)
print("EXPLORATORY DATA ANALYSIS COMPLETED")
print("=" * 60)

print("\nSeven charts saved successfully in:")
print(image_folder)

print("\nChart names:")

for file_name in sorted(os.listdir(image_folder)):
    print(file_name)

print("\nAll analysis results displayed successfully.")