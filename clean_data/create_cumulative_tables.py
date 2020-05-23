import pandas as pd

team_list = pd.read_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_abbreviations_list.csv',
                        header=None).values.tolist()
team_list = [team[0].upper() for team in team_list]
# empty list for each team
SDG = []
RAI = []
PHI = []
DAL = []
NYG = []
WAS = []
GNB = []
MIN = []
CHI = []
DET = []
SFO = []
NOR = []
ATL = []
CAR = []
SEA = []
RAM = []
TAM = []
CRD = []
NWE = []
BUF = []
NYJ = []
MIA = []
RAV = []
PIT = []
CLE = []
CIN = []
HTX = []
OTI = []
CLT = []
JAX = []
KAN = []
DEN = []

list_of_team_lists = [SDG, RAI, PHI, DAL, NYG, WAS, GNB, MIN, CHI, DET, SFO, NOR, ATL, CAR, SEA, RAM, TAM, CRD, NWE,
                      BUF, NYJ, MIA, RAV, PIT, CLE, CIN, HTX, OTI, CLT, JAX, KAN, DEN]
for team in team_list:
    file_path = 'C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/' + team + '.CSV'
    df = pd.read_csv(file_path)

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
            'avg.Sk', 'avg.Bltz', 'avg.Hrry', 'avg.Hits', 'avg.Scrm', 'avg.ScrambleYds', 'avg.Att.1', 'avg.Yds.1',
            'avg.1D.1',
            'avg.YBC', 'avg.YAC.1', 'avg.BrkTkl', 'avg.Tgt', 'avg.Rec', 'avg.Yds.2', 'avg.1D.2', 'avg.YBC.1',
            'avg.YAC.2',
            'avg.BrkTkl.1', 'avg.Drop', 'avg.Int', 'avg.Tgt.1', 'avg.Cmp.1', 'avg.Yds.3', 'avg.TD', 'avg.Air',
            'avg.YAC.3',
            'avg.Bltz.1', 'avg.Hrry.1', 'avg.QBKD', 'avg.Sk.1', 'avg.Prss', 'avg.Comb', 'avg.MTkl',
            'avg.total.DADOT']] = \
        df2018.apply(lambda row: (row[['Cmp', 'Att', 'Yds', '1D', 'IAY', 'CAY', 'YAC', 'Drops', 'BadTh',
                                       'Sk', 'Bltz', 'Hrry', 'Hits', 'Scrm', 'ScrambleYds', 'Att.1', 'Yds.1', '1D.1',
                                       'YBC', 'YAC.1', 'BrkTkl', 'Tgt', 'Rec', 'Yds.2', '1D.2', 'YBC.1', 'YAC.2',
                                       'BrkTkl.1', 'Drop', 'Int', 'Tgt.1', 'Cmp.1', 'Yds.3', 'TD', 'Air', 'YAC.3',
                                       'Bltz.1', 'Hrry.1', 'QBKD', 'Sk.1', 'Prss', 'Comb', 'MTkl', 'total.DADOT']] /
                                  row[
                                      'Games Played']), axis=1)

    df2019[['avg.Cmp', 'avg.Att', 'avg.Yds', 'avg.1D', 'avg.IAY', 'avg.CAY', 'avg.YAC', 'avg.Drops', 'avg.BadTh',
            'avg.Sk', 'avg.Bltz', 'avg.Hrry', 'avg.Hits', 'avg.Scrm', 'avg.ScrambleYds', 'avg.Att.1', 'avg.Yds.1',
            'avg.1D.1',
            'avg.YBC', 'avg.YAC.1', 'avg.BrkTkl', 'avg.Tgt', 'avg.Rec', 'avg.Yds.2', 'avg.1D.2', 'avg.YBC.1',
            'avg.YAC.2',
            'avg.BrkTkl.1', 'avg.Drop', 'avg.Int', 'avg.Tgt.1', 'avg.Cmp.1', 'avg.Yds.3', 'avg.TD', 'avg.Air',
            'avg.YAC.3',
            'avg.Bltz.1', 'avg.Hrry.1', 'avg.QBKD', 'avg.Sk.1', 'avg.Prss', 'avg.Comb', 'avg.MTkl',
            'avg.total.DADOT']] = \
        df2019.apply(lambda row: (row[['Cmp', 'Att', 'Yds', '1D', 'IAY', 'CAY', 'YAC', 'Drops', 'BadTh',
                                       'Sk', 'Bltz', 'Hrry', 'Hits', 'Scrm', 'ScrambleYds', 'Att.1', 'Yds.1', '1D.1',
                                       'YBC', 'YAC.1', 'BrkTkl', 'Tgt', 'Rec', 'Yds.2', '1D.2', 'YBC.1', 'YAC.2',
                                       'BrkTkl.1', 'Drop', 'Int', 'Tgt.1', 'Cmp.1', 'Yds.3', 'TD', 'Air', 'YAC.3',
                                       'Bltz.1', 'Hrry.1', 'QBKD', 'Sk.1', 'Prss', 'Comb', 'MTkl', 'total.DADOT']] /
                                  row[
                                      'Games Played']), axis=1)

    df2018.drop(['Cmp', 'Att', 'Yds', '1D', 'IAY', 'CAY', 'YAC', 'Drops', 'BadTh',
                 'Sk', 'Bltz', 'Hrry', 'Hits', 'Scrm', 'ScrambleYds', 'Att.1', 'Yds.1', '1D.1',
                 'YBC', 'YAC.1', 'BrkTkl', 'Tgt', 'Rec', 'Yds.2', '1D.2', 'YBC.1', 'YAC.2',
                 'BrkTkl.1', 'Drop', 'Int', 'Tgt.1', 'Cmp.1', 'Yds.3', 'TD', 'Air', 'YAC.3',
                 'Bltz.1', 'Hrry.1', 'QBKD', 'Sk.1', 'Prss', 'Comb', 'MTkl', 'total.DADOT'], inplace=True, axis=1)

    df2019.drop(['Cmp', 'Att', 'Yds', '1D', 'IAY', 'CAY', 'YAC', 'Drops', 'BadTh',
                 'Sk', 'Bltz', 'Hrry', 'Hits', 'Scrm', 'ScrambleYds', 'Att.1', 'Yds.1', '1D.1',
                 'YBC', 'YAC.1', 'BrkTkl', 'Tgt', 'Rec', 'Yds.2', '1D.2', 'YBC.1', 'YAC.2',
                 'BrkTkl.1', 'Drop', 'Int', 'Tgt.1', 'Cmp.1', 'Yds.3', 'TD', 'Air', 'YAC.3',
                 'Bltz.1', 'Hrry.1', 'QBKD', 'Sk.1', 'Prss', 'Comb', 'MTkl', 'total.DADOT'], inplace=True, axis=1)

    df2018 = pd.concat([df[['Year', 'Week', 'Home']], df2018], axis=1, join='inner')
    df2019 = pd.concat([df[['Year', 'Week', 'Home']], df2019], axis=1, join='inner')

    # locate bye weeks, and weeks missing up to super bowl and fill with value from previous week

    df2018_values = df2018.values.tolist()
    df2019_values = df2019.values.tolist()
    df_list = [df2018_values, df2019_values]

    # repeat previous week for BYEs, and PLAYOFFS if tem is eliminated
    for frame_list in df_list:
        all_weeks = list(range(1, 22))
        played_Weeks = [item[1] for item in frame_list]
        weeks_missing = [week for week in all_weeks if week not in played_Weeks]

        # columns are the same for both
        cols = df2018.columns.values

        for missing_week in weeks_missing:
            position_to_insert = int(missing_week - 1)
            position_to_repeat = int(missing_week - 2)
            element = frame_list[position_to_repeat].copy()
            element[1] = missing_week
            frame_list.insert(position_to_insert, element)

    # update year for turn of calendar
    for week in df2018_values:
        if week[1] > 17:
            week[0] += 1

    for week in df2019_values:
        if week[1] > 17:
            week[0] += 1

    # concat dataframes for each season ands then convert them to a list and update team_list in list_of_team_lists
    p_cols = df2018.columns.values
    newdf_2018 = pd.DataFrame(df2018_values, columns=p_cols)
    newdf_2019 = pd.DataFrame(df2019_values, columns=p_cols)
    df_cumsum = pd.concat([newdf_2018, newdf_2019], axis=0)
    combined_list = df_cumsum.values.tolist()
    list_of_team_lists[team_list.index(team)].append(combined_list)

