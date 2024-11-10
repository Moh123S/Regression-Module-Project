# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ngjxk3_cRMcqvc8wkh0wkrwpbRr9kSLU
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("/content/placement.csv")

dataset.head(3)

x = dataset[["cgpa"]]
y = dataset["package"]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state = 42)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train,y_train)

lr.predict([[6.89]])



y_prd = lr.predict(x)

plt.figure(figsize=(5,4))
sns.scatterplot(x="cgpa",y="package",data=dataset)
plt.plot(dataset['cgpa'],y_prd,c="red")
plt.legend(["org","predict line"])
plt.savefig("predict.jpg")
plt.show()





"""MULTIPLE LINEAR REGRESSION"""

dataset = pd.read_csv("/content/multiple_linear_regression_dataset.csv")

dataset.head(3)

sns.pairplot(data = dataset)
plt.show()

sns.heatmap(dataset.corr(),annot=True)
plt.show()

from google.colab import drive
drive.mount('/content/drive')

dataset.shape

x = dataset.iloc[:,:-1]
y = dataset["income"]

x.ndim

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state = 42)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train,y_train)

lr.coef_

lr.intercept_

lr.score(x_test,y_test)*100

lr.predict(x_test)





"""POLYNOMIAL REGRESSION"""

dataset = pd.read_csv("/content/salary.csv")

dataset.head(3)

dataset.ndim

dataset.columns = dataset.columns.str.strip()

# Assuming 'dataset' is your DataFrame and you want to drop the column at index 2
dataset = dataset.drop(dataset.columns[0], axis=1)

dataset.corr()

plt.figure(figsize=(5,3))
sns.scatterplot(x=dataset["Level"],y=dataset["Salary"])
plt.show()

dataset = dataset.rename(columns={'Level': 'level'})

dataset.columns = dataset.columns.str.strip()

x = dataset[['Level']]
y = dataset["Salary"]

from sklearn.preprocessing import PolynomialFeatures

pf = PolynomialFeatures(degree=2)
pf.fit(x)
x = pf.transform(x)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state = 42)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train,y_train)

lr.score(x_test,y_test)*100

prd = lr.predict(x)

plt.figure(figsize=(5,3))
sns.scatterplot(x=dataset["Level"],y=dataset["Salary"])
plt.plot(dataset["Level"],lr.predict(x),c="red")
plt.legend(["org","predict line"])
plt.show()



test = pf.transform([[5]])
test

lr.predict(test)

"""gernaly it is show how to pridict valve bytheway it is wrong pridiction because data is not correct"""





