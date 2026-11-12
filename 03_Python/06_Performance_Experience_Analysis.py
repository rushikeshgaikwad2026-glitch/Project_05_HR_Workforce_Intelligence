
# ============================================================
# PROJECT 05: WORKFORCE INTELLIGENCE
# SCRIPT 06: PERFORMANCE & EXPERIENCE ANALYSIS
# ============================================================
# Objective:
# Analyse employee performance, satisfaction, training,
# career development, and workplace experience.
#
# Dataset:
# HR_Analytics_Cleaned.csv
#
# Important:
# This dataset contains fictional employee records.
# Associations do not establish causation.
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
    "Performance_Experience_Charts"
)

os.makedirs(image_folder, exist_ok=True)


# STEP 3: LOAD DATASET

df = pd.read_csv(csv_path)

print("\n" + "=" * 60)
print("WORKFORCE INTELLIGENCE - PERFORMANCE & EXPERIENCE ANALYSIS")
print("=" * 60)

print("\nDataset loaded successfully!")
print("Total Employees:", len(df))


# STEP 4: PERFORMANCE RATING ANALYSIS

print("\n1. PERFORMANCE RATING ANALYSIS")

performance_analysis = df.groupby("PerformanceRating").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Average_Salary_Hike=("PercentSalaryHike", "mean"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

performance_analysis["Attrition_Rate_Percent"] = (
    performance_analysis["Employees_Left"]
    / performance_analysis["Total_Employees"]
    * 100
).round(2)

print(performance_analysis.round(2))


# STEP 5: JOB INVOLVEMENT ANALYSIS

print("\n2. JOB INVOLVEMENT ANALYSIS")

job_involvement = df.groupby("JobInvolvement").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Average_Monthly_Income=("MonthlyIncome", "mean"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

job_involvement["Attrition_Rate_Percent"] = (
    job_involvement["Employees_Left"]
    / job_involvement["Total_Employees"]
    * 100
).round(2)

print(job_involvement.round(2))


# STEP 6: JOB SATISFACTION ANALYSIS

print("\n3. JOB SATISFACTION ANALYSIS")

job_satisfaction = df.groupby("JobSatisfaction").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

job_satisfaction["Attrition_Rate_Percent"] = (
    job_satisfaction["Employees_Left"]
    / job_satisfaction["Total_Employees"]
    * 100
).round(2)

print(job_satisfaction)


# STEP 7: ENVIRONMENT SATISFACTION ANALYSIS

print("\n4. ENVIRONMENT SATISFACTION ANALYSIS")

environment_satisfaction = df.groupby(
    "EnvironmentSatisfaction"
).agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

environment_satisfaction["Attrition_Rate_Percent"] = (
    environment_satisfaction["Employees_Left"]
    / environment_satisfaction["Total_Employees"]
    * 100
).round(2)

print(environment_satisfaction)


# STEP 8: RELATIONSHIP SATISFACTION ANALYSIS

print("\n5. RELATIONSHIP SATISFACTION ANALYSIS")

relationship_satisfaction = df.groupby(
    "RelationshipSatisfaction"
).agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

relationship_satisfaction["Attrition_Rate_Percent"] = (
    relationship_satisfaction["Employees_Left"]
    / relationship_satisfaction["Total_Employees"]
    * 100
).round(2)

print(relationship_satisfaction)


# STEP 9: WORK-LIFE BALANCE ANALYSIS

print("\n6. WORK-LIFE BALANCE ANALYSIS")

worklife_analysis = df.groupby("WorkLifeBalance").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

worklife_analysis["Attrition_Rate_Percent"] = (
    worklife_analysis["Employees_Left"]
    / worklife_analysis["Total_Employees"]
    * 100
).round(2)

print(worklife_analysis)


# STEP 10: TRAINING ANALYSIS

print("\n7. TRAINING ANALYSIS")

training_analysis = df.groupby("TrainingTimesLastYear").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Average_Performance_Rating=("PerformanceRating", "mean"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

training_analysis["Attrition_Rate_Percent"] = (
    training_analysis["Employees_Left"]
    / training_analysis["Total_Employees"]
    * 100
).round(2)

print(training_analysis.round(2))


# STEP 11: CAREER PROGRESSION ANALYSIS

print("\n8. CAREER PROGRESSION ANALYSIS")

career_analysis = df.groupby("JobLevel").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Average_Years_At_Company=("YearsAtCompany", "mean"),
    Average_Years_In_Current_Role=("YearsInCurrentRole", "mean"),
    Average_Years_Since_Promotion=("YearsSinceLastPromotion", "mean"),
    Average_Years_With_Manager=("YearsWithCurrManager", "mean")
)

print(career_analysis.round(2))


# STEP 12: ATTRITION BY JOB LEVEL

print("\n9. ATTRITION BY JOB LEVEL")

job_level_attrition = df.groupby("JobLevel").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

job_level_attrition["Attrition_Rate_Percent"] = (
    job_level_attrition["Employees_Left"]
    / job_level_attrition["Total_Employees"]
    * 100
).round(2)

print(job_level_attrition)


# STEP 13: MANAGER TENURE ANALYSIS

print("\n10. MANAGER TENURE ANALYSIS")

manager_analysis = df.groupby("YearsWithCurrManager").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

manager_analysis["Attrition_Rate_Percent"] = (
    manager_analysis["Employees_Left"]
    / manager_analysis["Total_Employees"]
    * 100
).round(2)

print(manager_analysis)


# ============================================================
# STEP 14: VISUALIZATIONS
# ============================================================


# CHART 1: PERFORMANCE RATING DISTRIBUTION

plt.figure(figsize=(8, 5))

performance_counts = df["PerformanceRating"].value_counts().sort_index()

plt.bar(
    performance_counts.index.astype(str),
    performance_counts.values
)

plt.title("Employee Performance Rating Distribution")
plt.xlabel("Performance Rating")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "01_Performance_Rating_Distribution.png")
)

