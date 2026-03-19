import numpy as np
import time

np.random.seed(42)

arr_1d = np.array([10, 20, 30, 40, 50])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr_3d = np.arange(24).reshape(2, 3, 4)

print("Part A - Task 1: Indexing and slicing")
print("1D element [2]:", arr_1d[2])
print("1D slice [1:4]:", arr_1d[1:4])
print("2D row 1:", arr_2d[1])
print("2D col 2:", arr_2d[:, 2])
print("2D subarray [0:2, 0:2]:", arr_2d[0:2, 0:2])
print("3D [0, 1, :]:", arr_3d[0, 1, :])

print("
Task 2: Basic operations (no loops)")
a = np.array([1, 2, 3, 4, 5], dtype=float)
b = np.array([10, 20, 30, 40, 50], dtype=float)
print("Addition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Mean:", a.mean())
print("Variance:", a.var())
print("Std Dev:", a.std())

print("
Task 3: Broadcasting")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
row = np.array([10, 20, 30])
vec = np.array([[1], [2]])

print("2D + 1D (row broadcast):", matrix + row)
print("2D * scalar:", matrix * 5)
print("2D * col vector:", matrix * vec)
print("Broadcasting rule: shapes are aligned from trailing dim; size-1 dims expand to match.")

print("
Task 4: Vectorised operations")
data = np.array([-3, -1, 0, 2, 4, -5, 7])
print("Squares:", data ** 2)
print("Cubes:", data ** 3)
print("Replace negatives with 0:", np.where(data < 0, 0, data))
d_min, d_max = data.min(), data.max()
normalized = (data - d_min) / (d_max - d_min)
print("Normalized:", normalized.round(3))

print("
Task 5: Dataset analysis")
dataset = np.random.randint(0, 100, (5, 6))
print("Dataset:
", dataset)
flat_sorted = np.sort(dataset.flatten())[::-1]
print("Top 5 values:", flat_sorted[:5])
print("Row-wise sums:", dataset.sum(axis=1))
print("Column-wise sums:", dataset.sum(axis=0))
threshold = 60
print(f"Indices where value > {threshold}:", np.argwhere(dataset > threshold))

print("
Part B - Matrix operations")
A = np.array([[2, 3], [1, 4]])
B = np.array([[1, 0], [2, 1]])
print("Matrix multiply A @ B:", A @ B)
print("Transpose A:", A.T)
print("Determinant A:", round(np.linalg.det(A), 4))

coeff = np.array([[2, 3], [4, 1]])
rhs   = np.array([8, 10])
sol   = np.linalg.solve(coeff, rhs)
print("\nLinear system solution:", sol.round(4))
print("Verify:", np.allclose(coeff @ sol, rhs))

n = 1_000_000
big = np.random.rand(n)

t0 = time.time()
total = 0.0
for x in big:
    total += x
loop_time = time.time() - t0

t1 = time.time()
np_total = big.sum()
np_time = time.time() - t1

print(f"\nLoop time : {loop_time:.4f}s")
print(f"NumPy time: {np_time:.4f}s")
print(f"Speedup   : {loop_time / np_time:.1f}x")

def normalize(X):
    return (X - X.min()) / (X.max() - X.min())

print("\nPart C")
print("Q2 normalize([1,2,3,4,5]):", normalize(np.array([1,2,3,4,5])))

print("\nQ1")
print("Broadcasting: NumPy automatically expands smaller arrays to match larger shapes.")
print("Useful: avoids explicit loops and temporary arrays.")

print("\nQ3")
print("Vectorisation: operations applied to entire arrays using C-level loops.")
print("NumPy faster: uses BLAS/LAPACK, avoids Python interpreter overhead per element.")

print("\nPart D")
prompt = "Explain NumPy broadcasting and vectorisation with practical Python examples."
ai_output = """
Broadcasting: allows arithmetic between arrays of different shapes.
Example:
  a = np.array([[1,2,3],[4,5,6]])  # (2,3)
  b = np.array([10,20,30])          # (3,)
  a + b  # b broadcasts to (2,3)

Vectorisation: replace Python loops with NumPy array ops.
Example:
  data = np.arange(1e6)
  result = data ** 2  # vectorised
"""
print("Prompt:", prompt)
print("AI Output:", ai_output)
print("Evaluation:")
print("Examples correct and runnable.")
print("Broadcasting shape rules explained correctly.")
print("Improvement: show a case where broadcasting fails to reinforce understanding.")
