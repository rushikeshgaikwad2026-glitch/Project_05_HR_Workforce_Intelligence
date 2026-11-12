
# ============================================================
# PROJECT 05: WORKFORCE INTELLIGENCE
# SCRIPT 05: EMPLOYEE ATTRITION ANALYSIS
# ============================================================
# Objective:
# Identify workforce segments with higher employee attrition
# and explore possible patterns associated with employees
# leaving the organization.
#
# Dataset:
# HR_Analytics_Cleaned.csv
#
# Important:
# This is descriptive analysis of fictional employee data.
# Associations do not establish causes of attrition.
# ============================================================


# STEP 1: IMPORT LIBRARIES

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
    "Attrition_Charts"
)

os.makedirs(image_folder, exist_ok=True)


# STEP 3: LOAD DATASET

df = pd.read_csv(csv_path)

print("\n" + "=" * 60)
print("WORKFORCE INTELLIGENCE - ATTRITION ANALYSIS")
print("=" * 60)

print("\nDataset loaded successfully!")
print("Total Employees:", len(df))


# STEP 4: OVERALL ATTRITION ANALYSIS

print("\n1. OVERALL ATTRITION ANALYSIS")

attrition_count = df["Attrition"].value_counts()

attrition_rate = (
    df["Attrition"].value_counts(normalize=True) * 100
).round(2)

print("\nEmployee Attrition Count:")
print(attrition_count)

print("\nEmployee Attrition Percentage:")
print(attrition_rate)

print(
    "\nOverall Attrition Rate:",
    round((df["Attrition"] == "Yes").mean() * 100, 2),
    "%"
)


# STEP 5: ATTRITION BY DEPARTMENT

print("\n2. ATTRITION BY DEPARTMENT")

department_attrition = df.groupby("Department").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

department_attrition["Employees_Retained"] = (
    department_attrition["Total_Employees"]
    - department_attrition["Employees_Left"]
)

department_attrition["Attrition_Rate_Percent"] = (
    department_attrition["Employees_Left"]
    / department_attrition["Total_Employees"]
    * 100
).round(2)

print(department_attrition)


# STEP 6: ATTRITION BY JOB ROLE

print("\n3. ATTRITION BY JOB ROLE")

job_role_attrition = df.groupby("JobRole").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

job_role_attrition["Attrition_Rate_Percent"] = (
    job_role_attrition["Employees_Left"]
    / job_role_attrition["Total_Employees"]
    * 100
).round(2)

print(
    job_role_attrition.sort_values(
        by="Attrition_Rate_Percent",
        ascending=False
    )
)


# STEP 7: ATTRITION BY GENDER

print("\n4. ATTRITION BY GENDER")

gender_attrition = df.groupby("Gender").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

gender_attrition["Attrition_Rate_Percent"] = (
    gender_attrition["Employees_Left"]
    / gender_attrition["Total_Employees"]
    * 100
).round(2)

print(gender_attrition)


# STEP 8: ATTRITION BY MARITAL STATUS

print("\n5. ATTRITION BY MARITAL STATUS")

marital_attrition = df.groupby("MaritalStatus").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

marital_attrition["Attrition_Rate_Percent"] = (
    marital_attrition["Employees_Left"]
    / marital_attrition["Total_Employees"]
    * 100
).round(2)

print(marital_attrition)


# STEP 9: ATTRITION BY BUSINESS TRAVEL

print("\n6. ATTRITION BY BUSINESS TRAVEL")

travel_attrition = df.groupby("BusinessTravel").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

travel_attrition["Attrition_Rate_Percent"] = (
    travel_attrition["Employees_Left"]
    / travel_attrition["Total_Employees"]
    * 100
).round(2)

print(travel_attrition)


# STEP 10: ATTRITION BY JOB SATISFACTION

print("\n7. ATTRITION BY JOB SATISFACTION")

satisfaction_attrition = df.groupby("JobSatisfaction").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

satisfaction_attrition["Attrition_Rate_Percent"] = (
    satisfaction_attrition["Employees_Left"]
    / satisfaction_attrition["Total_Employees"]
    * 100
).round(2)

print(satisfaction_attrition)


# STEP 11: ATTRITION BY WORK-LIFE BALANCE

print("\n8. ATTRITION BY WORK-LIFE BALANCE")

worklife_attrition = df.groupby("WorkLifeBalance").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

worklife_attrition["Attrition_Rate_Percent"] = (
    worklife_attrition["Employees_Left"]
    / worklife_attrition["Total_Employees"]
    * 100
).round(2)

print(worklife_attrition)


# STEP 12: ATTRITION BY YEARS AT COMPANY

print("\n9. ATTRITION BY YEARS AT COMPANY")

df["TenureGroup"] = pd.cut(
    df["YearsAtCompany"],
    bins=[-1, 1, 3, 5, 10, 20, 50],
    labels=[
        "0-1 Years",
        "2-3 Years",
        "4-5 Years",
        "6-10 Years",
        "11-20 Years",
        "Above 20 Years"
    ]
)

tenure_attrition = df.groupby(
    "TenureGroup",
    observed=False
).agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

