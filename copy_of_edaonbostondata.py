# -*- coding: utf-8 -*-
"""Copy of EDAonBostonData.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WXLzbeNKKG88ZdCr_Sz9PO48DEZ5EsO6
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

data= pd.read_csv('/content/Boston.csv')

data.head()

data.ZN.replace(0,np.nan,inplace = True)
data.CHAS.replace(0,np.nan,inplace=True)
data.info()

data.isnull().sum()/len(data) * 100

data = data.drop(['ZN','CHAS'],axis=1)
data.info()

sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.distplot(data['MEDV'], bins=30)
plt.show()

correlation_matrix = data.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)

from sklearn.model_selection import train_test_split
X = data.iloc[:,:-1]
y = data.iloc[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.30,random_state=0)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
from sklearn import metrics
print("MAE", metrics.mean_absolute_error(y_test, y_pred))
print("MSE", metrics.mean_squared_error(y_test, y_pred))
print("RMSE", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print("Score:", model.score(X_test, y_test))