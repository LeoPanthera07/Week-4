import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

print("Part A - Task 1: Synthetic datasets")
n = 100
X_reg = np.linspace(0, 10, n)
y_reg = 3 * X_reg + 7 + np.random.normal(0, 3, n)

X_cls = np.random.randn(n)
y_cls = (X_cls > 0).astype(int)

print("Regression target sample:", y_reg[:5].round(2))
print("Classification target sample:", y_cls[:10])

print("\nTask 2: Visualize regression")
plt.figure(figsize=(8, 4))
plt.scatter(X_reg, y_reg, s=10, label="data")
m = np.polyfit(X_reg, y_reg, 1)
plt.plot(X_reg, np.polyval(m, X_reg), color="red", label="fit")
plt.title("Regression: X vs y")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.savefig("pm_regression.png", dpi=150, bbox_inches="tight")
plt.show()
print("Regression slope:", round(m[0], 2), "intercept:", round(m[1], 2))

print("\nTask 3: Problem type identification")
print("Continuous target (float) → Regression")
print("Discrete target (0/1/categories) → Classification")

print("\nTask 4: Manual linear regression + MSE")
def predict_linear(X, weight, bias):
    return weight * X + bias

def mse(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

w, b = 3.0, 7.0
y_pred_reg = predict_linear(X_reg, w, b)
print("MSE (manual model):", round(mse(y_reg, y_pred_reg), 4))

print("\nTask 5: Simple classification + accuracy")
threshold = 0.0
y_pred_cls = (X_cls >= threshold).astype(int)
accuracy = (y_pred_cls == y_cls).sum() / len(y_cls)
print("Accuracy:", round(accuracy, 4))

print("\nTask 6: Regression vs Classification comparison")
print("Regression  → continuous output, metric: MSE/RMSE/MAE")
print("Classification → discrete output, metric: accuracy/precision/recall")
print("Use regression for: price, temperature, demand forecasting")
print("Use classification for: spam/not-spam, disease yes/no, fraud detection")

print("\nPart B - Bias-Variance Tradeoff")
X_bv = np.linspace(-3, 3, 100)
y_bv = np.sin(X_bv) + np.random.normal(0, 0.3, 100)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
degrees = [1, 2, 5]
labels  = ["Degree 1 (underfit)", "Degree 2 (balanced)", "Degree 5 (overfit)"]

for i, (deg, label) in enumerate(zip(degrees, labels)):
    coeffs = np.polyfit(X_bv, y_bv, deg)
    y_fit  = np.polyval(coeffs, X_bv)
    train_mse = mse(y_bv, y_fit)
    axes[i].scatter(X_bv, y_bv, s=8)
    axes[i].plot(X_bv, y_fit, color="red")
    axes[i].set_title(f"{label}\nMSE={train_mse:.3f}")

plt.tight_layout()
plt.savefig("pm_bias_variance.png", dpi=150, bbox_inches="tight")
plt.show()

print("Bias: error from wrong assumptions (underfit — high bias)")
print("Variance: sensitivity to training data (overfit — high variance)")
print("Optimal model: low bias AND low variance (usually degree 2 here)")

def calculate_mse(y_true, y_pred):
    return ((np.array(y_true) - np.array(y_pred)) ** 2).mean()

print("\nPart C")
print("Q2 calculate_mse([1,2,3], [1.1,2.1,2.9]):", round(calculate_mse([1,2,3],[1.1,2.1,2.9]),4))

print("\nQ1")
print("Regression: continuous output (house price, salary).")
print("Classification: discrete output (spam/ham, cat/dog).")

print("\nQ3")
print("Bias: model too simple, misses patterns (underfitting).")
print("Variance: model too complex, memorises noise (overfitting).")
print("Goal: sweet spot where both are minimised.")

print("\nPart D")
prompt = "Explain regression vs classification and bias-variance tradeoff with Python examples and visualizations."
ai_output = """
Regression: predicts continuous values. Example: LinearRegression on housing data.
Classification: predicts categories. Example: LogisticRegression on spam data.
Bias-Variance: low-degree poly = high bias. High-degree poly = high variance.
Ideal model balances both.
Visualization: plot train/test MSE vs polynomial degree to find the sweet spot.
"""
print("Prompt:", prompt)
print("AI Output:", ai_output)
print("Evaluation:")
print("Explanations are correct.")
print("Bias-variance visualization approach is valid.")
print("Improvement: AI should show test error increasing after optimal degree to clearly show overfitting.")
