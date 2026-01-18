import pandas as pd
import numpy as np

# -----------------------------
# CONFIG
# -----------------------------
START_PRICE = 20000
START_DATE = "2024-01-01"
END_DATE = "2024-12-31"
INTERVAL = "5min"
RISK_FREE_RATE = 0.065

np.random.seed(42)

# -----------------------------
# CREATE TIME INDEX (Market hours)
# -----------------------------
all_times = pd.date_range(START_DATE, END_DATE, freq=INTERVAL)
market_times = all_times[
    (all_times.time >= pd.to_datetime("09:15").time()) &
    (all_times.time <= pd.to_datetime("15:30").time())
]

n = len(market_times)

# -----------------------------
# SPOT DATA
# -----------------------------
spot_returns = np.random.normal(0, 0.0007, n)
spot_prices = START_PRICE * np.exp(np.cumsum(spot_returns))

spot = pd.DataFrame({
    "datetime": market_times,
    "open": spot_prices,
    "high": spot_prices * (1 + np.random.uniform(0, 0.001, n)),
    "low": spot_prices * (1 - np.random.uniform(0, 0.001, n)),
    "close": spot_prices,
    "volume": np.random.randint(80_000, 150_000, n)
})

spot.to_csv("data/raw/nifty_spot_5min.csv", index=False)

# -----------------------------
# FUTURES DATA
# -----------------------------
basis = np.random.normal(0.0005, 0.0003, n)
futures_price = spot_prices * (1 + basis)

futures = pd.DataFrame({
    "datetime": market_times,
    "open": futures_price,
    "high": futures_price * (1 + np.random.uniform(0, 0.001, n)),
    "low": futures_price * (1 - np.random.uniform(0, 0.001, n)),
    "close": futures_price,
    "volume": np.random.randint(60_000, 120_000, n),
    "open_interest": np.random.randint(900_000, 1_300_000, n),
    "expiry": "2024-12-26"
})

futures.to_csv("data/raw/nifty_futures_5min.csv", index=False)

# -----------------------------
# OPTIONS DATA (ATM ± 2)
# -----------------------------
option_rows = []

for i, price in enumerate(spot_prices):
    atm = round(price / 50) * 50
    iv = np.clip(np.random.normal(0.18, 0.03), 0.12, 0.30)

    for strike_offset in [-100, -50, 0, 50, 100]:
        strike = atm + strike_offset

        for opt_type in ["CE", "PE"]:
            ltp = max(5, abs(price - strike) * 0.4 + np.random.uniform(20, 80))

            option_rows.append([
                market_times[i],
                strike,
                opt_type,
                round(ltp, 2),
                round(iv, 3),
                np.random.randint(400_000, 1_200_000),
                np.random.randint(5_000, 25_000),
                "2024-12-26"
            ])

options = pd.DataFrame(option_rows, columns=[
    "datetime", "strike", "option_type",
    "ltp", "iv", "open_interest", "volume", "expiry"
])

options.to_csv("data/raw/nifty_options_5min.csv", index=False)

print("✅ Dummy data generated successfully!")
