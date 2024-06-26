# import libraries

# 1. to handle the data
import pandas as pd
import numpy as np

# 2. To Viusalize the data
import matplotlib.pyplot as plt
import seaborn as sns

#3.To split the data 
from sklearn.model_selection import train_test_split


#to test the model 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score , recall_score , accuracy_score , f1_score

#loading the data 

df = pd.read_csv('heart_disease_health_indicators_BRFSS2015.csv')



x = df.drop('HeartDiseaseorAttack', axis =1)
y = df['HeartDiseaseorAttack']

#splitting the data for training and testing the data 

x_train, x_test , y_train, y_test=train_test_split(x, y, random_state=200, test_size=0.25, shuffle= True )

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


from sklearn.tree import DecisionTreeClassifier 


model =DecisionTreeClassifier()
model.fit(x_train, y_train)

print("train shape: " + str(x_train.shape))
print("score on test: " + str(model.score(x_test, y_test)))
print("score on train: "+ str(model.score(x_train, y_train)))

dt_y_predicts = model.predict(x_test)


accuracy = accuracy_score(y_test, dt_y_predicts)
print('Accuracy = '+ str(accuracy))

f1 = f1_score(y_test, dt_y_predicts)
print('f1 score = '+ str(f1))

recall = recall_score(y_test, dt_y_predicts)
print('recall = '+ str(recall))

precision = precision_score(y_test, dt_y_predicts)
print('precision = '+ str(precision))

dt_cm = confusion_matrix(y_test, dt_y_predicts)
print('confusion matrix'+ str(dt_cm))