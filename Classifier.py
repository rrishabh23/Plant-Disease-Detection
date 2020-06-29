

import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

br = pd.read_csv('featuredataset/Color_Apple_blackrot.csv')
hh = pd.read_csv('featuredataset/Color_Apple_healthy.csv')

br = br.drop(['imgid'], axis=1)
br['Infected'] = 1

hh = hh.drop(['imgid'], axis=1)
hh['Infected'] = 0


full = hh.append(br)
y = full['Infected']
X = full.drop('Infected', axis=1)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=3)


classifier = XGBClassifier()
classifier.fit(x_train, y_train)
acc = classifier.score(x_test, y_test)
print("\nClassifier Accuracy : ",acc*100,'%')
#-------------88% Accuracy

'''
import tensorflow
from keras.models import Sequential
from keras.layers import Dense,Dropout
from sklearn.metrics import confusion_matrix

model = Sequential()
model.add(Dense(units=1024, activation='relu', input_shape=(5,)))
model.add(Dense(units=256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

model.fit(x_train, y_train, epochs=100)
test_loss, test_accuracy = model.evaluate(x_test, y_test)

out=model.predict(X)
y_pred = pd.Series([int(i>0.5) for i in out])
confusion_matrix(y, y_pred)
#-------------89% Accuracy
'''
def test_image():
    x_in = pd.read_csv('featuredataset/test.csv')
    x_in = x_in.drop(['imgid'], axis=1)
    if classifier.predict(x_in)[0] == 1:
        print('The Leaf is Infected!')
    else:
        print('The Leaf is Healthy!')
