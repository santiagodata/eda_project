"""
EDA (Exploratory Data Analysis) - Example Project
Dataset: customers_ecommerce_churn.csv

Run:
    python -m src.eda

Outputs:
    - reports/eda_summary.json
    - reports/figures/*.png
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "customers_ecommerce_churn.csv"
REPORTS = ROOT / "reports"
FIGURES = REPORTS / "figures"


def savefig(name: str) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(FIGURES / f"{name}.png", dpi=160)
    plt.close()


def main() -> None:
    df = pd.read_csv(DATA_PATH)

    summary: dict[str, object] = {}
    summary["n_rows_raw"] = int(df.shape[0])
    summary["n_cols"] = int(df.shape[1])
    summary["dtypes"] = {c: str(t) for c, t in df.dtypes.items()}

    for c in ["signup_date", "last_purchase_date"]:
        df[c] = pd.to_datetime(df[c], errors="coerce")

    summary["missing_by_col"] = df.isna().sum().sort_values(ascending=False).to_dict()
    summary["duplicate_rows"] = int(df.duplicated().sum())

    df = df.drop_duplicates().reset_index(drop=True)
    summary["n_rows_after_dedup"] = int(df.shape[0])

    num_cols = [
        "sessions_last_30d",
        "orders_last_90d",
        "avg_order_value_usd",
        "discount_rate",
        "support_tickets_last_90d",
        "return_rate",
        "nps_score",
        "tenure_months",
        "gross_revenue_12m_usd",
    ]

    desc = df[num_cols].describe(percentiles=[0.01, 0.05, 0.5, 0.95, 0.99]).T
    summary["numeric_describe"] = desc.round(3).to_dict()

    # Univariate plots
    for c in ["sessions_last_30d", "orders_last_90d", "avg_order_value_usd", "gross_revenue_12m_usd", "nps_score"]:
        plt.figure()
        df[c].dropna().hist(bins=30)
        plt.title(f"Distribution: {c}")
        plt.xlabel(c)
        plt.ylabel("count")
        savefig(f"hist_{c}")

    # Categorical counts
    for c in ["region", "acquisition_channel", "preferred_device", "churned"]:
        plt.figure()
        df[c].value_counts(dropna=False).plot(kind="bar")
        plt.title(f"Counts: {c}")
        plt.xlabel(c)
        plt.ylabel("count")
        savefig(f"bar_{c}")

    # Churn rate by category
    for c in ["region", "acquisition_channel", "preferred_device"]:
        churn_rate = df.groupby(c, dropna=False)["churned"].mean().sort_values(ascending=False)
        plt.figure()
        churn_rate.plot(kind="bar")
        plt.title(f"Churn rate by {c}")
        plt.xlabel(c)
        plt.ylabel("mean(churned)")
        savefig(f"churn_rate_by_{c}")

    # Boxplots for numeric vs churn
    for c in ["sessions_last_30d", "orders_last_90d", "gross_revenue_12m_usd", "nps_score", "support_tickets_last_90d"]:
        plt.figure()
        df.boxplot(column=c, by="churned")
        plt.title(f"{c} by churned")
        plt.suptitle("")
        plt.xlabel("churned")
        plt.ylabel(c)
        savefig(f"box_{c}_by_churn")

    # Correlation
    corr = df[num_cols + ["churned"]].corr(numeric_only=True)
    summary["corr_with_churn"] = corr["churned"].sort_values(ascending=False).round(3).to_dict()

    plt.figure(figsize=(10, 7))
    plt.imshow(corr, aspect="auto")
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.index)), corr.index)
    plt.title("Correlation (numeric)")
    plt.colorbar()
    savefig("corr_matrix")

    # Outliers (IQR)
    outliers: dict[str, int] = {}
    for c in ["gross_revenue_12m_usd", "avg_order_value_usd", "orders_last_90d"]:
        s = df[c].dropna()
        q1, q3 = s.quantile([0.25, 0.75])
        iqr = q3 - q1
        low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        outliers[c] = int(((df[c] < low) | (df[c] > high)).sum())
    summary["outlier_counts_iqr"] = outliers

    REPORTS.mkdir(parents=True, exist_ok=True)
    with open(REPORTS / "eda_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print("✅ EDA complete.")
    print(f"- Figures: {FIGURES}")
    print(f"- Summary: {REPORTS / 'eda_summary.json'}")


if __name__ == "__main__":
    main()
