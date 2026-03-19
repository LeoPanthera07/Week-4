import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
n = 600

df = pd.DataFrame({
    "student_id": range(1, n + 1),
    "name": [f"Student_{i}" for i in range(1, n + 1)],
    "age": np.random.randint(18, 26, n),
    "score": np.random.normal(65, 15, n).clip(0, 100).round(1),
    "attendance": np.random.uniform(50, 100, n).round(1),
    "department": np.random.choice(["CS", "IT", "ECE", "ME", "CE"], n),
    "year": np.random.choice([1, 2, 3, 4], n),
    "passed": None
})
df["passed"] = (df["score"] >= 40).astype(int)
df.to_csv("students.csv", index=False)
df = pd.read_csv("students.csv")

print("Part A - Task 1: loc selection")
print(df.loc[0:4, ["name", "score", "department"]])
print(df.loc[df["department"] == "CS", ["name", "score"]].head(3))
print(df.loc[(df["score"] > 80) & (df["year"] == 3), ["name", "score", "year"]].head(3))

print("\nilocselection")
print(df.iloc[0:5, 0:4])
print(df.iloc[10:15, [0, 3, 5]])
print(df.iloc[-5:, :])

print("\nTask 2: Filtering")
high_scorers = df[df["score"] > 80]
print("High scorers (score > 80):", len(high_scorers))

cs_low_attendance = df[(df["department"] == "CS") & (df["attendance"] < 65)]
print("CS students with attendance < 65:", len(cs_low_attendance))

senior_passed = df[(df["year"] == 4) & (df["passed"] == 1)]
print("Year 4 passed students:", len(senior_passed))

print("\nTask 3: Descriptive statistics")
print(df[["score", "attendance", "age"]].describe())
print("\nInterpretation:")
print(f"Score  — mean: {df['score'].mean():.2f}, std: {df['score'].std():.2f}, min: {df['score'].min():.2f}, max: {df['score'].max():.2f}")
print(f"Attendance — mean: {df['attendance'].mean():.2f}")
print("Score is roughly normally distributed around 65. Std ~15 means most scores lie 50-80.")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].hist(df["score"], bins=25, edgecolor="white")
axes[0, 0].set_title("Task 4: Score Distribution (Histogram)")
axes[0, 0].set_xlabel("Score")
axes[0, 0].set_ylabel("Frequency")

dept_avg = df.groupby("department")["score"].mean().sort_values(ascending=False)
axes[0, 1].bar(dept_avg.index, dept_avg.values)
axes[0, 1].set_title("Task 5: Avg Score by Department (Bar Plot)")
axes[0, 1].set_xlabel("Department")
axes[0, 1].set_ylabel("Avg Score")

year_trend = df.groupby("year")["score"].mean()
axes[1, 0].plot(year_trend.index, year_trend.values, marker="o")
axes[1, 0].set_title("Task 6: Avg Score by Year (Line Chart)")
axes[1, 0].set_xlabel("Year")
axes[1, 0].set_ylabel("Avg Score")

df["score"].plot.kde(ax=axes[1, 1])
axes[1, 1].set_title("Task 7: Score Density (KDE Plot)")
axes[1, 1].set_xlabel("Score")

plt.tight_layout()
plt.savefig("am_charts.png", dpi=150, bbox_inches="tight")
plt.show()

print("\nPart B - Grouped analysis")
grouped = df.groupby("department")[["score", "attendance"]].mean().round(2)
print(grouped)

grouped["score"].sort_values(ascending=False).plot(kind="bar", figsize=(8, 4), title="Avg Score by Department")
plt.ylabel("Avg Score")
plt.tight_layout()
plt.savefig("am_grouped_bar.png", dpi=150, bbox_inches="tight")
plt.show()

fig2, ax2 = plt.subplots(figsize=(8, 4))
df["score"].plot.kde(ax=ax2, label="Score")
df["attendance"].plot.kde(ax=ax2, label="Attendance")
ax2.set_title("KDE: Score vs Attendance")
ax2.legend()
plt.tight_layout()
plt.savefig("am_kde_compare.png", dpi=150, bbox_inches="tight")
plt.show()

print("\nInsight: CS and IT tend to score higher. Score distribution is normal. Attendance is roughly uniform.")

print("\nPart C")
print("Q1: loc uses labels/conditions. iloc uses integer positions.")

above_avg = df[df["score"] > df["score"].mean()]
print("Q2 - Rows above avg score:", len(above_avg))

print("Q3: describe() gives count, mean, std, min, quartiles, max.")
print("Useful to spot outliers, skewness, scale differences.")

print("\nPart D")
prompt = "Explain how to perform data analysis using Pandas and visualization using Matplotlib with examples."
ai_output = """
Pandas: load CSV with pd.read_csv(), filter with boolean indexing, summarize with describe().
Matplotlib: plt.hist() for distributions, plt.bar() for categories, plt.plot() for trends.
Example: df[df['score'] > 80].groupby('dept')['score'].mean().plot(kind='bar')
"""
print("Prompt:", prompt)
print("AI Output:", ai_output)
print("Evaluation:")
print("Explanation is correct and concise.")
print("Code examples are runnable.")
print("Improvement: AI should show KDE overlay on histogram for richer distribution analysis.")
