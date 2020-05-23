import pandas as pd

df = pd.read_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/schedule/schedule_results.csv')
df['Date String'] = df.apply(lambda row: (row['Day'] + ' ' + row['Date'] + ' ' + str(row['Year']) + ' ' + row['Time']),
                             axis=1)

df['Datetime'] = pd.to_datetime(df['Date String'])
df['Month'] = df['Datetime'].dt.month
df['Day of Week'] = df['Datetime'].dt.dayofweek
df['Day Number'] = df['Datetime'].dt.day
df['Hour'] = df['Datetime'].dt.hour

df.drop(['Date String', 'Datetime', 'Day', 'Date', 'Time'], inplace=True, axis=1)

re_ordered = ['Year', 'Week', 'Month', 'Day of Week', 'Day Number', 'Hour',
              'Team 1', 'Team 2', 'Team 1 Score', 'Team 2 Score', 'Total', 'Spread', 'Team 1 Win']

df = df.loc[:, re_ordered]
df.to_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/schedule/schedule_results_formatted_datetime.csv', index=False)
