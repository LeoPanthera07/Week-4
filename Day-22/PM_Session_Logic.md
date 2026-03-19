# Day 22 PM – Logic and Explanations

## Dataset
Reuses `students.csv` (600 rows) — score (continuous), passed (binary), study_hours, attendance, age, department, year.

---

## Part A

### Task 1: ML Problem Type
- Labels are present → **Supervised Learning**.
- `score` is continuous → **Regression**.
- `passed` is binary (0/1) → **Classification**.

### Task 2: Data handling
- `isnull().sum()` checks for missing values.
- `dropna()` removes any rows with nulls (none in synthetic data).
- Relevant features selected: age, attendance, study_hours, score, passed.

### Task 3: Manual linear regression
- Formula: `weight = Σ(x − x̄)(y − ȳ) / Σ(x − x̄)²`
- `bias = ȳ − weight × x̄`
- Prediction: `y_pred = weight * X + bias`
- MSE = mean of squared differences.
- Higher `study_hours` → higher predicted `score`.

### Task 4: Classification
- Threshold = mean score.
- If score ≥ threshold → predict passed=1.
- Accuracy = correct predictions / total.

### Task 5: Comparison table
| | Regression | Classification |
|---|---|---|
| Output | Continuous | Discrete |
| Target | score | passed (0/1) |
| Metric | MSE/RMSE | Accuracy/F1 |
| Example | Predict score | Predict pass/fail |

---

## Part B: Feature Analysis

### Correlation
- `df.corr()` computes Pearson correlation between all numeric columns.
- `study_hours` has the highest positive correlation with `score`.
- `age` has near-zero correlation — not useful for prediction.

### Feature selection
- Remove irrelevant columns like `student_id`, `department` (non-numeric/no signal).
- High-correlation features → improve model accuracy.
- Low/no correlation → add noise → can hurt generalization.

---

## Part C

### Q1. Types of Machine Learning
- **Supervised**: labelled data, predict target (regression/classification).
- **Unsupervised**: no labels, find structure (clustering, dimensionality reduction).
- **Reinforcement**: agent learns by trial-and-error using rewards.

### Q2. Filter + compute
```python
subset = df[df["score"] > df["score"].mean()]
avg_study = subset["study_hours"].mean()
```

### Q3. Regression vs Classification
- Regression → continuous output (price, temperature, score).
- Classification → discrete output (spam/ham, pass/fail, fraud/ok).

---

## Part D

### AI evaluation
- ML type definitions are correct.
- sklearn code is logically valid and runnable.
- Improvement: show a manual implementation (like the regression in Task 3) so the explanation is not purely library-dependent.

---

## Implementation Notes
- Run `PM_Session.py` to generate `pm_regression.png`.
- Dataset is created inside the script — no external CSV needed.
- Submit on LMS with GitHub link by **20/Mar/2026 · 09:15 AM**.
