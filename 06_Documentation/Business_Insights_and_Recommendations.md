# Workforce Intelligence – Business Insights & Recommendations

> **Project 05 | HR Analytics & Decision Support Platform**  
> **Analysis:** 1,470 employee records | 32 cleaned columns | Python, SQL, Statistics, Machine Learning and Power BI

---

## 1. Executive Summary

This project analyses employee demographics, compensation, job roles, workplace experience, performance and attrition patterns using the IBM HR Analytics Employee Attrition & Performance dataset.

The objective is to identify workforce patterns, understand factors associated with employee attrition and demonstrate how HR analytics can support evidence-based workforce decisions.

### Key workforce indicators

| KPI | Result |
|---|---:|
| Total employees | 1,470 |
| Employees who stayed | 1,233 |
| Employees who left | 237 |
| Overall attrition rate | 16.12% |
| Employee retention rate | 83.88% |
| Average monthly income | 6,502.93 |

**Overall finding:** Attrition is not evenly distributed across the workforce. Differences appear across job roles, tenure, overtime, business travel, job satisfaction and other employee characteristics.

---

## 2. Department and Job Role Analysis

### Department-wise attrition

| Department | Employees | Employees Left | Attrition Rate |
|---|---:|---:|---:|
| Sales | 446 | 92 | 20.63% |
| Human Resources | 63 | 12 | 19.05% |
| Research & Development | 961 | 133 | 13.84% |

**Insights:**
- Sales has the highest department-level attrition rate at 20.63%.
- Research & Development accounts for the largest number of departures because it has the largest workforce.
- Human Resources has a relatively high attrition rate, but its smaller employee count should be considered.

### Job role-wise attrition

| Job Role | Employees | Employees Left | Attrition Rate |
|---|---:|---:|---:|
| Sales Representative | 83 | 33 | 39.76% |
| Laboratory Technician | 259 | 62 | 23.94% |
| Human Resources | 52 | 12 | 23.08% |
| Sales Executive | 326 | 57 | 17.48% |
| Research Scientist | 292 | 47 | 16.10% |
| Manufacturing Director | 145 | 10 | 6.90% |
| Healthcare Representative | 131 | 9 | 6.87% |
| Manager | 102 | 5 | 4.90% |
| Research Director | 80 | 2 | 2.50% |

**Insights:**
- Sales Representatives have the highest observed attrition rate at 39.76%.
- Laboratory Technicians are another group with relatively high attrition.
- Research Directors and Managers have comparatively low attrition rates.

**Recommendations:**
- Investigate workload, role expectations and career progression in high-attrition job roles.
- Conduct focused employee feedback reviews in Sales and Laboratory Technician teams.
- Compare retention practices across departments.

---

## 3. Compensation and Salary Intelligence

### Average monthly income

| Attrition Status | Employees | Average Monthly Income |
|---|---:|---:|
| Stayed | 1,233 | 6,832.74 |
| Left | 237 | 4,787.09 |

Employees who left had approximately 29.94% lower average monthly income than employees who stayed.

### Median monthly income

| Attrition Status | Median Monthly Income |
|---|---:|
| Stayed | 5,204 |
| Left | 3,202 |

The median comparison also shows a difference in monthly income between the two groups.

### Salary by job level

| Job Level | Average Monthly Income |
|---:|---:|
| 1 | 2,786.92 |
| 2 | 5,502.28 |
| 3 | 9,817.25 |
| 4 | 15,503.78 |
| 5 | 19,191.83 |

**Insights:**
- Average monthly income increases with job level.
- Employees who left had lower average and median monthly income than those who stayed.
- The observed salary differences do not establish that compensation alone explains attrition.

**Recommendations:**
- Review compensation progression for entry-level employees.
- Examine salary differences alongside job role, experience and tenure.
- Review internal career progression and promotion opportunities.

---

## 4. Employee Attrition and Retention Analysis

### Age group-wise attrition

| Age Group | Employees | Employees Left | Attrition Rate |
|---|---:|---:|---:|
| 18–25 | 123 | 44 | 35.77% |
| 26–35 | 606 | 116 | 19.14% |
| 36–45 | 468 | 43 | 9.19% |
| 46–55 | 226 | 26 | 11.50% |
| 56+ | 47 | 8 | 17.02% |

The youngest age group has the highest observed attrition rate. The 56+ group is comparatively small, so its rate should be interpreted cautiously.

### Tenure-wise attrition

| Tenure Group | Employees | Employees Left | Attrition Rate |
|---|---:|---:|---:|
| 0–2 Years | 342 | 102 | 29.82% |
| 3–5 Years | 434 | 60 | 13.82% |
| 6–10 Years | 448 | 55 | 12.28% |
| Above 10 Years | 246 | 20 | 8.13% |

**Insights:**
- Employees with 0–2 years of tenure have the highest attrition rate.
- This group accounts for 102 of the 237 departures, approximately 43.04%.
- Attrition generally decreases across the longer-tenure groups.

**Recommendations:**
- Strengthen onboarding and early-tenure support.
- Introduce structured manager check-ins for new employees.
- Review role clarity, training and career development during the first two years.

---

## 5. Workplace Experience and Engagement

### Overtime and attrition

| Overtime | Employees | Employees Left | Attrition Rate |
|---|---:|---:|---:|
| Yes | 416 | 127 | 30.53% |
| No | 1,054 | 110 | 10.44% |

Employees working overtime have approximately 2.92 times the observed attrition rate of employees not working overtime.

### Job satisfaction

| Satisfaction Rating | Employees | Employees Left | Attrition Rate |
|---:|---:|---:|---:|
| 1 | 289 | 66 | 22.84% |
| 2 | 280 | 46 | 16.43% |
| 3 | 442 | 73 | 16.52% |
| 4 | 459 | 52 | 11.33% |

### Work-life balance

| Rating | Employees | Employees Left | Attrition Rate |
|---:|---:|---:|---:|
| 1 | 80 | 25 | 31.25% |
| 2 | 344 | 58 | 16.86% |
| 3 | 893 | 127 | 14.22% |
| 4 | 153 | 27 | 17.65% |

### Business travel

| Travel Frequency | Employees | Employees Left | Attrition Rate |
|---|---:|---:|---:|
| Travel Frequently | 277 | 69 | 24.91% |
| Travel Rarely | 1,043 | 156 | 14.96% |
| Non-Travel | 150 | 12 | 8.00% |

**Insights:**
- Overtime employees have a substantially higher observed attrition rate.
- Employees with the lowest job satisfaction rating have higher attrition than employees with the highest rating.
- The lowest work-life balance group has the highest attrition rate, although it contains only 80 employees.
- Frequent business travellers have a higher observed attrition rate than non-travellers.

**Recommendations:**
- Review overtime allocation and workload distribution.
- Investigate employee concerns through satisfaction surveys and feedback.
- Examine travel schedules and support for frequent travellers.
- Monitor work-life balance and employee engagement across teams.

---

## 6. Performance and Career Development

### Performance rating and attrition

| Performance Rating | Employees | Employees Left | Attrition Rate |
|---:|---:|---:|---:|
| 3 | 1,244 | 200 | 16.08% |
| 4 | 226 | 37 | 16.37% |

Attrition rates are almost identical across the two performance ratings. Performance rating alone does not appear to distinguish employees who leave from those