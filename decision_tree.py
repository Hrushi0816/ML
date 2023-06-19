# -*- coding: utf-8 -*-
"""Decision Tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LjJVWttyReuYqan03P2P7fFSpt1mBUSw
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = {
    'Id':[1,2,3,4,5,6,7,8,9,10,11,12,13,14],
    'Age':['<21','<21','21-35','>35','>35','>35','21-35','<21','<21','>35','<21','21-35','21-35','>35'],
    'Income':['High','High','High','Medium','Low','Low','Low','Medium','Low','Medium','Medium','Medium','High','Medium'],
    'Gender':['Male','Male','Male','Male','Female','Female','Female','Male','Female','Female','Female','Male','Female','Male'],
    'MaritalStatus':['Single','Married','Single','Single','Single','Married','Married','Single','Married','Single','Married','Married','Single','Married'],
    'Buys':['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
}

df= pd.DataFrame(dataset)

from sklearn.preprocessing import LabelEncoder
le =LabelEncoder()

df['Age'] = le.fit_transform(df['Age'])
df['Income']= le.fit_transform(df['Income'])
df['Gender'] = le.fit_transform(df['Gender'])
df['MaritalStatus'] =le.fit_transform(df['MaritalStatus'])
df['Buys']=le.fit_transform(df['Buys'])

x= df.drop('Buys', axis=1)

y=df['Buys']

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(x,y)

model.tree_.feature[0]

x.columns[model.tree_.feature[0]]

from sklearn.tree import plot_tree
plt.figure(figsize=(15,10))
plot_tree(model, rounded= True,filled=True, class_names=['Yes','No'],feature_names=x.columns)
plt.show()

