
# ============================================================
# PROJECT 05: WORKFORCE INTELLIGENCE
# SCRIPT 09: LOAD CLEANED DATA INTO MYSQL
# ============================================================

import pandas as pd
import mysql.connector
from pathlib import Path

# ------------------------------------------------------------
# 1. DEFINE FILE PATH
# ------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent

CSV_PATH = PROJECT_DIR / "02_Cleaned_Data" / "HR_Analytics_Cleaned.csv"

# ------------------------------------------------------------
# 2. MYSQL DATABASE CONNECTION
# ------------------------------------------------------------

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vedika@12345",
    database="hr_workforce_intelligence",
    allow_local_infile=True
)

cursor = connection.cursor()

print("=" * 60)
print("WORKFORCE INTELLIGENCE - MYSQL DATA IMPORT")
print("=" * 60)

# ------------------------------------------------------------
# 3. LOAD CLEANED CSV
# ------------------------------------------------------------

df = pd.read_csv(CSV_PATH)

print(f"\nCSV loaded successfully!")
print(f"Total records: {len(df)}")
print(f"Total columns: {len(df.columns)}")

# ------------------------------------------------------------
# 4. PREPARE DATA FOR MYSQL
# ------------------------------------------------------------

# Replace pandas missing values with None
df = df.astype(object).where(pd.notna(df), None)

columns = list(df.columns)

column_names = ", ".join(f"`{column}`" for column in columns)

placeholders = ", ".join(["%s"] * len(columns))

insert_query = f"""
    INSERT INTO hr_employee_attrition ({column_names})
    VALUES ({placeholders})
"""

# ------------------------------------------------------------
# 5. INSERT DATA
# ------------------------------------------------------------

try:
    # Clear previous records to avoid duplicate imports
    cursor.execute("DELETE FROM hr_employee_attrition")

    records = [tuple(row) for row in df.itertuples(index=False, name=None)]

    cursor.executemany(insert_query, records)

    connection.commit()

    print("\nData imported successfully!")

    # --------------------------------------------------------
    # 6. VERIFY IMPORTED RECORDS
    # --------------------------------------------------------

    cursor.execute(
        "SELECT COUNT(*) FROM hr_employee_attrition"
    )

    total_records = cursor.fetchone()[0]

    print(f"\nTotal records in MySQL: {total_records}")

    if total_records == len(df):
        print("SUCCESS: CSV and MySQL record counts match.")
    else:
        print("WARNING: Record counts do not match.")

except Exception as error:
    connection.rollback()
    print(f"\nERROR: {error}")

finally:
    cursor.close()
    connection.close()

print("\nMYSQL IMPORT PROCESS COMPLETED")
