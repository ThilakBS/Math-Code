import pandas as pd


df = pd.read_csv("CompanyFinanceIndex.csv")

print("Type-", type(df))
df['quarterly_net_income_in_Millions'] = (df['quarterly_net_income'] / 1000000)
df
