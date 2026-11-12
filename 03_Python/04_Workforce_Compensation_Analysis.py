
# ============================================================
# PROJECT 05: WORKFORCE INTELLIGENCE
# SCRIPT 04: WORKFORCE COMPENSATION ANALYSIS
# ============================================================
# Objective:
# Analyse employee compensation, salary distribution,
# salary differences, salary hikes, and stock options.
#
# Dataset:
# HR_Analytics_Cleaned.csv
#
# Important:
# Compensation comparisons are descriptive.
# Salary differences do not automatically indicate
# unfair pay because job roles, levels, and experience
# may differ between employee groups.
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
    "Compensation_Charts"
)

os.makedirs(image_folder, exist_ok=True)


# STEP 3: LOAD DATASET

df = pd.read_csv(csv_path)

print("\n" + "=" * 60)
print("WORKFORCE INTELLIGENCE - COMPENSATION ANALYSIS")
print("=" * 60)

print("\nCleaned dataset loaded successfully!")
print("Total Employees:", len(df))


# STEP 4: OVERALL SALARY ANALYSIS

print("\n1. OVERALL SALARY ANALYSIS")

print("\nMonthly Income Summary:")

print(df["MonthlyIncome"].describe().round(2))

print("\nAverage Monthly Income:")
print(round(df["MonthlyIncome"].mean(), 2))

print("\nMedian Monthly Income:")
print(round(df["MonthlyIncome"].median(), 2))

print("\nMinimum Monthly Income:")
print(df["MonthlyIncome"].min())

print("\nMaximum Monthly Income:")
print(df["MonthlyIncome"].max())


# STEP 5: SALARY BY DEPARTMENT

print("\n2. SALARY BY DEPARTMENT")

department_salary = df.groupby("Department").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Average_Monthly_Income=("MonthlyIncome", "mean"),
    Median_Monthly_Income=("MonthlyIncome", "median"),
    Minimum_Income=("MonthlyIncome", "min"),
    Maximum_Income=("MonthlyIncome", "max")
)

department_salary = department_salary.round(2)

print(department_salary)


# STEP 6: SALARY BY JOB ROLE

print("\n3. SALARY BY JOB ROLE")

job_role_salary = df.groupby("JobRole").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Average_Monthly_Income=("MonthlyIncome", "mean"),
    Median_Monthly_Income=("MonthlyIncome", "median")
)

job_role_salary = job_role_salary.round(2)

print(
    job_role_salary.sort_values(
        by="Average_Monthly_Income",
        ascending=False
    )
)


# STEP 7: SALARY BY JOB LEVEL

print("\n4. SALARY BY JOB LEVEL")

job_level_salary = df.groupby("JobLevel").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Average_Monthly_Income=("MonthlyIncome", "mean"),
    Median_Monthly_Income=("MonthlyIncome", "median")
)

job_level_salary = job_level_salary.round(2)

print(job_level_salary)


# STEP 8: GENDER-WISE SALARY COMPARISON

print("\n5. GENDER-WISE SALARY COMPARISON")

gender_salary = df.groupby("Gender").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Average_Monthly_Income=("MonthlyIncome", "mean"),
    Median_Monthly_Income=("MonthlyIncome", "median")
)

gender_salary = gender_salary.round(2)

print(gender_salary)


# STEP 9: SALARY COMPARISON BY ATTRITION

print("\n6. SALARY COMPARISON BY ATTRITION")

attrition_salary = df.groupby("Attrition").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Average_Monthly_Income=("MonthlyIncome", "mean"),
    Median_Monthly_Income=("MonthlyIncome", "median")
)

attrition_salary = attrition_salary.round(2)

print(attrition_salary)


# STEP 10: SALARY HIKE ANALYSIS

print("\n7. SALARY HIKE ANALYSIS")

salary_hike = df.groupby("PerformanceRating").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Average_Salary_Hike=("PercentSalaryHike", "mean"),
    Median_Salary_Hike=("PercentSalaryHike", "median")
)

salary_hike = salary_hike.round(2)

print(salary_hike)

print("\nSalary Hike Distribution:")

print(
    df["PercentSalaryHike"].value_counts().sort_index()
)


# STEP 11: STOCK OPTION ANALYSIS

print("\n8. STOCK OPTION ANALYSIS")

