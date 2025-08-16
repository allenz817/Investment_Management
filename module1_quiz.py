"""
Question 1
Read in the data in the file “Portfolios_Formed_on_ME_monthly_EW.csv” as we did in the lab sessions.We performed a series of analysis on the ‘Lo 10’ and the ‘Hi 10’ columns which are the returns of the lowest and highest decile portfolios. For purposes of this assignment, we will use the lowest and highest quintile portfolios, which are labelled ‘Lo 20’ and ‘Hi 20’ respectively.
What was the Annualized Return of the Lo 20 portfolio over the entire period?

Enter the answer as a percentage. e.g. if your answer is 23.43% enter the number 23.43

Enter answer here
"""
"""
Question 1
Read in the data in the file "Portfolios_Formed_on_ME_monthly_EW.csv" as we did in the lab sessions.We performed a series of analysis on the 'Lo 10' and the 'Hi 10' columns which are the returns of the lowest and highest decile portfolios. For purposes of this assignment, we will use the lowest and highest quintile portfolios, which are labelled 'Lo 20' and 'Hi 20' respectively.
What was the Annualized Return of the Lo 20 portfolio over the entire period?

Enter the answer as a percentage. e.g. if your answer is 23.43% enter the number 23.43

Enter answer here
"""

import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv("data/Portfolios_Formed_on_ME_monthly_EW.csv", header=0, index_col=0)
lo_20_returns = df['Lo 20']
"""
lo_20_returns = pd.to_numeric(df['Lo 20'], errors='coerce')
lo_20_returns = lo_20_returns.dropna()
lo_20_returns = lo_20_returns / 100
"""

n_months = len(lo_20_returns)
n_years = n_months / 12

cumulative_return = (1 + lo_20_returns).prod()
annualized_return = (cumulative_return ** (1 / n_years) - 1) * 100

print(f"Annualized Return of Lo 20 portfolio: {annualized_return:.2f}%")

"""
Question 2
What was the Annualized Volatility of the Lo 20 portfolio over the entire period? 

Enter the answer as a numeric to one decimal place, as a percentage. e.g. if your answer is 23.43% enter the number 23.4

"""
monthly_volatility = lo_20_returns.std()
annualized_volatility = monthly_volatility * np.sqrt(12) * 100
print(f"Annualized Volatility of Lo 20 portfolio: {annualized_volatility:.1f}%")