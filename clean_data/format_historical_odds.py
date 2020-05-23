import pandas as pd
import datetime


def abbreviate(x):
    team_list_abbreviation = pd.read_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_abbreviations_list.csv',
                                         header=None).values.tolist()
    team_list_full_names = pd.read_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_names_full.txt',
                                       header=None).values.tolist()
    for full_name in team_list_full_names:
        if full_name[0] == x:
            return team_list_abbreviation[team_list_full_names.index(full_name)][0]


df = pd.read_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/odds/nfl_odds_historical.csv')
df['Date'] = pd.to_datetime(df['Date'])
# all games after end of 2017-2018 season
df = df.loc[(df['Date'].dt.date > datetime.date(2018, 2, 4))]
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day Number'] = df['Date'].dt.day

df['Home Team'] = df['Home Team'].apply(abbreviate)
df['Away Team'] = df['Away Team'].apply(abbreviate)

df['Team 1'] = df['Home Team']
df['Team 2'] = df['Away Team']
df['Team 1 Odds Close'] = df['Home Odds Close']
df['Team 2 Odds Close'] = df['Away Odds Close']
df['Team 1 Line Close'] = df['Home Line Close']
df['Team 2 Line Close'] = df['Away Line Close']
df['Team 1 Line Odds Close'] = df['Home Line Odds Close']
df['Team 2 Line Odds Close'] = df['Away Line Odds Close']

df.drop(['Date',
         'Home Team',
         'Home Score',
         'Away Team',
         'Away Score',
         'Overtime?',
         'Playoff Game?',
         'Neutral Venue?',
         'Home Odds Open',
         'Home Odds Min',
         'Home Odds Max',
         'Home Odds Close',
         'Away Odds Open',
         'Away Odds Min',
         'Away Odds Max',
         'Away Odds Close',
         'Home Line Open',
         'Home Line Min',
         'Home Line Max',
         'Home Line Close',
         'Away Line Open',
         'Away Line Min',
         'Away Line Max',
         'Away Line Close',
         'Home Line Odds Open',
         'Home Line Odds Min',
         'Home Line Odds Max',
         'Home Line Odds Close',
         'Away Line Odds Open',
         'Away Line Odds Min',
         'Away Line Odds Max',
         'Away Line Odds Close',
         'Total Score Open',
         'Total Score Min',
         'Total Score Max',
         'Total Score Over Open',
         'Total Score Over Min',
         'Total Score Over Max',
         'Total Score Under Open',
         'Total Score Under Min',
         'Total Score Under Max',
         'Total Score Under Close',
         'Notes'], inplace=True, axis=1)

# sort alphabetical

# df['Total Score Close']
# df['Total Score Over Close']
# df['Year']
# df['Month']
# df['Day Number']

cols = df.columns.values
games_list = df.values.tolist()

for game in games_list:
    team1 = game[5]
    team2 = game[6]

    team1_odds_close = game[7]
    team2_odds_close = game[8]

    team1_line_close = game[9]
    team2_line_close = game[10]

    team1_line_odds_close = game[11]
    team2_line_odds_close = game[12]
    # check alphabetical
    if game[6] < game[5]:
        # switch
        game[5] = team2
        game[6] = team1

        game[7] = team2_odds_close
        game[8] = team1_odds_close

        game[9] = team2_line_close
        game[10] = team1_line_close

        game[11] = team2_line_odds_close
        game[12] = team1_line_odds_close

df1 = pd.DataFrame(games_list, columns=cols)
df1.drop(['Team 2 Line Close', 'Team 2 Line Odds Close'], inplace=True, axis=1)

df1.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/odds/nfl_odds_historical_sorted.csv', index=False)