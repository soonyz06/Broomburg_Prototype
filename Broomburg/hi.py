import pandas as pd
import polars as pl
import matplotlib.pyplot as plt
import statsmodels.api as sm
from src.utils.history import get_history
import numpy as np
from pathlib import Path
from src.utils.time_series import plot_periodogram, stationarity_tests, plot_acf_pacf, plot_stl_decom, plot_bands

def get_time_plot(history, freq=30, mode="log", feature="close", alpha=0.05):
    if mode.lower()=="log":
        returns = f"log_returns"
        history = history.with_columns(pl.col(feature).log().alias(f"log_{feature}"))
        history = history.with_columns(pl.col(f"log_{feature}").diff().over("symbol").alias(returns))
        model_type = "additive"
        feature = f"log_{feature}"
    elif mode.lower()=="abs":
        returns = f"abs_returns"
        history = history.with_columns(pl.col(feature).abs().alias(f"abs_{feature}"))
        history = history.with_columns(pl.col(f"abs_{feature}").diff().over("symbol").alias(returns))
        model_type = "additive"
        feature = f"abs_{feature}"
    else:
        returns = f"returns"
        history = history.with_columns((pl.col(feature)/pl.col(feature).shift(1).over("symbol")-1).alias(returns))
        model_type = "multiplicative"

    df = history.to_pandas()
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.month
    df["date_num"] = df["date"].astype("int64") // 10**9
    for sym in df["symbol"].unique():
        ts = df[df["symbol"] == sym].set_index("date")
        plot_regression(df, ["date_num"], returns)
        #params = {"col": returns}
        #plot_acf_pacf(ts[returns], freq=freq, alpha=alpha)
        #plot_bands(ts[returns], window=freq, alpha=alpha)
        #plot_stl_decom(ts[feature], period=freq)
        #plot_periodogram(ts[returns])
        #x = stationarity_tests(ts[feature])

symbols = ["SPY"]
history = get_history(symbols, period="3y")
get_time_plot(history, freq=30, mode="log")
