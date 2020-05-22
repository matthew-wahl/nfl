import pandas as pd

df0 = pd.read_csv('/nfl/team_abbreviations_list.csv', header=None)
team_list = df0.values.tolist()

year = '19'
for team in team_list:
    file_location = 'C:/Users/matth/Desktop/teams_full_season_advanced_stats/' + team[0] + year + '.log'

    clean_rush = pd.DataFrame()
    clean_receiving = pd.DataFrame()
    clean_defense = pd.DataFrame()
    clean_df = [clean_rush, clean_receiving, clean_defense]

    df = pd.read_csv(file_location, header=None)
    # remove JS command
    df.drop([0, 2, 4], inplace=True)

    mess_rushing = df.iloc[0]
    mess_defense = df.iloc[0]
    mess_receiving = df.iloc[0]

    mess_df_list = [mess_rushing, mess_defense, mess_receiving]

    i = 0
    for item in mess_df_list:

        messy_str = item.values.tolist()[0]
        val_list = messy_str.split('\n')
        clean = []

        for val in val_list:
            clean.append(val.split('\t'))
        clean_df[i] = pd.DataFrame(clean[1:], columns=clean[0])
        print(clean_df[i])
        i += 1

