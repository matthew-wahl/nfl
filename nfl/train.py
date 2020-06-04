import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.callbacks import EarlyStopping

import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:/Users/matth/PycharmProjects/untitled1/nfl/predictors/stat_predictors_with_dummies_and_odds.csv')

data['Team 1 Win'] = data.apply(lambda x: 1 if (x['Spread'] > 0) else 0, axis=1)
X = data.drop(['Total',
               'Spread',
               'Total Score Close',
               'Total Score Over Close',
               'Team 1 Odds Close',
               'Team 2 Odds Close',
               'Team 1 Line Close',
               'Team 1 Line Odds Close',
               'Team 1 Win'], axis=1).values

y = data['Team 1 Win'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.199, random_state=42)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# print(X_train.shape)
# >>(376, 152)

model = Sequential()
model.add(Dense(units=152, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=304, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=608, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam')

early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=25)

model.fit(x=X_train,
          y=y_train,
          epochs=600,
          validation_data=(X_test, y_test),
          callbacks=[early_stop],
          verbose=1)

model_loss = pd.DataFrame(model.history.history)
model_loss.plot()

predictions = model.predict_classes(X_test)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))