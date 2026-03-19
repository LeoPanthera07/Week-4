import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data = np.random.normal(loc=60, scale=10, size=1000)

mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)
std = variance ** 0.5

print("Part A")
print(f"Mean    : {mean:.4f}")
print(f"Variance: {variance:.4f}")
print(f"Std Dev : {std:.4f}")

plt.hist(data, bins=30, edgecolor="white")
plt.title("Normal Distribution (μ=60, σ=10)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("pm_hist.png", dpi=150, bbox_inches="tight")
plt.show()

z_scores = [(x - mean) / std for x in data]
z_arr = np.array(z_scores)
print(f"\nZ-score mean: {z_arr.mean():.4f}  std: {z_arr.std():.4f}")

marks = [45, 72, 88, 55, 63, 91, 39, 76, 82, 50, 94, 100, 10]
m_mean = sum(marks) / len(marks)
m_var  = sum((x - m_mean) ** 2 for x in marks) / len(marks)
m_std  = m_var ** 0.5
m_med  = sorted(marks)[len(marks) // 2]
z_marks = [(x - m_mean) / m_std for x in marks]

print("\nStudent marks analysis")
print(f"Mean    : {m_mean:.2f}")
print(f"Median  : {m_med}")
print(f"Variance: {m_var:.2f}")
print(f"Std Dev : {m_std:.2f}")
print("Outliers (|Z| > 2):", [marks[i] for i, z in enumerate(z_marks) if abs(z) > 2])

pop_mean = 65
z_stat = (m_mean - pop_mean) / (m_std / len(marks) ** 0.5)
print(f"\nOne-sample Z-test: H0: μ = {pop_mean}")
print(f"Z-statistic: {z_stat:.4f}")
print("Reject H0" if abs(z_stat) > 1.96 else "Fail to reject H0")

false_positives = 0
n_sim = 1000
for _ in range(n_sim):
    sample = np.random.normal(loc=65, scale=10, size=30)
    s_mean = sample.mean()
    s_std  = sample.std()
    z = (s_mean - 65) / (s_std / 30 ** 0.5)
    if abs(z) > 1.96:
        false_positives += 1

fpr = false_positives / n_sim
print(f"\nFalse positive rate: {fpr:.3f}  (expected ~0.05)")

print("\nPart B")
normal_s  = np.random.normal(loc=50, scale=15, size=1000)
z_normal  = (normal_s - normal_s.mean()) / normal_s.std()

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(normal_s, bins=30, edgecolor="white")
axes[0].set_title(f"Normal  mean={normal_s.mean():.1f} std={normal_s.std():.1f}")
axes[1].hist(z_normal, bins=30, edgecolor="white")
axes[1].set_title(f"Standard Normal  mean={z_normal.mean():.2f} std={z_normal.std():.2f}")
plt.savefig("pm_distributions.png", dpi=150, bbox_inches="tight")
plt.show()

group_a = np.random.normal(60, 10, 100)
group_b = np.random.normal(55, 10, 100)
diff    = group_a.mean() - group_b.mean()
print(f"\nGroup A mean: {group_a.mean():.2f}  Group B mean: {group_b.mean():.2f}")
print(f"Difference in means: {diff:.2f}")
print("Groups appear different" if abs(diff) > 3 else "Groups appear similar")

def z_score(x, mean, std):
    return (x - mean) / std

print("\nPart C")
print("z_score(75, 60, 10):", round(z_score(75, 60, 10), 4))

dataset = np.random.normal(60, 10, 100)
zs = [round(z_score(x, dataset.mean(), dataset.std()), 2) for x in dataset]
print("Z-scores sample:", zs[:5])

print("\nQ1")
print("Normal: any μ and σ. Standard Normal: μ=0, σ=1.")
print("Standardizing shifts and scales data to N(0,1).")

print("\nQ3")
print("Null hypothesis H0: assumption of no effect.")
print("Alternative H1: there is an effect.")
print("p-value: probability of observing result under H0.")
print("α=0.05: if p < α, reject H0.")

print("\nPart D")
prompt = "Explain normal distribution, Z-score, and hypothesis testing with a simple Python example."
ai_output = """
Normal distribution: bell-shaped curve, parameterized by mean and std.
Z-score: (x - mean) / std, measures how many std deviations x is from mean.
Hypothesis test: check if sample mean is significantly different from claimed population mean.

import numpy as np
from scipy import stats
data = np.random.normal(loc=50, scale=5, size=100)
z_stat, p_val = stats.ttest_1samp(data, popmean=50)
print(p_val)
"""
print("Prompt:", prompt)
print("AI Output:", ai_output)
print("Evaluation:")
print("Explanation is correct and concise.")
print("Code is logically correct and runnable.")
print("Improvement: implement Z-test manually instead of relying on scipy for better learning.")
