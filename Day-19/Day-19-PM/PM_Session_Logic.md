# Day 19 PM – Logic & Explanations

## Part A

### Task 1: Synthetic Normal Dataset
- `np.random.normal(loc=50, scale=10, size=1000)` generates 1000 samples from N(50, 10²).
- Histogram should show bell curve — mean ≈ median ≈ mode for symmetric distributions.

### Task 2: Binomial PMF
- PMF formula: P(X=k) = C(n,k) · pᵏ · (1-p)^(n-k)
- Sum of all k from 0 to n = 1 (verified).
- Bernoulli is Binomial(n=1, p).

### Task 3: Normal PDF (manual)
- Formula: f(x) = (1 / σ√2π) · exp(−0.5·((x−μ)/σ)²)
- Implemented without any scipy/stats — only numpy math.
- Peak at x=μ, width determined by σ.

### Task 4: Descriptive Stats
- **Skewness**: positive → right tail longer; negative → left tail longer.
- For normal distribution, skewness ≈ 0.

### Task 5: Coin Toss Simulation
- Law of Large Numbers: empirical P(H) → 0.5 as n → ∞.
- At n=1000 the difference should be < 0.03.

---

## Part B: Distribution Comparison

| Property | Normal | Uniform |
|----------|--------|---------|
| Shape | Bell curve | Flat |
| Spread | Controlled by σ | Set by [low, high] |
| Mean | μ parameter | (low+high)/2 |
| Use | Measurements, errors | Random sampling, simulations |

**When to use**:
- Normal: modeling real-world measurements (height, test scores, sensor errors).
- Uniform: equal probability scenarios (random feature init, random splits, roll of a die).

---

## Part C

**Q1: PMF vs PDF**
- PMF: discrete random variable. P(X=k) is exact probability. Values sum to 1.
- PDF: continuous random variable. P(a≤X≤b) = ∫f(x)dx. Point probability = 0.

**Q2: empirical_probability()**
- Counts events satisfying `event_fn`, divides by total.
- Uses relative frequency approach: P(event) ≈ occurrences / n.

**Q3: Central Limit Theorem**
- Sample means from ANY distribution → Normal as n→∞.
- ML importance: validates parametric tests on non-normal data; explains stable gradient averages in mini-batch training.

---

## Part D
AI output correct on all three distributions.
Improvement: overlay theoretical curve on histogram for visual verification.
