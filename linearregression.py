

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

my_dict = {
    'height': [151, 174, 138, 186, 128, 136, 179, 163, 152, 131],
    'weight': [63, 81, 56, 91, 47, 57, 76, 72, 62, 48]
}

df = pd.DataFrame(my_dict)

x = df[['height']]
y = df[['weight']]

df.isnull().sum()


x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=10)

model = LinearRegression()

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

plt.scatter(x_test, y_test, color='blue')
plt.plot(x_test, y_predict, color='red')
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Linear Regression Model")

print("Accuracy Taining", x_train, y_train)
print("Accuracy Testing", x_test, y_predict)

model.predict([[180]])
