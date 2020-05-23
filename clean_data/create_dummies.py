import pandas as pd

df = pd.read_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/predictors/stat_predictors_with_odds.csv')

df.drop(['Year', 'Month', 'Day Number', 'Team 1', 'Team 2_x', 'Year.team1', 'Week.team1',
         'Year.team2', 'Week.team2', 'Team 2_y'], inplace=True, axis=1)

week_dummies = pd.get_dummies(df['Week'], prefix='week', drop_first=True)
day_of_week_dummies = pd.get_dummies(df['Day of Week'], prefix='day_of_week', drop_first=True)
hour_dummies = pd.get_dummies(df['Hour'], prefix='hour', drop_first=True)
games_played_team1 = pd.get_dummies(df['Games Played.team1'], prefix='games_played_team_1', drop_first=True)
games_played_team2 = pd.get_dummies(df['Games Played.team2'], prefix='games_played_team_2', drop_first=True)

df.drop(['Week', 'Day of Week', 'Hour', 'Games Played.team1', 'Games Played.team2',
         'Total Score Close', 'Total Score Over Close', 'Team 1 Odds Close',
         'Team 2 Odds Close', 'Team 1 Line Close', 'Team 1 Line Odds Close', 'Home.team2', 'Team 1 Score',
         'Team 2 Score', 'Team 1 Win'
         ], inplace=True, axis=1)

df_predictors = pd.concat([df, week_dummies, day_of_week_dummies, hour_dummies, games_played_team1, games_played_team2],
                          axis=1)

new_col_order = ['Home.team1',
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
                 'avg.1D.2.team1', 'avg.YBC.1.team1', 'avg.YAC.2.team1', 'avg.BrkTkl.1.team1',
                 'avg.Drop.team1', 'avg.Int.team1', 'avg.Tgt.1.team1', 'avg.Cmp.1.team1',
                 'avg.Yds.3.team1', 'avg.TD.team1', 'avg.Air.team1', 'avg.YAC.3.team1',
                 'avg.Bltz.1.team1', 'avg.Hrry.1.team1', 'avg.QBKD.team1', 'avg.Sk.1.team1',
                 'avg.Prss.team1', 'avg.Comb.team1', 'avg.MTkl.team1',
                 'avg.total.DADOT.team1', 'avg.Cmp.team2', 'avg.Att.team2', 'avg.Yds.team2',
                 'avg.1D.team2', 'avg.IAY.team2', 'avg.CAY.team2', 'avg.YAC.team2',
                 'avg.Drops.team2', 'avg.BadTh.team2', 'avg.Sk.team2', 'avg.Bltz.team2',
                 'avg.Hrry.team2', 'avg.Hits.team2', 'avg.Scrm.team2',
                 'avg.ScrambleYds.team2', 'avg.Att.1.team2', 'avg.Yds.1.team2',
                 'avg.1D.1.team2', 'avg.YBC.team2', 'avg.YAC.1.team2', 'avg.BrkTkl.team2',
                 'avg.Tgt.team2', 'avg.Rec.team2', 'avg.Yds.2.team2', 'avg.1D.2.team2',
                 'avg.YBC.1.team2', 'avg.YAC.2.team2', 'avg.BrkTkl.1.team2', 'avg.Drop.team2',
                 'avg.Int.team2', 'avg.Tgt.1.team2', 'avg.Cmp.1.team2', 'avg.Yds.3.team2',
                 'avg.TD.team2', 'avg.Air.team2', 'avg.YAC.3.team2', 'avg.Bltz.1.team2',
                 'avg.Hrry.1.team2', 'avg.QBKD.team2', 'avg.Sk.1.team2', 'avg.Prss.team2',
                 'avg.Comb.team2', 'avg.MTkl.team2', 'avg.total.DADOT.team2', 'week_3',
                 'week_4' 'week_5', 'week_6', 'week_7', 'week_8', 'week_9', 'week_10', 'week_11',
                 'week_12' 'week_13', 'week_14', 'week_15', 'week_16', 'week_17', 'week_18',
                 'week_19' 'week_20', 'week_21', 'day_of_week_3', 'day_of_week_4',
                 'day_of_week_5', 'day_of_week_6', 'hour_12', 'hour_13', 'hour_15', 'hour_16',
                 'hour_18', 'hour_20', 'games_played_team_1_2.0', 'games_played_team_1_3.0',
                 'games_played_team_1_4.0', 'games_played_team_1_5.0',
                 'games_played_team_1_6.0', 'games_played_team_1_7.0',
                 'games_played_team_1_8.0', 'games_played_team_1_9.0',
                 'games_played_team_1_10.0', 'games_played_team_1_11.0',
                 'games_played_team_1_12.0', 'games_played_team_1_13.0',
                 'games_played_team_1_14.0', 'games_played_team_1_15.0',
                 'games_played_team_1_16.0', 'games_played_team_1_17.0',
                 'games_played_team_1_18.0', 'games_played_team_2_2.0',
                 'games_played_team_2_3.0', 'games_played_team_2_4.0',
                 'games_played_team_2_5.0', 'games_played_team_2_6.0',
                 'games_played_team_2_7.0', 'games_played_team_2_8.0',
                 'games_played_team_2_9.0', 'games_played_team_2_10.0',
                 'games_played_team_2_11.0', 'games_played_team_2_12.0',
                 'games_played_team_2_13.0', 'games_played_team_2_14.0',
                 'games_played_team_2_15.0', 'games_played_team_2_16.0',
                 'games_played_team_2_17.0', 'games_played_team_2_18.0',
                 'Total', 'Spread']
df_predictors = df_predictors.reindex(columns=new_col_order)
df_predictors.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/predictors/stat_predictors_with_dummies.csv')
