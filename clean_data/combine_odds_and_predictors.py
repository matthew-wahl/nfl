import pandas as pd

df = pd.read_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/predictors/stat_predictors.csv')
df1 = pd.read_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/odds/nfl_odds_historical_sorted_full.csv')

odds_values = df1.values.tolist()
# split into seasons
season_2018 = odds_values[0:int(len(odds_values)/2)]
season_2019 = odds_values[int(len(odds_values)/2):]

# remove first week
season_2018 = season_2018[0:-16]
season_2019 = season_2019[0:-16]

# reverse order
season_2018 = season_2018[::-1]
season_2019 = season_2019[::-1]

combined = []
for item in season_2019:
    combined.append(item)
for item in season_2018:
    combined.append(item)

df2 = pd.DataFrame(combined, columns=df1.columns.values)

# combine
df_merged = pd.merge(df, df2, how='left', on=['Year', 'Month', 'Day Number', 'Team 1'])
df_merged.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/predictors/stat_predictors_with_odds.csv', index=False)
