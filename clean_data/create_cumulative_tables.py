import pandas as pd

df = pd.read_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/ATL.CSV')

df2018 = df.copy()
df2019 = df.copy()

df2018 = df2018[df2018['Year'] == 2018]
df2019 = df2019[df2019['Year'] == 2019]

df2018.drop(['Year', 'Week', 'Home'], inplace=True, axis=1)
df2019.drop(['Year', 'Week', 'Home'], inplace=True, axis=1)

df2018 = df2018.cumsum()
df2019 = df2019.cumsum()

index2018 = list(df2018.index)
index2019 = list(df2019.index)

index2018list = [item + 1 for item in index2018]
index2019list = [item + 1 - len(index2018list) for item in index2019]

df2018.insert(value=index2018list, loc=0, column='Games Played')
df2019.insert(value=index2019list, loc=0, column='Games Played')

df2018[['avg.Cmp', 'avg.Att', 'avg.Yds', 'avg.1D', 'avg.IAY', 'avg.CAY', 'avg.YAC', 'avg.Drops', 'avg.BadTh',
        'avg.Sk', 'avg.Bltz', 'avg.Hrry', 'avg.Hits', 'avg.Scrm', 'avg.ScrambleYds', 'avg.Att.1', 'avg.Yds.1', 'avg.1D.1',
        'avg.YBC', 'avg.YAC.1', 'avg.BrkTkl', 'avg.Tgt', 'avg.Rec', 'avg.Yds.2', 'avg.1D.2', 'avg.YBC.1', 'avg.YAC.2',
        'avg.BrkTkl.1', 'avg.Drop', 'avg.Int', 'avg.Tgt.1', 'avg.Cmp.1', 'avg.Yds.3', 'avg.TD', 'avg.Rat', 'avg.Air', 'avg.YAC.3',
        'avg.Bltz.1', 'avg.Hrry.1', 'avg.QBKD', 'avg.Sk.1', 'avg.Prss', 'avg.Comb', 'avg.MTkl', 'avg.total.DADOT']] = \
    df2018.apply(lambda row: (row[['Cmp', 'Att', 'Yds', '1D', 'IAY', 'CAY', 'YAC', 'Drops', 'BadTh',
        'Sk', 'Bltz', 'Hrry', 'Hits', 'Scrm', 'ScrambleYds', 'Att.1', 'Yds.1', '1D.1',
        'YBC', 'YAC.1', 'BrkTkl', 'Tgt', 'Rec', 'Yds.2', '1D.2', 'YBC.1', 'YAC.2',
        'BrkTkl.1', 'Drop', 'Int', 'Tgt.1', 'Cmp.1', 'Yds.3', 'TD', 'Rat', 'Air', 'YAC.3',
        'Bltz.1', 'Hrry.1', 'QBKD', 'Sk.1', 'Prss', 'Comb', 'MTkl', 'total.DADOT']] / row['Games Played']), axis=1)

df2019[['avg.Cmp', 'avg.Att', 'avg.Yds', 'avg.1D', 'avg.IAY', 'avg.CAY', 'avg.YAC', 'avg.Drops', 'avg.BadTh',
        'avg.Sk', 'avg.Bltz', 'avg.Hrry', 'avg.Hits', 'avg.Scrm', 'avg.ScrambleYds', 'avg.Att.1', 'avg.Yds.1', 'avg.1D.1',
        'avg.YBC', 'avg.YAC.1', 'avg.BrkTkl', 'avg.Tgt', 'avg.Rec', 'avg.Yds.2', 'avg.1D.2', 'avg.YBC.1', 'avg.YAC.2',
        'avg.BrkTkl.1', 'avg.Drop', 'avg.Int', 'avg.Tgt.1', 'avg.Cmp.1', 'avg.Yds.3', 'avg.TD', 'avg.Rat', 'avg.Air', 'avg.YAC.3',
        'avg.Bltz.1', 'avg.Hrry.1', 'avg.QBKD', 'avg.Sk.1', 'avg.Prss', 'avg.Comb', 'avg.MTkl', 'avg.total.DADOT']] = \
    df2019.apply(lambda row: (row[['Cmp', 'Att', 'Yds', '1D', 'IAY', 'CAY', 'YAC', 'Drops', 'BadTh',
        'Sk', 'Bltz', 'Hrry', 'Hits', 'Scrm', 'ScrambleYds', 'Att.1', 'Yds.1', '1D.1',
        'YBC', 'YAC.1', 'BrkTkl', 'Tgt', 'Rec', 'Yds.2', '1D.2', 'YBC.1', 'YAC.2',
        'BrkTkl.1', 'Drop', 'Int', 'Tgt.1', 'Cmp.1', 'Yds.3', 'TD', 'Rat', 'Air', 'YAC.3',
        'Bltz.1', 'Hrry.1', 'QBKD', 'Sk.1', 'Prss', 'Comb', 'MTkl', 'total.DADOT']] / row['Games Played']), axis=1)


df2018.drop(['Cmp', 'Att', 'Yds', '1D', 'IAY', 'CAY', 'YAC', 'Drops', 'BadTh',
        'Sk', 'Bltz', 'Hrry', 'Hits', 'Scrm', 'ScrambleYds', 'Att.1', 'Yds.1', '1D.1',
        'YBC', 'YAC.1', 'BrkTkl', 'Tgt', 'Rec', 'Yds.2', '1D.2', 'YBC.1', 'YAC.2',
        'BrkTkl.1', 'Drop', 'Int', 'Tgt.1', 'Cmp.1', 'Yds.3', 'TD', 'Rat', 'Air', 'YAC.3',
        'Bltz.1', 'Hrry.1', 'QBKD', 'Sk.1', 'Prss', 'Comb', 'MTkl', 'total.DADOT'], inplace=True, axis=1)

df2019.drop(['Cmp', 'Att', 'Yds', '1D', 'IAY', 'CAY', 'YAC', 'Drops', 'BadTh',
        'Sk', 'Bltz', 'Hrry', 'Hits', 'Scrm', 'ScrambleYds', 'Att.1', 'Yds.1', '1D.1',
        'YBC', 'YAC.1', 'BrkTkl', 'Tgt', 'Rec', 'Yds.2', '1D.2', 'YBC.1', 'YAC.2',
        'BrkTkl.1', 'Drop', 'Int', 'Tgt.1', 'Cmp.1', 'Yds.3', 'TD', 'Rat', 'Air', 'YAC.3',
        'Bltz.1', 'Hrry.1', 'QBKD', 'Sk.1', 'Prss', 'Comb', 'MTkl', 'total.DADOT'], inplace=True, axis=1)

bob = pd.concat([df2018, df2019])