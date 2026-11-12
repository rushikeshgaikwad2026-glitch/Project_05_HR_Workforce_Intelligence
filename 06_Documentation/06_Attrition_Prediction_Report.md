# Employee Attrition Prediction – Model Evaluation Report

## 1. Objective

The objective of this analysis was to develop a classification model to estimate employee attrition using employee demographic, job-related, compensation and workplace experience information.

The analysis uses Logistic Regression, a classification algorithm that estimates the probability of an employee belonging to the attrition class.

## 2. Dataset Overview

| Parameter | Details |
|---|---|
| Dataset | IBM HR Analytics Employee Attrition & Performance |
| Total records | 1,470 |
| Target variable | Attrition |
| Employees who stayed | 1,233 |
| Employees who left | 237 |
| Overall attrition rate | 16.12% |
| Input features | 30 before encoding |
| Algorithm | Logistic Regression |

The dataset is a fictional employee dataset and does not represent actual IBM employee records.

## 3. Methodology

The following steps were performed:

1. Loaded the cleaned employee dataset.
2. Converted the Attrition target into binary values:
   - No = 0
   - Yes = 1
3. Excluded EmployeeNumber because it is an employee identifier.
4. Separated numerical and categorical variables.
5. Applied StandardScaler to numerical variables.
6. Applied One-Hot Encoding to categorical variables.
7. Divided the dataset into training and testing subsets using an 80:20 split.
8. Used stratified sampling to preserve the attrition distribution.
9. Trained a Logistic Regression model with balanced class weights.
10. Evaluated the model using classification metrics and a confusion matrix.

Random state: 42.

## 4. Model Performance

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 75.17% |
| Precision – Attrition | 34.88% |
| Recall – Attrition | 63.83% |
| F1-Score – Attrition | 45.11% |
| ROC-AUC | 80.32% |

### Interpretation

- Accuracy of 75.17% represents the proportion of correct predictions across both classes.
- Precision of 34.88% means approximately 35% of employees predicted to leave actually belonged to the attrition class.
- Recall of 63.83% means the model identified 30 out of 47 actual departures in the test dataset.
- F1-score of 45.11% reflects the balance between precision and recall.
- ROC-AUC of 80.32% indicates useful discrimination between the two classes.

Accuracy should not be interpreted in isolation. A simple model predicting that every employee stayed would achieve 83.88% accuracy because the dataset is imbalanced.

## 5. Confusion Matrix

| Actual / Predicted | Predicted Stayed | Predicted Left |
|---|---:|---:|
| Actual Stayed | 191 | 56 |
| Actual Left | 17 | 30 |

### Business Interpretation

- 191 employees who stayed were correctly classified.
- 56 employees who stayed were incorrectly flagged as potential departures.
- 30 employees who left were correctly identified.
- 17 actual departures were missed.

The model identifies a portion of employees associated with attrition risk, but its false-positive predictions mean it should not be used as the sole basis for employee interventions.

## 6. Important Model Associations

The Logistic Regression coefficients highlighted the following features:

| Feature | Coefficient | Direction of Association |
|---|---:|---|
| JobRole – Research Director | -1.466 | Lower estimated attrition odds |
| JobRole – Laboratory Technician | +1.194 | Higher estimated attrition odds |
| JobRole – Sales Representative | +1.121 | Higher estimated attrition odds |
| BusinessTravel – Non-Travel | -0.994 | Lower estimated attrition odds |
| OverTime – No | -0.893 | Lower estimated attrition odds |
| BusinessTravel – Travel Frequently | +0.788 | Higher estimated attrition odds |
| OverTime – Yes | +0.762 | Higher estimated attrition odds |
| TotalWorkingYears | -0.620 | Lower estimated attrition odds |
| JobLevel | +0.607 | Higher estimated attrition odds in the fitted model |
| YearsSinceLastPromotion | +0.503 | Higher estimated attrition odds |

These coefficients describe conditional associations learned by the model. They are not causal effects.

Absolute coefficient values should not be treated as a definitive ranking of feature importance because categorical and standardised numerical features have different representations.

## 7. Business Recommendations

Based on the combined descriptive and predictive analysis:

1. Review retention challenges among Sales Representatives and Laboratory Technicians.
2. Examine overtime patterns and workload distribution.
3. Review travel expectations and support for employees who travel frequently.
4. Strengthen early-tenure onboarding and manager engagement.
5. Monitor job satisfaction and work-life balance.
6. Review career progression and promotion opportunities.

These recommendations should be investigated through further employee research rather than treated as proven solutions.

## 8. Model Limitations

- The dataset contains fictional employee records.
- It represents a single employee-data snapshot rather than a dated employment history.
- The model identifies patterns associated with the recorded attrition label; it does not establish future employee departures.
- The test dataset contains only 47 employees who left.
- Precision is relatively low, resulting in a considerable number of false-positive predictions.
- The model has not undergone extensive hyperparameter tuning or external validation.
- The model's predictions and coefficients do not establish causation.
- Balanced class weights influence the model's fitted decision boundary and coefficients.

## 9. Conclusion

The Logistic Regression model achieved a ROC-AUC of 80.32% and recall of 63.83% for the attrition class on the test dataset.

It provides a useful introductory predictive analysis and demonstrates how employee characteristics can be used to classify recorded attrition outcomes.

However, the model should be considered an exploratory classification exercise rather than a validated operational employee-retention prediction system.

Further evaluation, threshold optimisation and external validation would be required before practical deployment.
