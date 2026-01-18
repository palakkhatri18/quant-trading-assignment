# Quantitative Trading Strategy Project (Beginner Level)

## Introduction

This project is my attempt to understand and build a basic quantitative trading system.
I am a beginner in quantitative finance and machine learning, and this project was created
to learn how data, indicators, models, and strategies work together in real trading systems.

The goal of this project is **not** to create a perfect or highly profitable trading system,
but to understand the **complete end-to-end pipeline** used in algorithmic trading.

---

## What is Quantitative Trading?

Quantitative trading means making trading decisions using:
- Historical market data
- Mathematical indicators
- Statistical models
- Machine learning (optional)

Instead of guessing or trading emotionally, rules are defined using data and logic.

---

## Project Objective

The main objectives of this project are:
1. Understand how market data is structured
2. Learn feature engineering (creating useful indicators)
3. Detect market conditions (called regimes)
4. Create a rule-based trading strategy
5. Test the strategy on historical data (backtesting)
6. Use machine learning to improve trade quality

---

## Data Used in This Project

### Why Dummy Data Was Used

Due to time, infrastructure, and API limitations, **controlled dummy data** was generated.
The dummy data follows realistic market behavior and **exactly matches the required columns**
mentioned in the assignment.

The focus of this project is **system design and logic**, not data sourcing.

---

## Types of Data Created

### 1. NIFTY Spot Data (5-Minute Interval)
This represents the actual index price.

Columns:
- `datetime` – time of the candle
- `open` – price at start of candle
- `high` – highest price
- `low` – lowest price
- `close` – price at end of candle
- `volume` – traded volume

---

### 2. NIFTY Futures Data
This represents futures contracts.

Additional columns:
- `open_interest` – number of open contracts
- `expiry` – contract expiry date

---

### 3. NIFTY Options Data
Options data is used to understand market sentiment and volatility.

Columns:
- `strike` – option strike price
- `option_type` – CE (Call) or PE (Put)
- `ltp` – last traded price
- `iv` – implied volatility
- `open_interest` – open positions
- `volume` – traded volume

---

## Feature Engineering (Creating Indicators)

Feature engineering means **creating useful columns** from raw data.

### Indicators Used

#### EMA (Exponential Moving Average)
- EMA(5): short-term trend
- EMA(15): medium-term trend

EMA gives more importance to recent prices.

---

#### Spot Returns
Shows how much the price changes between candles.

Used to measure profit and loss.

---

#### Futures Basis
Formula:
(futures price − spot price) / spot price


This shows market expectation and sentiment.

---

#### PCR (Put-Call Ratio)

PCR is calculated using:
- Open Interest
- Volume

Formula:


PCR = Put / Call


It helps understand whether traders are more bullish or bearish.

---

#### Average Implied Volatility (IV)

IV represents expected future volatility.
Higher IV usually means higher uncertainty or fear.

---

## Regime Detection (Market States)

### What is a Market Regime?

A market regime is the **overall condition of the market**, such as:
- Uptrend
- Downtrend
- Sideways

---

### Model Used: Hidden Markov Model (HMM)

HMM is a statistical model that:
- Assumes the market switches between hidden states
- Learns these states from data
- Does not require labels

---

### Regimes Defined

- `+1` → Uptrend
- `0` → Sideways
- `-1` → Downtrend

The model is trained on:
- Implied volatility
- Put-call ratios
- Futures basis
- Spot returns

---

### Regime Analysis Performed

- Price with regime overlay
- Regime transition matrix
- Regime-wise statistics
- Regime duration histogram

These help understand how markets move between states.

---

## Trading Strategy

### Strategy Used: EMA Crossover with Regime Filter

#### Entry Rules

**Long Trade**
- EMA(5) crosses above EMA(15)
- Market regime is bullish (+1)

**Short Trade**
- EMA(5) crosses below EMA(15)
- Market regime is bearish (-1)

**No trades** are taken in sideways regime (0).

---

### Why Regime Filter Is Important

Without regime filtering, EMA strategies generate many false signals.
Regime filtering reduces unnecessary trades and drawdowns.

---

## Backtesting

Backtesting means testing the strategy on past data.

Metrics calculated:
- Total return
- Equity curve
- Maximum drawdown
- Win rate
- Sharpe ratio (basic)

This helps understand how the strategy would have behaved historically.

---

## Machine Learning Enhancement

### Purpose of Machine Learning

Machine learning is used as a **trade quality filter**, not as a price predictor.

Goal:
- Predict whether a trade will be profitable or not

---

### Target Variable



1 → Profitable trade
0 → Loss trade


---

### Model Used

- XGBoost Classifier

Why XGBoost:
- Works well with tabular data
- Handles non-linear relationships
- Fast and widely used

---

### Training Method

- Time-series split (no shuffling)
- Prevents look-ahead bias

---

### Note on LSTM

LSTM model was planned but skipped due to:
- Time constraints
- Hardware limitations
- Environment issues

The ML pipeline structure is still implemented correctly.

---

## Project Structure



quant_trading_assignment/
│
├── data/
│ ├── raw/
│ ├── merged/
│
├── notebooks/
│ ├── 1_data_preparation.ipynb
│ ├── 2_regime_detection.ipynb
│ ├── 3_strategy_backtest.ipynb
│ ├── 4_ml_filter.ipynb
│
├── results/
│ └── baseline_strategy_results.csv
│
├── requirements.txt
├── README.md


---

## Limitations

- Dummy data used instead of live market APIs
- LSTM model not implemented
- Advanced trade outlier analysis not included
- Performance metrics kept basic

These were conscious decisions due to time constraints.

---

## Key Learnings

Through this project I learned:
- How raw market data is processed
- How features are created
- How regimes affect strategies
- Why backtesting is important
- How ML can assist rule-based systems

---

## Conclusion

This project helped me understand how a real quantitative trading system
is structured from start to finish. Although the system is simplified,
the logic and workflow closely resemble real-world trading pipelines.

This project serves as a strong foundation for further learning
and improvement in quantitative finance and algorithmic trading.