stock_option = df.groupby("StockOptionLevel").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Average_Monthly_Income=("MonthlyIncome", "mean"),
    Attrition_Count=("Attrition", lambda x: (x == "Yes").sum())
)

stock_option["Attrition_Rate_Percent"] = (
    stock_option["Attrition_Count"]
    / stock_option["Total_Employees"]
    * 100
).round(2)

stock_option["Average_Monthly_Income"] = (
    stock_option["Average_Monthly_Income"].round(2)
)

print(stock_option)


# STEP 12: OVERTIME AND MONTHLY INCOME

print("\n9. OVERTIME AND MONTHLY INCOME")

overtime_salary = df.groupby("OverTime").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Average_Monthly_Income=("MonthlyIncome", "mean"),
    Median_Monthly_Income=("MonthlyIncome", "median")
)

overtime_salary = overtime_salary.round(2)

print(overtime_salary)


# ============================================================
# STEP 13: VISUALIZATIONS
# ============================================================


# CHART 1: MONTHLY INCOME DISTRIBUTION

plt.figure(figsize=(9, 5))

plt.hist(
    df["MonthlyIncome"],
    bins=20,
    edgecolor="black"
)

plt.title("Monthly Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "01_Monthly_Income_Distribution.png")
)

plt.close()


# CHART 2: AVERAGE SALARY BY DEPARTMENT

plt.figure(figsize=(8, 5))

plt.bar(
    department_salary.index,
    department_salary["Average_Monthly_Income"]
)

plt.title("Average Monthly Income by Department")
plt.xlabel("Department")
plt.ylabel("Average Monthly Income")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "02_Salary_by_Department.png")
)

plt.close()


# CHART 3: AVERAGE SALARY BY JOB ROLE

job_role_chart = job_role_salary.sort_values(
    by="Average_Monthly_Income"
)

plt.figure(figsize=(10, 6))

plt.barh(
    job_role_chart.index,
    job_role_chart["Average_Monthly_Income"]
)

plt.title("Average Monthly Income by Job Role")
plt.xlabel("Average Monthly Income")
plt.ylabel("Job Role")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "03_Salary_by_Job_Role.png")
)

plt.close()


# CHART 4: AVERAGE SALARY BY JOB LEVEL

plt.figure(figsize=(8, 5))

plt.plot(
    job_level_salary.index,
    job_level_salary["Average_Monthly_Income"],
    marker="o"
)

plt.title("Average Monthly Income by Job Level")
plt.xlabel("Job Level")
plt.ylabel("Average Monthly Income")

plt.xticks(job_level_salary.index)

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "04_Salary_by_Job_Level.png")
)

plt.close()


# CHART 5: SALARY BY ATTRITION

plt.figure(figsize=(7, 5))

plt.bar(
    attrition_salary.index,
    attrition_salary["Average_Monthly_Income"]
)

plt.title("Average Monthly Income by Attrition Status")
plt.xlabel("Attrition")
plt.ylabel("Average Monthly Income")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "05_Salary_by_Attrition.png")
)

plt.close()


# CHART 6: SALARY HIKE BY PERFORMANCE RATING

plt.figure(figsize=(8, 5))

plt.bar(
    salary_hike.index.astype(str),
    salary_hike["Average_Salary_Hike"]
)

plt.title("Average Salary Hike by Performance Rating")
plt.xlabel("Performance Rating")
plt.ylabel("Average Salary Hike (%)")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "06_Salary_Hike_by_Performance.png")
)

plt.close()


# CHART 7: ATTRITION RATE BY STOCK OPTION LEVEL

plt.figure(figsize=(8, 5))

plt.bar(
    stock_option.index.astype(str),
    stock_option["Attrition_Rate_Percent"]
)

plt.title("Attrition Rate by Stock Option Level")
plt.xlabel("Stock Option Level")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "07_Attrition_by_Stock_Option.png")
)

plt.close()


# ============================================================
# STEP 14: FINAL MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("WORKFORCE COMPENSATION ANALYSIS COMPLETED")
print("=" * 60)

print("\nSeven compensation charts saved in:")
print(image_folder)

print("\nChart names:")

for file_name in sorted(os.listdir(image_folder)):
    print(file_name)

print("\nAll compensation analyses completed successfully.")
