import pandas as pd

df = pd.read_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/schedule/schedule_results_formatted_datetime.csv')
schedule_cols = df.columns.values

schedule_list = df.values.tolist()
no_first_week = []

# remove first week where there is no pre-game data available
for game in schedule_list:
    if game[1] != 1:
        no_first_week.append(game)

p_list = []
# add team pre-game stats
for game in no_first_week:
    # team 1
    file_path1 = 'C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/' \
                 + game[6].upper() + '_cumsum.CSV'
    df1 = pd.read_csv(file_path1)
    # get game data of cumulative stats as of the end of previous week
    df1 = df1.loc[(df1['Year'] == game[0]) & (df1['Week'] == game[1] - 1)]
    stats = df1.values.tolist()
    if stats:
        for stat in stats[0]:
            game.append(stat)

    # team 2
    file_path2 = 'C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/' \
                 + game[7].upper() + '_cumsum.CSV'
    df2 = pd.read_csv(file_path2)
    # get game data of cumulative stats as of the end of previous week
    df2 = df2.loc[(df2['Year'] == game[0]) & (df2['Week'] == game[1] - 1)]
    stats = df2.values.tolist()
    if stats:
        for stat in stats[0]:
            game.append(stat)
    p_list.append(game)

p_cols = ['Year', 'Week', 'Month', 'Day of Week', 'Day Number', 'Hour', 'Team 1', 'Team 2',
          'Team 1 Score', 'Team 2 Score', 'Total', 'Spread', 'Team 1 Win',
          'Year.team1',
          'Week.team1',
          'Home.team1',
          'Games Played.team1',
          'avg.Cmp.team1',
          'avg.Att.team1',
          'avg.Yds.team1',
          'avg.1D.team1',
          'avg.IAY.team1',
          'avg.CAY.team1',
          'avg.YAC.team1',
          'avg.Drops.team1',
          'avg.BadTh.team1',
          'avg.Sk.team1',
          'avg.Bltz.team1',
          'avg.Hrry.team1',
          'avg.Hits.team1',
          'avg.Scrm.team1',
          'avg.ScrambleYds.team1',
          'avg.Att.1.team1',
          'avg.Yds.1.team1',
          'avg.1D.1.team1',
          'avg.YBC.team1',
          'avg.YAC.1.team1',
          'avg.BrkTkl.team1',
          'avg.Tgt.team1',
          'avg.Rec.team1',
          'avg.Yds.2.team1',
          'avg.1D.2.team1',
          'avg.YBC.1.team1',
          'avg.YAC.2.team1',
          'avg.BrkTkl.1.team1',
          'avg.Drop.team1',
          'avg.Int.team1',
          'avg.Tgt.1.team1',
          'avg.Cmp.1.team1',
          'avg.Yds.3.team1',
          'avg.TD.team1',
          'avg.Air.team1',
          'avg.YAC.3.team1',
          'avg.Bltz.1.team1',
          'avg.Hrry.1.team1',
          'avg.QBKD.team1',
          'avg.Sk.1.team1',
          'avg.Prss.team1',
          'avg.Comb.team1',
          'avg.MTkl.team1',
          'avg.total.DADOT.team1',
          'Year.team2',
          'Week.team2',
          'Home.team2',
          'Games Played.team2',
          'avg.Cmp.team2',
          'avg.Att.team2',
          'avg.Yds.team2',
          'avg.1D.team2',
          'avg.IAY.team2',
          'avg.CAY.team2',
          'avg.YAC.team2',
          'avg.Drops.team2',
          'avg.BadTh.team2',
          'avg.Sk.team2',
          'avg.Bltz.team2',
          'avg.Hrry.team2',
          'avg.Hits.team2',
          'avg.Scrm.team2',
          'avg.ScrambleYds.team2',
          'avg.Att.1.team2',
          'avg.Yds.1.team2',
          'avg.1D.1.team2',
          'avg.YBC.team2',
          'avg.YAC.1.team2',
          'avg.BrkTkl.team2',
          'avg.Tgt.team2',
          'avg.Rec.team2',
          'avg.Yds.2.team2',
          'avg.1D.2.team2',
          'avg.YBC.1.team2',
          'avg.YAC.2.team2',
          'avg.BrkTkl.1.team2',
          'avg.Drop.team2',
          'avg.Int.team2',
          'avg.Tgt.1.team2',
          'avg.Cmp.1.team2',
          'avg.Yds.3.team2',
          'avg.TD.team2',
          'avg.Air.team2',
          'avg.YAC.3.team2',
          'avg.Bltz.1.team2',
          'avg.Hrry.1.team2',
          'avg.QBKD.team2',
          'avg.Sk.1.team2',
          'avg.Prss.team2',
          'avg.Comb.team2',
          'avg.MTkl.team2',
          'avg.total.DADOT.team2']

df_p = pd.DataFrame(p_list, columns=p_cols)
df_p.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/predictors/stat_predictors.csv', index=False)
