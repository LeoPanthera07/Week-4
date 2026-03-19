import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
n = 600

df = pd.DataFrame({
    "student_id": range(1, n + 1),
    "age": np.random.randint(18, 26, n),
    "score": np.random.normal(65, 15, n).clip(0, 100).round(1),
    "attendance": np.random.uniform(50, 100, n).round(1),
    "study_hours": np.random.normal(5, 2, n).clip(0, 12).round(1),
    "department": np.random.choice(["CS", "IT", "ECE", "ME", "CE"], n),
    "year": np.random.choice([1, 2, 3, 4], n),
})
df["passed"] = (df["score"] >= 40).astype(int)
df.to_csv("students.csv", index=False)
df = pd.read_csv("students.csv")

print("Part A - Task 1: Identify ML Problem Type")
print("Dataset: student performance data")
print("Supervised learning — labels (score, passed) are available")
print("score column → continuous → Regression problem")
print("passed column → binary (0/1) → Classification problem")

print("\nTask 2: Data handling")
print("Missing values:", df.isnull().sum().sum())
df = df.dropna()
relevant = df[["age", "attendance", "study_hours", "score", "passed"]]
print("Relevant features shape:", relevant.shape)
print(relevant.head())

print("\nTask 3: Regression — predict score from study_hours")
X = df["study_hours"].values
y = df["score"].values

x_mean = X.mean()
y_mean = y.mean()
weight = ((X - x_mean) * (y - y_mean)).sum() / ((X - x_mean) ** 2).sum()
bias   = y_mean - weight * x_mean

y_pred = weight * X + bias
mse    = ((y - y_pred) ** 2).mean()

print(f"Linear model: score = {weight:.4f} * study_hours + {bias:.4f}")
print(f"MSE: {mse:.4f}")

plt.figure(figsize=(8, 4))
plt.scatter(X, y, s=8, alpha=0.5, label="data")
plt.plot(X, y_pred, color="red", label="regression line")
plt.title("Regression: Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.legend()
plt.tight_layout()
plt.savefig("pm_regression.png", dpi=150, bbox_inches="tight")
plt.show()

print("\nTask 4: Classification — predict passed from score")
threshold = df["score"].mean()
y_cls_pred = (df["score"] >= threshold).astype(int)
y_cls_true = df["passed"].values
accuracy   = (y_cls_pred == y_cls_true).sum() / len(y_cls_true)
print(f"Threshold: {threshold:.2f}")
print(f"Accuracy: {accuracy:.4f}")

print("\nTask 5: Comparison")
print(f"{'':20} {'Regression':20} {'Classification':20}")
print(f"{'Output type':20} {'Continuous (score)':20} {'Discrete (0/1)':20}")
print(f"{'Use case':20} {'Score prediction':20} {'Pass/fail detection':20}")
print(f"{'Metric':20} {'MSE / RMSE':20} {'Accuracy / F1':20}")

print("\nPart B - Feature analysis")
corr = df[["age", "attendance", "study_hours", "score"]].corr()
print("Correlation matrix:")
print(corr.round(3))
print("\nstudyscore correlation:", round(corr.loc["study_hours", "score"], 3))

important = df[["attendance", "study_hours", "score"]].corr()["score"].drop("score").sort_values(ascending=False)
print("Feature correlation with score:", important.round(3))

df_clean = df.drop(columns=["student_id", "department"])
print("Removed irrelevant columns. Remaining:", df_clean.columns.tolist())

print("\nImpact: Features with higher correlation improve model accuracy.")
print("Removing noise columns reduces overfitting risk.")

print("\nPart C")
print("Q1: Supervised — labelled data (regression/classification)")
print("     Unsupervised — no labels (clustering, PCA)")
print("     Reinforcement — agent learns from rewards (game AI)")

high_score_subset = df[df["score"] > df["score"].mean()]
avg_study = high_score_subset["study_hours"].mean()
print(f"\nQ2 - Avg study hours for above-avg scorers: {avg_study:.2f}")

print("\nQ3: Regression → continuous output (price, temp).")
print("     Classification → discrete output (spam/ham, fraud/ok).")

print("\nPart D")
prompt = "Explain types of machine learning, regression, and classification with Python examples using Pandas."
ai_output = """
Supervised: labelled data. Regression predicts continuous, classification predicts category.
Unsupervised: no labels. Example: KMeans clustering.
Reinforcement: reward-based learning.

Regression example (Pandas):
  from sklearn.linear_model import LinearRegression
  model = LinearRegression().fit(X, y)

Classification:
  from sklearn.linear_model import LogisticRegression
  model = LogisticRegression().fit(X, y_cls)
"""
print("Prompt:", prompt)
print("AI Output:", ai_output)
print("Evaluation:")
print("ML type definitions are correct.")
print("Code is runnable with sklearn installed.")
print("Improvement: manually implement one model to show deeper understanding without library dependency.")
