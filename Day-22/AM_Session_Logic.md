# Day 22 AM – Logic and Explanations

## Dataset
Synthetic `students.csv` — 600 rows, columns: student_id, name, age, score, attendance, department, year, passed.

---

## Part A

### Task 1: loc vs iloc
- `loc` uses label-based indexing (row labels or boolean conditions + column names).
- `iloc` uses position-based indexing (integer row/col positions).
- 3 examples each to cover single row, range, and conditional selection.

### Task 2: Filtering
- Boolean conditions chained with `&` or `|`.
- Example: `df[(df["score"] > 80) & (df["attendance"] < 65)]` selects high-scorers with low attendance.

### Task 3: Descriptive statistics
- `describe()` returns count, mean, std, min, 25%, 50%, 75%, max for numeric columns.
- Mean ≈ 65 with std ≈ 15 → scores follow a normal distribution.
- Interpreting min/max helps spot data quality issues.

### Task 4: Histogram
- Score distribution is bell-shaped (normally distributed).
- Most students score between 50–80; tail extends toward 0 and 100.

### Task 5: Bar plot
- Grouped mean scores per department show relative performance.
- Easy to compare multiple categories side by side.

### Task 6: Line chart
- Average score plotted by year shows a trend (slight improvement or drop).
- Index-based trend works when no datetime column is available.

### Task 7: KDE plot
- KDE (Kernel Density Estimate) is a smoothed version of the histogram.
- Shows shape of distribution without binning artifacts.

---

## Part B

### Grouped analysis
- `groupby("department")[["score","attendance"]].mean()` gives per-department averages.
- Bar plot visualizes differences cleanly.

### KDE comparison
- Overlaying score and attendance KDE shows their distribution shapes on the same scale.
- Score is normally distributed; attendance is roughly uniform.

### Key insight
CS and IT students tend to score higher. Attendance is spread evenly but correlates weakly with score.

---

## Part C

### Q1. loc vs iloc
| | loc | iloc |
|---|---|---|
| Index type | Label / condition | Integer position |
| Example | `df.loc[0, "score"]` | `df.iloc[0, 3]` |

### Q2. Filter above average
```python
above_avg = df[df["score"] > df["score"].mean()]
```

### Q3. describe()
Returns 8 statistics per numeric column: count, mean, std, min, 25th/50th/75th percentile, max.
Useful for spotting skewed data, outliers, and scale differences between features.

---

## Part D
AI correctly identifies Pandas and Matplotlib usage.
Improvement: show KDE overlaid on histogram for comparing smoothed vs binned distribution.

---

## Implementation Notes
- Run `AM_Session.py` to generate `students.csv`, `am_charts.png`, `am_grouped_bar.png`, `am_kde_compare.png`.
- Submit on LMS with GitHub link by **20/Mar/2026 · 9:00 AM**.
