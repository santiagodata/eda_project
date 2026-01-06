# Data Dictionary

File: `data/customers_ecommerce_churn.csv`

| Column | Type | Description |
|---|---|---|
| customer_id | int | Unique customer identifier |
| signup_date | date | Signup date |
| region | category | Customer region |
| acquisition_channel | category | Acquisition source/channel |
| preferred_device | category | Preferred device for browsing |
| sessions_last_30d | int | Sessions in last 30 days |
| orders_last_90d | int | Orders in last 90 days |
| avg_order_value_usd | float | Average order value in USD |
| discount_rate | float | Typical discount usage (0-1) |
| support_tickets_last_90d | int | Support tickets in last 90 days |
| return_rate | float | Return rate (0-1) |
| nps_score | int | Net Promoter Score (-100 to 100), with some missing values |
| tenure_months | int | Customer tenure in months |
| gross_revenue_12m_usd | float | Estimated revenue last 12 months in USD (includes outliers) |
| last_purchase_date | date | Last purchase date (NaT for customers with 0 orders) |
| churned | int | 1 if churned, 0 otherwise |