SDG_dfcumsum = pd.DataFrame(SDG[0], columns=p_cols)
RAI_dfcumsum = pd.DataFrame(RAI[0], columns=p_cols)
PHI_dfcumsum = pd.DataFrame(PHI[0], columns=p_cols)
DAL_dfcumsum = pd.DataFrame(DAL[0], columns=p_cols)
NYG_dfcumsum = pd.DataFrame(NYG[0], columns=p_cols)
WAS_dfcumsum = pd.DataFrame(WAS[0], columns=p_cols)
GNB_dfcumsum = pd.DataFrame(GNB[0], columns=p_cols)
MIN_dfcumsum = pd.DataFrame(MIN[0], columns=p_cols)
CHI_dfcumsum = pd.DataFrame(CHI[0], columns=p_cols)
DET_dfcumsum = pd.DataFrame(DET[0], columns=p_cols)
SFO_dfcumsum = pd.DataFrame(SFO[0], columns=p_cols)
NOR_dfcumsum = pd.DataFrame(NOR[0], columns=p_cols)
ATL_dfcumsum = pd.DataFrame(ATL[0], columns=p_cols)
CAR_dfcumsum = pd.DataFrame(CAR[0], columns=p_cols)
SEA_dfcumsum = pd.DataFrame(SEA[0], columns=p_cols)
RAM_dfcumsum = pd.DataFrame(RAM[0], columns=p_cols)
TAM_dfcumsum = pd.DataFrame(TAM[0], columns=p_cols)
CRD_dfcumsum = pd.DataFrame(CRD[0], columns=p_cols)
NWE_dfcumsum = pd.DataFrame(NWE[0], columns=p_cols)
BUF_dfcumsum = pd.DataFrame(BUF[0], columns=p_cols)
NYJ_dfcumsum = pd.DataFrame(NYJ[0], columns=p_cols)
MIA_dfcumsum = pd.DataFrame(MIA[0], columns=p_cols)
RAV_dfcumsum = pd.DataFrame(RAV[0], columns=p_cols)
PIT_dfcumsum = pd.DataFrame(PIT[0], columns=p_cols)
CLE_dfcumsum = pd.DataFrame(CLE[0], columns=p_cols)
CIN_dfcumsum = pd.DataFrame(CIN[0], columns=p_cols)
HTX_dfcumsum = pd.DataFrame(HTX[0], columns=p_cols)
OTI_dfcumsum = pd.DataFrame(OTI[0], columns=p_cols)
CLT_dfcumsum = pd.DataFrame(CLT[0], columns=p_cols)
JAX_dfcumsum = pd.DataFrame(JAX[0], columns=p_cols)
KAN_dfcumsum = pd.DataFrame(KAN[0], columns=p_cols)
DEN_dfcumsum = pd.DataFrame(DEN[0], columns=p_cols)

