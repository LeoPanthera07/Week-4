# Day 19 AM – Logic & Explanations

## Part A

### Task 1–2: Loop vs Higher-Order Functions
- `mean_loop`: sums elements then divides — O(n), readable.
- `mean_hof`: uses `reduce` to accumulate sum. Same result, functional style.
- Variance: sum of squared deviations from mean, divided by n.
- Median: sort list, return middle element (or average of two middles for even length).

### Task 3: Filtering + Grades
- `filter(lambda x: x > avg, marks)` — keeps only above-average marks.
- List comprehension with ternary chain assigns A/B/C based on thresholds.

### Task 4: Standard Deviation
- `std = sqrt(variance)`.
- NumPy verification confirms manual result matches `np.std()`.

### Task 5: Groups A and B
- A has higher mean (25.43) and higher variance than B (mean=3.54).
- Difference in means ≈ 21.9 — suggests very different distributions.

---

## Part B: two_sample_t_test()

Formula: `t = (m1 - m2) / sqrt(v1/n1 + v2/n2)`

- This is Welch's t-test (does not assume equal variance).
- Rule of thumb: |t| > 1.96 → reject H₀ at α=0.05 (two-tailed, large samples).
- Applied on A vs B: |t| >> 1.96 → significant difference.

---

## Part C

**Q1 — Loops vs Comprehensions vs HOF**

| Method | When to use |
|--------|------------|
| Loop | Complex logic, multiple conditions, side effects |
| List comprehension | Simple transforms/filters on a single iterable |
| HOF (map/filter/reduce) | Functional pipelines, reusable lambdas |

**Q2 — Flatten + remove evens**
- Flatten: `[x for sublist in nested for x in sublist]` — double comprehension iterates nested structure.
- Remove evens: `[x for x in flat if x % 2 != 0]`.

**Q3 — Hypothesis testing**
- H₀: status quo (no effect).
- p-value: probability of observing this data if H₀ were true.
- α = 0.05: threshold. p < α → reject H₀ → result is statistically significant.

---

## Part D

AI prompt asks for descriptive stats + hypothesis testing with real-world Python.
Evaluation: output correct; suggest adding effect size (Cohen's d) and checking assumptions before t-test.
