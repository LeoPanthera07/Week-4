# Day 20 PM – Logic and Explanations

## Part A

### 1. Normal dataset
- `np.random.normal(loc, scale, size)` generates data from N(μ, σ²).
- Mean, variance, and std are computed manually using list/generator expressions.
- Histogram should show a bell shape confirming normality.

### 2. Z-score standardization
- Formula: Z = (x − μ) / σ
- After standardization, mean ≈ 0 and std ≈ 1 (verified by printing).

### 3. Outlier detection
- Z-scores are computed for each mark.
- Any mark with |Z| > 2 is flagged as a potential outlier (covers ~95% of normal distribution).

### 4. One-sample Z-test
- H₀: μ = given value (e.g., 65)
- Z-statistic: Z = (sample_mean − μ₀) / (σ / √n)
- If |Z| > 1.96, reject H₀ at α = 0.05 (two-tailed).

### 5. False positive rate simulation
- Run 1000 simulations under H₀ (mean truly = 65).
- Count how often |Z| > 1.96 (false positive).
- Result ≈ 0.05, which matches the significance level α.

---

## Part B

### Normal vs Standard Normal
- Normal: centered at any μ with any σ.
- Standard Normal: always μ = 0, σ = 1.
- Standardizing shifts the distribution without changing its shape.

### Two-group comparison
- Compute means of both groups and the difference.
- A large difference relative to spread suggests the groups are different.

### When to standardize
- Before any distance-based algorithm (KNN, SVM, K-Means).
- When features have different units or scales.
- Z-score ensures no feature dominates due to scale.

---

## Part C

### Q1. Normal vs Standard Normal
- Normal: parameterized by μ and σ.
- Standard Normal: fixed μ = 0, σ = 1.
- Standard Normal is used in Z-tables and significance testing.

### Q2. `z_score(x, mean, std)`
- Returns (x − mean) / std.
- Simple, vectorizable, and the foundation of standardization.

### Q3. Hypothesis testing
- **H₀ (null)**: default assumption (no effect, no difference).
- **H₁ (alternative)**: what we are trying to prove.
- **p-value**: probability of observing this result if H₀ is true.
- **α**: threshold for rejection; typically 0.05.
- If p < α → reject H₀.

---

## Part D

### AI evaluation
- Explanation is correct: normal distribution, Z-score, and test are described accurately.
- Code uses `scipy.stats.ttest_1samp`, which is valid.
- Improvement: manually implementing Z = (x̄ − μ₀) / (σ/√n) shows deeper understanding.

---

## Implementation Notes
- Save the code as `PM_Session.py`.
- Save this file as `PM_Session_Logic.md`.
- Run `PM_Session.py` to generate `pm_hist.png` and `pm_distributions.png`.
- Push both to GitHub and submit on LMS.


https://github.com/LeoPanthera07/Week-4/tree/60814909838cc380d65bbc89e0517ae74cac40c6/Day-20