tenure_attrition["Attrition_Rate_Percent"] = (
    tenure_attrition["Employees_Left"]
    / tenure_attrition["Total_Employees"]
    * 100
).round(2)

print(tenure_attrition)


# STEP 13: ATTRITION BY YEARS SINCE LAST PROMOTION

print("\n10. ATTRITION BY PROMOTION HISTORY")

df["PromotionGroup"] = pd.cut(
    df["YearsSinceLastPromotion"],
    bins=[-1, 0, 2, 5, 10, 20],
    labels=[
        "0 Years",
        "1-2 Years",
        "3-5 Years",
        "6-10 Years",
        "Above 10 Years"
    ]
)

promotion_attrition = df.groupby(
    "PromotionGroup",
    observed=False
).agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

promotion_attrition["Attrition_Rate_Percent"] = (
    promotion_attrition["Employees_Left"]
    / promotion_attrition["Total_Employees"]
    * 100
).round(2)

print(promotion_attrition)


# STEP 14: ATTRITION BY ENVIRONMENT SATISFACTION

print("\n11. ATTRITION BY ENVIRONMENT SATISFACTION")

environment_attrition = df.groupby(
    "EnvironmentSatisfaction"
).agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

environment_attrition["Attrition_Rate_Percent"] = (
    environment_attrition["Employees_Left"]
    / environment_attrition["Total_Employees"]
    * 100
).round(2)

print(environment_attrition)


# ============================================================
# STEP 15: VISUALIZATIONS
# ============================================================


# CHART 1: OVERALL ATTRITION DISTRIBUTION

plt.figure(figsize=(7, 5))

attrition_count.plot(
    kind="bar"
)

plt.title("Overall Employee Attrition")
plt.xlabel("Attrition Status")
plt.ylabel("Number of Employees")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "01_Overall_Attrition.png")
)

plt.close()


# CHART 2: ATTRITION RATE BY DEPARTMENT

plt.figure(figsize=(8, 5))

plt.bar(
    department_attrition.index,
    department_attrition["Attrition_Rate_Percent"]
)

plt.title("Attrition Rate by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "02_Attrition_by_Department.png")
)

plt.close()


# CHART 3: ATTRITION RATE BY JOB ROLE

job_role_chart = job_role_attrition.sort_values(
    by="Attrition_Rate_Percent"
)

plt.figure(figsize=(10, 6))

plt.barh(
    job_role_chart.index,
    job_role_chart["Attrition_Rate_Percent"]
)

plt.title("Attrition Rate by Job Role")
plt.xlabel("Attrition Rate (%)")
plt.ylabel("Job Role")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "03_Attrition_by_Job_Role.png")
)

plt.close()


# CHART 4: ATTRITION RATE BY GENDER

plt.figure(figsize=(7, 5))

plt.bar(
    gender_attrition.index,
    gender_attrition["Attrition_Rate_Percent"]
)

plt.title("Attrition Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "04_Attrition_by_Gender.png")
)

plt.close()


# CHART 5: ATTRITION RATE BY BUSINESS TRAVEL

plt.figure(figsize=(8, 5))

plt.bar(
    travel_attrition.index,
    travel_attrition["Attrition_Rate_Percent"]
)

plt.title("Attrition Rate by Business Travel")
plt.xlabel("Business Travel")
plt.ylabel("Attrition Rate (%)")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "05_Attrition_by_Business_Travel.png")
)

plt.close()


# CHART 6: ATTRITION RATE BY JOB SATISFACTION

plt.figure(figsize=(8, 5))

plt.bar(
    satisfaction_attrition.index.astype(str),
    satisfaction_attrition["Attrition_Rate_Percent"]
)

plt.title("Attrition Rate by Job Satisfaction")
plt.xlabel("Job Satisfaction Rating")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "06_Attrition_by_Job_Satisfaction.png")
)

plt.close()


# CHART 7: ATTRITION RATE BY TENURE

plt.figure(figsize=(10, 5))

plt.bar(
    tenure_attrition.index.astype(str),
    tenure_attrition["Attrition_Rate_Percent"]
)

plt.title("Attrition Rate by Years at Company")
plt.xlabel("Years at Company")
plt.ylabel("Attrition Rate (%)")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "07_Attrition_by_Tenure.png")
)

plt.close()


# CHART 8: ATTRITION RATE BY WORK-LIFE BALANCE

plt.figure(figsize=(8, 5))

plt.bar(
    worklife_attrition.index.astype(str),
    worklife_attrition["Attrition_Rate_Percent"]
)

plt.title("Attrition Rate by Work-Life Balance")
plt.xlabel("Work-Life Balance Rating")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "08_Attrition_by_Work_Life_Balance.png")
)

plt.close()


# ============================================================
# STEP 16: FINAL MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("EMPLOYEE ATTRITION ANALYSIS COMPLETED")
print("=" * 60)

print("\nEight attrition charts saved in:")
print(image_folder)

print("\nChart names:")

for file_name in sorted(os.listdir(image_folder)):
    print(file_name)

print("\nAll attrition analyses completed successfully.")
