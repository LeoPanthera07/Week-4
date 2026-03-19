# Day 21 PM – Logic and Explanations

## Part A

### Task 1: Synthetic datasets
- Regression: `y = 3x + 7 + noise` — continuous target.
- Classification: binary label derived from threshold on a normal random variable.

### Task 2: Visualize and fit
- `np.polyfit(X, y, 1)` fits a degree-1 polynomial (linear model).
- `np.polyval(m, X)` evaluates it for plotting.

### Task 3: Problem type
- Continuous float target → regression.
- Discrete/categorical target → classification.

### Task 4: Manual MSE
- Linear prediction: `y_pred = w * X + b`
- MSE = mean of squared differences between true and predicted values.

### Task 5: Classification accuracy
- Simple threshold: if X >= 0, predict class 1; else class 0.
- Accuracy = correct predictions / total predictions.

### Task 6: Comparison
| | Regression | Classification |
|---|---|---|
| Output | Continuous | Discrete |
| Metric | MSE, RMSE | Accuracy, F1 |
| Example | Price prediction | Spam detection |

---

## Part B: Bias-Variance Tradeoff

### Polynomial degrees
- Degree 1: straight line, cannot capture curve → **high bias, underfitting**.
- Degree 2: captures curve, generalises well → **balanced**.
- Degree 5: fits noise, wiggly → **high variance, overfitting**.

### Concepts
- **Bias**: error from overly simple model; misses true signal.
- **Variance**: error from oversensitivity to training data; fails on new data.
- **Optimal model**: lowest combined bias and variance (sweet spot).

---

## Part C

### Q1. Regression vs Classification
- Regression: predicts a quantity (house price, demand).
- Classification: predicts a category (fraud/not, disease/healthy).

### Q2. calculate_mse(y_true, y_pred)
- Formula: mean of (y_true − y_pred)²
- Single NumPy line, no loops.

### Q3. Bias-Variance
- Underfitting: high bias, low variance. Model ignores data patterns.
- Overfitting: low bias, high variance. Model memorises training noise.
- Goal: find the model complexity where test error is minimised.

---

## Part D

### AI evaluation
- Regression vs classification explanation is correct.
- Bias-variance framing is accurate.
- Improvement: AI should plot test error alongside train error to properly demonstrate overfitting at high polynomial degree.

---

## Implementation Notes
- Save as `PM_Session.py`.
- Save this file as `PM_Session_Logic.md`.
- Run the script to generate `pm_regression.png` and `pm_bias_variance.png`.
- Push both files to GitHub. Submit link on LMS by 19/Mar/2026 · 11:55 PM.

https://github.com/LeoPanthera07/Week-4/tree/c23a2f18faa5960788b17698d5035fbe156d99bf