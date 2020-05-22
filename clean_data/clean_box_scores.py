import numpy as np
import pandas as pd
import os


def get_list_of_files(dir_name):
    # create a list of file and sub directories
    # names in the given directory
    list_of_file = os.listdir(dir_name)
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_file:
        # Create full path
        fullPath = os.path.join(dir_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            all_files = all_files + get_list_of_files(fullPath)
        else:
            all_files.append(fullPath)

    return all_files


nfl = get_list_of_files('C:/Users/matth/PycharmProjects/untitled1/nfl/box_scores/')
team_list = pd.read_csv('C:/Users/matth/PycharmProjects/untitled1/team_abbreviations_list.csv',
                        header=None).values.tolist()

p_cols = ['Year', 'Week', 'Home', 'Cmp', 'Att', 'Yds', '1D', 'IAY', 'CAY', 'YAC', 'Drops', 'BadTh', 'Sk', 'Bltz',
          'Hrry',
          'Hits',
          'Scrm', 'ScrambleYds', 'Att', 'Yds', '1D', 'YBC', 'YAC', 'BrkTkl', 'Tgt', 'Rec', 'Yds', '1D', 'YBC', 'YAC',
          'BrkTkl', 'Drop', 'Int', 'Tgt', 'Cmp', 'Yds', 'TD', 'Rat', 'Air', 'YAC', 'Bltz', 'Hrry',
          'QBKD', 'Sk', 'Prss', 'Comb', 'MTkl', 'total.DADOT']

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

bob = []
count = 0
for file in nfl:
    file_string = file.split('/')[7].split('\\')
    # ['2019', 'week9', 'rai_det.log']
    year = file_string[0]
    week = file_string[1]
    week_num = int(file_string[1][4:])
    # week 18: WC,
    # week 19: DivRound
    # week 20: ConfChamp
    # week 21: SB
    game = file_string[2].split('.')[0]

    path = 'C:/Users/matth/PycharmProjects/untitled1/nfl/box_scores/' + year + '/' + week + '/' + game + '.log'

    # rav_nwe = Baltimore Ravens @ New England Patriots
    home_team = game.split('_')[0]
    away_team = game.split('_')[1]

    for team in team_list:
        # team in team_list is formatted as ['sdg']
        if away_team == team[0]:
            away_index = team_list.index(team)
        if home_team == team[0]:
            home_index = team_list.index(team)

    df = pd.read_csv(path)
    df.drop([0, 1, 2, 4, 6, 8], inplace=True)

    j = 0
    clean_df = []
    for num in range(len(df)):
        mess_df = df.iloc[num]
        messy_str = mess_df.values[0]
        val_list = messy_str.split('\n')

        clean_away = []
        clean_home = []
        clean_array = [clean_away, clean_home]
        i = 0
        for item in val_list:
            # check for table header dividing teams
            # home team listed after division
            if 'Player' in item:
                i += 1
                cols = item.split('\t')
            # away team listed before division
            else:
                clean_array[i].append(item.split('\t'))

        clean_df.append(pd.DataFrame(clean_array[0], columns=cols))
        clean_df.append(pd.DataFrame(clean_array[1], columns=cols))

    for k in range(0, 2):
        # passing
        passing = clean_df[0 + k]
        passing.drop(['Player', 'Tm', '1D%', 'IAY/PA', 'CAY/Cmp', 'CAY/PA', 'YAC/Cmp', 'Drop%', 'Bad%'], inplace=True,
                     axis=1)
        passing = passing.apply(pd.to_numeric)
        passing['ScrambleYds'] = passing.apply(lambda row: (row['Scrm'] * row['Yds/Scr']
                                                            if row['Scrm'] and row['Yds/Scr']
                                                            else None), axis=1)
        passing.drop(['Yds/Scr'], inplace=True, axis=1)
        cols = list(passing.columns.values)

        if k == 0:
            home = 0
        else:
            home = 1

        totals = [year, week_num, home]
        for col in cols:
            totals.append(passing[col].sum())

        cols.insert(0, 'Year')
        cols.insert(1, 'Week')
        cols.insert(2, 'Home')
        df_passing = pd.DataFrame([totals], columns=cols)

        # rushing
        rushing = clean_df[2 + k]
        rushing.drop(['Player', 'Tm', 'Att/Br', 'YBC/Att', 'YAC/Att'], inplace=True, axis=1)
        rushing = rushing.apply(pd.to_numeric)
        cols = list(rushing.columns.values)
        totals = []
        for col in cols:
            totals.append(rushing[col].sum())
        df_rushing = pd.DataFrame([totals], columns=cols)

        # receiving
        receiving = clean_df[4 + k]
        receiving.drop(['Player', 'Tm', 'YBC/R', 'YAC/R', 'Rec/Br', 'Drop%'], inplace=True, axis=1)
        receiving = receiving.apply(pd.to_numeric)
        cols = list(receiving.columns.values)
        totals = []
        for col in cols:
            totals.append(receiving[col].sum())
        df_receiving = pd.DataFrame([totals], columns=cols)

        # defense
        defense = clean_df[6 + k]
        defense.drop(['Player', 'Tm', 'MTkl%', 'Cmp%', 'Yds/Cmp', 'Yds/Tgt'], inplace=True, axis=1)
        defense = defense.apply(pd.to_numeric)
        defense['total.DADOT'] = defense.apply(lambda row: (row['Tgt'] * row['DADOT']
                                                            if row['Tgt'] and row['DADOT']
                                                            else None), axis=1)
        defense.drop(['DADOT'], inplace=True, axis=1)
        cols = list(defense.columns.values)
        totals = []
        for col in cols:
            totals.append(defense[col].sum())
        df_defense = pd.DataFrame([totals], columns=cols)

        hhh = pd.concat([df_passing, df_rushing, df_receiving, df_defense], axis=1)
        b = hhh.values.tolist()[0]

        if k == 0:
            # print(away_team, away_index, b)
            list_of_team_lists[away_index].append(b)

        elif k == 1:
            # print(home_team, home_index, b)
            # print(team_list[home_index], home_team)
            list_of_team_lists[home_index].append(b)
        else:
            print('ERROR: k != 0 and k != 1')
            break

# write team box score lists to CSVs
sdg_df = pd.DataFrame(SDG, columns=p_cols).sort_values(by=['Year', 'Week'])
sdg_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/SDG.CSV', index=False)
rai_df = pd.DataFrame(RAI, columns=p_cols).sort_values(by=['Year', 'Week'])
rai_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/RAI.CSV', index=False)
phi_df = pd.DataFrame(PHI, columns=p_cols).sort_values(by=['Year', 'Week'])
phi_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/PHI.CSV', index=False)
dal_df = pd.DataFrame(DAL, columns=p_cols).sort_values(by=['Year', 'Week'])
dal_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/DAL.CSV', index=False)
nyg_df = pd.DataFrame(NYG, columns=p_cols).sort_values(by=['Year', 'Week'])
nyg_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/NYG.CSV', index=False)
was_df = pd.DataFrame(WAS, columns=p_cols).sort_values(by=['Year', 'Week'])
was_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/WAS.CSV', index=False)
gnb_df = pd.DataFrame(GNB, columns=p_cols).sort_values(by=['Year', 'Week'])
gnb_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/GNB.CSV', index=False)
min_df = pd.DataFrame(MIN, columns=p_cols).sort_values(by=['Year', 'Week'])
min_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/MIN.CSV', index=False)
chi_df = pd.DataFrame(CHI, columns=p_cols).sort_values(by=['Year', 'Week'])
chi_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/CHI.CSV', index=False)
det_df = pd.DataFrame(DET, columns=p_cols).sort_values(by=['Year', 'Week'])
det_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/DET.CSV', index=False)
sfo_df = pd.DataFrame(SFO, columns=p_cols).sort_values(by=['Year', 'Week'])
sfo_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/SFO.CSV', index=False)
nor_df = pd.DataFrame(NOR, columns=p_cols).sort_values(by=['Year', 'Week'])
nor_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/NOR.CSV', index=False)
atl_df = pd.DataFrame(ATL, columns=p_cols).sort_values(by=['Year', 'Week'])
atl_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/ATL.CSV', index=False)
car_df = pd.DataFrame(CAR, columns=p_cols).sort_values(by=['Year', 'Week'])
car_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/CAR.CSV', index=False)
sea_df = pd.DataFrame(SEA, columns=p_cols).sort_values(by=['Year', 'Week'])
sea_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/SEA.CSV', index=False)
ram_df = pd.DataFrame(RAM, columns=p_cols).sort_values(by=['Year', 'Week'])
ram_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/RAM.CSV', index=False)
tam_df = pd.DataFrame(TAM, columns=p_cols).sort_values(by=['Year', 'Week'])
tam_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/TAM.CSV', index=False)
crd_df = pd.DataFrame(CRD, columns=p_cols).sort_values(by=['Year', 'Week'])
crd_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/CRD.CSV', index=False)
nwe_df = pd.DataFrame(NWE, columns=p_cols).sort_values(by=['Year', 'Week'])
nwe_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/NWE.CSV', index=False)
buf_df = pd.DataFrame(BUF, columns=p_cols).sort_values(by=['Year', 'Week'])
buf_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/BUF.CSV', index=False)
nyj_df = pd.DataFrame(NYJ, columns=p_cols).sort_values(by=['Year', 'Week'])
nyj_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/NYJ.CSV', index=False)
mia_df = pd.DataFrame(MIA, columns=p_cols).sort_values(by=['Year', 'Week'])
mia_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/MIA.CSV', index=False)
rav_df = pd.DataFrame(RAV, columns=p_cols).sort_values(by=['Year', 'Week'])
rav_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/RAV.CSV', index=False)
pit_df = pd.DataFrame(PIT, columns=p_cols).sort_values(by=['Year', 'Week'])
pit_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/PIT.CSV', index=False)
cle_df = pd.DataFrame(CLE, columns=p_cols).sort_values(by=['Year', 'Week'])
cle_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/CLE.CSV', index=False)
cin_df = pd.DataFrame(CIN, columns=p_cols).sort_values(by=['Year', 'Week'])
cin_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/CIN.CSV', index=False)
htx_df = pd.DataFrame(HTX, columns=p_cols).sort_values(by=['Year', 'Week'])
htx_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/HTX.CSV', index=False)
oti_df = pd.DataFrame(OTI, columns=p_cols).sort_values(by=['Year', 'Week'])
oti_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/OTI.CSV', index=False)
clt_df = pd.DataFrame(CLT, columns=p_cols).sort_values(by=['Year', 'Week'])
clt_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/CLT.CSV', index=False)
jax_df = pd.DataFrame(JAX, columns=p_cols).sort_values(by=['Year', 'Week'])
jax_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/JAX.CSV', index=False)
kan_df = pd.DataFrame(KAN, columns=p_cols).sort_values(by=['Year', 'Week'])
kan_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/KAN.CSV', index=False)
den_df = pd.DataFrame(DEN, columns=p_cols).sort_values(by=['Year', 'Week'])
den_df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/team_box_scores_sorted/DEN.CSV', index=False)