plt.close()


# CHART 2: ATTRITION BY JOB INVOLVEMENT

plt.figure(figsize=(8, 5))

plt.bar(
    job_involvement.index.astype(str),
    job_involvement["Attrition_Rate_Percent"]
)

plt.title("Attrition Rate by Job Involvement")
plt.xlabel("Job Involvement Rating")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "02_Attrition_by_Job_Involvement.png")
)

plt.close()


# CHART 3: ATTRITION BY JOB SATISFACTION

plt.figure(figsize=(8, 5))

plt.bar(
    job_satisfaction.index.astype(str),
    job_satisfaction["Attrition_Rate_Percent"]
)

plt.title("Attrition Rate by Job Satisfaction")
plt.xlabel("Job Satisfaction Rating")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "03_Attrition_by_Job_Satisfaction.png")
)

plt.close()


# CHART 4: ATTRITION BY ENVIRONMENT SATISFACTION

plt.figure(figsize=(8, 5))

plt.bar(
    environment_satisfaction.index.astype(str),
    environment_satisfaction["Attrition_Rate_Percent"]
)

plt.title("Attrition Rate by Environment Satisfaction")
plt.xlabel("Environment Satisfaction Rating")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "04_Attrition_by_Environment_Satisfaction.png")
)

plt.close()


# CHART 5: ATTRITION BY WORK-LIFE BALANCE

plt.figure(figsize=(8, 5))

plt.bar(
    worklife_analysis.index.astype(str),
    worklife_analysis["Attrition_Rate_Percent"]
)

plt.title("Attrition Rate by Work-Life Balance")
plt.xlabel("Work-Life Balance Rating")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "05_Attrition_by_Work_Life_Balance.png")
)

plt.close()


# CHART 6: TRAINING DISTRIBUTION

plt.figure(figsize=(8, 5))

training_counts = df["TrainingTimesLastYear"].value_counts().sort_index()

plt.bar(
    training_counts.index.astype(str),
    training_counts.values
)

plt.title("Training Sessions in the Last Year")
plt.xlabel("Number of Training Sessions")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "06_Training_Distribution.png")
)

plt.close()


# CHART 7: ATTRITION BY JOB LEVEL

plt.figure(figsize=(8, 5))

plt.bar(
    job_level_attrition.index.astype(str),
    job_level_attrition["Attrition_Rate_Percent"]
)

plt.title("Attrition Rate by Job Level")
plt.xlabel("Job Level")
plt.ylabel("Attrition Rate (%)")

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "07_Attrition_by_Job_Level.png")
)

plt.close()


# CHART 8: CAREER PROGRESSION BY JOB LEVEL

plt.figure(figsize=(9, 5))

plt.plot(
    career_analysis.index,
    career_analysis["Average_Years_At_Company"],
    marker="o",
    label="Years at Company"
)

plt.plot(
    career_analysis.index,
    career_analysis["Average_Years_In_Current_Role"],
    marker="o",
    label="Years in Current Role"
)

plt.title("Career Experience by Job Level")
plt.xlabel("Job Level")
plt.ylabel("Average Years")

plt.legend()

plt.tight_layout()

plt.savefig(
    os.path.join(image_folder, "08_Career_Experience_by_Job_Level.png")
)

plt.close()


# ============================================================
# STEP 15: FINAL MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("PERFORMANCE & EXPERIENCE ANALYSIS COMPLETED")
print("=" * 60)

print("\nEight charts saved in:")
print(image_folder)

print("\nChart names:")

for file_name in sorted(os.listdir(image_folder)):
    print(file_name)

print("\nAll performance and experience analyses completed.")
