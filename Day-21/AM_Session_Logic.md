# Day 21 AM – Logic and Explanations

## Part A

### Task 1: Indexing and slicing
- 1D indexing: `arr[i]`, slicing: `arr[start:end]`
- 2D row: `arr[i]`, column: `arr[:, j]`, subarray: `arr[r1:r2, c1:c2]`
- 3D: `arr[depth, row, :]` selects a row at a given depth.

### Task 2: Basic operations
- All arithmetic is element-wise: `+`, `-`, `*` without any loops.
- `mean()`, `var()`, `std()` are built-in NumPy aggregations — fast C-level computation.

### Task 3: Broadcasting
- Adding `(2,3)` + `(3,)`: the 1D row is broadcast across each row of the 2D array.
- Multiplying `(2,3)` * scalar: scalar expands to match full matrix shape.
- Multiplying `(2,3)` * `(2,1)`: the column vector broadcasts across each column.
- Rule: trailing dimensions must be equal or 1.

### Task 4: Vectorised operations
- `data ** 2` and `data ** 3` apply element-wise — no loop needed.
- `np.where(data < 0, 0, data)` replaces negatives in one call.
- Normalization: `(x - min) / (max - min)` scales all values to [0, 1].

### Task 5: Dataset analysis
- `np.sort(flat)[::-1][:5]` gives top 5 values via sort and reverse slice.
- `sum(axis=1)` → row sums, `sum(axis=0)` → column sums.
- `np.argwhere(dataset > threshold)` returns indices where condition is True.

---

## Part B

### Matrix operations
- `A @ B` → matrix multiplication (dot product).
- `A.T` → transpose.
- `np.linalg.det(A)` → determinant.

### Linear system
- Express as `Ax = b`, solve with `np.linalg.solve(A, b)`.
- Verification: `np.allclose(A @ x, b)` should return True.

### Performance comparison
- Python loop iterates one element at a time via interpreter.
- NumPy uses compiled C routines (BLAS) operating on entire array.
- Expected speedup: 50–200x depending on array size.

---

## Part C

### Q1. NumPy broadcasting
- NumPy automatically stretches smaller arrays to match shapes for arithmetic.
- Avoids writing explicit loops or creating repeated copies in memory.

### Q2. normalize(X)
- Formula: `(X - X.min()) / (X.max() - X.min())`
- All values fall in [0, 1] after normalization.

### Q3. Vectorisation vs loops
- Python loops have per-element interpreter overhead.
- Vectorised NumPy calls execute at C-speed on entire arrays.
- NumPy is also memory-efficient (contiguous array layout).

---

## Part D

### AI evaluation
- Examples for broadcasting and vectorisation are correct and runnable.
- Improvement: add a failing broadcast case (e.g., shape `(2,3)` + `(2,)`) to show when it breaks.

---

## Implementation Notes
- Save as `AM_Session.py`.
- Save this file as `AM_Session_Logic.md`.
- Run the script and verify printed outputs including speedup ratio.
- Push both files to GitHub. Submit link on LMS by 19/Mar/2026 · 11:55 PM.

https://github.com/LeoPanthera07/Week-4/tree/c23a2f18faa5960788b17698d5035fbe156d99bf