SDG_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/SDG_cumsum.CSV', index=False)
RAI_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/RAI_cumsum.CSV', index=False)
PHI_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/PHI_cumsum.CSV', index=False)
DAL_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/DAL_cumsum.CSV', index=False)
NYG_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/NYG_cumsum.CSV', index=False)
WAS_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/WAS_cumsum.CSV', index=False)
GNB_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/GNB_cumsum.CSV', index=False)
MIN_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/MIN_cumsum.CSV', index=False)
CHI_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/CHI_cumsum.CSV', index=False)
DET_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/DET_cumsum.CSV', index=False)
SFO_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/SFO_cumsum.CSV', index=False)
NOR_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/NOR_cumsum.CSV', index=False)
ATL_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/ATL_cumsum.CSV', index=False)
CAR_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/CAR_cumsum.CSV', index=False)
SEA_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/SEA_cumsum.CSV', index=False)
RAM_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/RAM_cumsum.CSV', index=False)
TAM_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/TAM_cumsum.CSV', index=False)
CRD_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/CRD_cumsum.CSV', index=False)
NWE_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/NWE_cumsum.CSV', index=False)
BUF_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/BUF_cumsum.CSV', index=False)
NYJ_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/NYJ_cumsum.CSV', index=False)
MIA_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/MIA_cumsum.CSV', index=False)
RAV_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/RAV_cumsum.CSV', index=False)
PIT_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/PIT_cumsum.CSV', index=False)
CLE_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/CLE_cumsum.CSV', index=False)
CIN_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/CIN_cumsum.CSV', index=False)
HTX_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/HTX_cumsum.CSV', index=False)
OTI_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/OTI_cumsum.CSV', index=False)
CLT_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/CLT_cumsum.CSV', index=False)
JAX_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/JAX_cumsum.CSV', index=False)
KAN_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/KAN_cumsum.CSV', index=False)
DEN_dfcumsum.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/season_cumsum_box_scores/DEN_cumsum.CSV', index=False)
