
# ============================================================
# PROJECT 05: WORKFORCE INTELLIGENCE
# STEP 8: EMPLOYEE ATTRITION PREDICTION
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# ------------------------------------------------------------
# 1. SET PROJECT PATHS
# ------------------------------------------------------------

PROJECT_PATH = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_PATH / "02_Cleaned_Data" / "HR_Analytics_Cleaned.csv"

OUTPUT_PATH = PROJECT_PATH / "06_Documentation"
IMAGE_PATH = PROJECT_PATH / "07_Images" / "Attrition_Prediction_Charts"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
IMAGE_PATH.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# 2. LOAD DATA
# ------------------------------------------------------------

df = pd.read_csv(DATA_PATH)

print("=" * 65)
print("WORKFORCE INTELLIGENCE - ATTRITION PREDICTION")
print("=" * 65)

print("\nDataset loaded successfully!")
print("Total Employees:", len(df))

# ------------------------------------------------------------
# 3. PREPARE FEATURES AND TARGET
# ------------------------------------------------------------

# Attrition is the variable we want to predict.
# Yes = 1 (employee left)
# No = 0 (employee stayed)

y = df["Attrition"].map({"Yes": 1, "No": 0})

# Remove target and employee identifier from input features.
X = df.drop(columns=["Attrition", "EmployeeNumber"])

# Separate numerical and categorical columns.
numeric_columns = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

categorical_columns = X.select_dtypes(include=["object"]).columns.tolist()

print("\nNumerical Features:", len(numeric_columns))
print("Categorical Features:", len(categorical_columns))

print("\nTarget Distribution:")
print(y.value_counts().rename(index={0: "Stayed", 1: "Left"}))

numeric_columns = X.select_dtypes(
    include=["number"]
).columns.tolist()

categorical_columns = X.select_dtypes(
    include=["object", "string"]
).columns.tolist()

# ------------------------------------------------------------
# 4. SPLIT TRAINING AND TESTING DATA
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Employees:", len(X_train))
print("Testing Employees:", len(X_test))

# ------------------------------------------------------------
# 5. PREPROCESS FEATURES
# ------------------------------------------------------------

# Scale numerical columns.
# Convert categorical columns into numerical indicators.

preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", StandardScaler(), numeric_columns),
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ]
)

# ------------------------------------------------------------
# 6. BUILD LOGISTIC REGRESSION MODEL
# ------------------------------------------------------------

model = Pipeline(
    steps=[
        ("preprocessing", preprocessor),
        (
            "classification",
            LogisticRegression(
                class_weight="balanced",
                max_iter=1000,
                random_state=42
            )
        )
    ]
)

# ------------------------------------------------------------
# 7. TRAIN MODEL
# ------------------------------------------------------------

model.fit(X_train, y_train)

print("\nModel training completed successfully!")

# ------------------------------------------------------------
# 8. MAKE PREDICTIONS
# ------------------------------------------------------------

y_pred = model.predict(X_test)

# Probability of attrition (class 1).
y_probability = model.predict_proba(X_test)[:, 1]

# ------------------------------------------------------------
# 9. EVALUATE MODEL
# ------------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred, zero_division=0)

recall = recall_score(y_test, y_pred, zero_division=0)

f1 = f1_score(y_test, y_pred, zero_division=0)

roc_auc = roc_auc_score(y_test, y_probability)

print("\n" + "=" * 65)
print("MODEL PERFORMANCE")
print("=" * 65)

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1-Score : {f1:.4f}")
print(f"ROC-AUC  : {roc_auc:.4f}")

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Stayed", "Left"],
    zero_division=0
))

# ------------------------------------------------------------
# 10. CONFUSION MATRIX
# ------------------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Stayed", "Left"]
)

display.plot(cmap="Blues", values_format="d")

plt.title("Employee Attrition Prediction - Confusion Matrix")
plt.tight_layout()

plt.savefig(
    IMAGE_PATH / "01_Confusion_Matrix.png",
    dpi=300
)

plt.close()

# ------------------------------------------------------------
# 11. FEATURE IMPORTANCE
# ------------------------------------------------------------

# Logistic Regression coefficients show the direction and
# strength of the model's learned associations.
# Positive coefficients increase estimated attrition odds;
# negative coefficients decrease them.

feature_names = model.named_steps[
    "preprocessing"
].get_feature_names_out()

coefficients = model.named_steps[
    "classification"
].coef_[0]

feature_importance = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": coefficients
})

feature_importance["Absolute_Coefficient"] = (
    feature_importance["Coefficient"].abs()
)

feature_importance = feature_importance.sort_values(
    by="Absolute_Coefficient",
    ascending=False
)

feature_importance.to_csv(
    OUTPUT_PATH / "06_Attrition_Model_Feature_Importance.csv",
    index=False
)

top_features = feature_importance.head(15).sort_values(
    by="Absolute_Coefficient"
)

plt.figure(figsize=(11, 7))

plt.barh(
    top_features["Feature"],
    top_features["Coefficient"]
)

plt.axvline(x=0, linestyle="--")

plt.title("Top 15 Attrition Model Features")
plt.xlabel("Logistic Regression Coefficient")
plt.ylabel("Feature")

plt.tight_layout()

plt.savefig(
    IMAGE_PATH / "02_Top_Features.png",
    dpi=300
)

plt.close()

# ------------------------------------------------------------
# 12. SAVE MODEL EVALUATION RESULTS
# ------------------------------------------------------------

evaluation_results = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1_Score",
        "ROC_AUC"
    ],
    "Value": [
        accuracy,
        precision,
        recall,
        f1,
        roc_auc
    ]
})

evaluation_results.to_csv(
    OUTPUT_PATH / "07_Attrition_Model_Evaluation.csv",
    index=False
)

# ------------------------------------------------------------
# 13. SAVE TEST DATA PREDICTIONS
# ------------------------------------------------------------

prediction_results = pd.DataFrame({
    "Actual_Attrition": y_test.map({
        0: "No",
        1: "Yes"
    }).values,

    "Predicted_Attrition": pd.Series(
        y_pred,
        index=y_test.index
    ).map({
        0: "No",
        1: "Yes"
    }).values,

    "Attrition_Probability_Percent": (
        y_probability * 100
    ).round(2)
}, index=y_test.index)

prediction_results.to_csv(
    OUTPUT_PATH / "08_Attrition_Test_Predictions.csv",
    index=False
)

# ------------------------------------------------------------
# 14. FINAL SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("ATTRITION PREDICTION COMPLETED SUCCESSFULLY")
print("=" * 65)

print("\nFiles saved:")
print("1. 06_Attrition_Model_Feature_Importance.csv")
print("2. 07_Attrition_Model_Evaluation.csv")
print("3. 08_Attrition_Test_Predictions.csv")
print("4. 01_Confusion_Matrix.png")
print("5. 02_Top_Features.png")

print("\nNote:")
print("Model predictions represent estimated probabilities,")
print("not certain outcomes for individual employees.")

print("\n" + "=" * 65)
