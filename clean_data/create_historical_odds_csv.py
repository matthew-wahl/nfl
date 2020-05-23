import pandas as pd

df = pd.read_excel('C:/Users/matth/PycharmProjects/untitled1/nfl/odds/nfl_historical_odds.xlsx', sheet_name='Data')
df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/odds/nfl_odds_historical.csv', index=False)
