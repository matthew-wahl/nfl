import pandas as pd

seasons = ['2018', '2019']
season_list = []
for season in seasons:
    file_path = 'C:/Users/matth/PycharmProjects/untitled1/nfl/schedule/schedule_' + season + '.log'
    df = pd.read_csv(file_path)
    team_list = pd.read_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_abbreviations_list.csv',
                            header=None).values.tolist()
    team_list_full = pd.read_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_names_full.txt',
                            header=None).values.tolist()

    string_list = str(df.values.tolist()[0][0])
    s = string_list.split('\n')
    for item in s:
        split_item = item.split('\t')
        # do not append headers separating weeks
        if split_item[0] == 'WildCard':
            split_item[0] = 18
        if split_item[0] == 'Division':
            split_item[0] = 19
        if split_item[0] == 'ConfChamp':
            split_item[0] = 20
        if split_item[0] == 'SuperBowl':
            split_item[0] = 21

        if split_item[2] not in ['Date', 'Playoffs']:
            split_item[0] = int(split_item[0])
            split_item[8] = int(split_item[8])
            split_item[9] = int(split_item[9])

            for team in team_list_full:
                if team[0] == split_item[4]:
                    split_item[4] = team_list[team_list_full.index(team)][0]

                if team[0] == split_item[6]:
                    split_item[6] = team_list[team_list_full.index(team)][0]

            # sort teams by alphabetical
            score1 = split_item[8]
            score2 = split_item[9]
            team1 = split_item[4]
            team2 = split_item[6]
            if split_item[4][0] < split_item[6][0]:
                split_item[8] = score1
                split_item[9] = score2
            else:
                split_item[4] = team2
                split_item[6] = team1
                split_item[8] = score2
                split_item[9] = score1

            season_list.append(split_item)

cols = ['Week', 'Day', 'Date', 'Time', 'Team 1', 'blank1', 'Team 2', 'blank2', 'Team 1 Score', 'Team 2 Score', 'YdsW', 'TOW',
        'YdsL', 'TOL']

df1 = pd.DataFrame(season_list, columns=cols)
df1.drop(['blank1', 'blank2', 'YdsW', 'TOW', 'YdsL', 'TOL'], inplace=True, axis=1)
df1['Total'] = df1.apply(lambda row: (row['Team 1 Score'] + row['Team 2 Score']), axis=1)
df1['Spread'] = df1.apply(lambda row: (row['Team 1 Score'] - row['Team 2 Score']), axis=1)

df1.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/schedule/schedule_results.csv')

