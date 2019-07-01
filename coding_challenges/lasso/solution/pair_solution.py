#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Using the lasso for model specification
#Jeremy Kedziora
#4/18/2016
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

from sklearn.linear_model import Lasso
from sklearn.cross_validation import KFold
import pandas as pd
import numpy as np


#define functions
def maker(N, n_vars, p):
    """A function to generate Monte Carlo linear regression data"""
    x = []  #an empty list to hold the data
    y = np.zeros(N)  #an array to hold the dependent variable
    b = []  #an empty list to hold the true bs
    i = 1
    while i <= n_vars:  #loop over the variables we want to create
        x_i = np.random.normal(loc=0.0, scale=1.0, size=N)  #generate the data
        x.append(x_i)  #add it to the list of data
        if np.random.uniform(0, 1) < p:  #if the variable matters...
            b_i = np.random.normal(
                loc=0.0, scale=1.0)  #draw a random effect for this variable
        else:
            b_i = 0  #otherwise set it's true effect equal to 0.
        b.append(b_i)  #add it to the list of effects
        y = y + b_i * x_i  #add the variable effect to the dependent variable
        i += 1  #index up i

    b_i = np.random.normal(loc=0.0, scale=1.0)  #draw a random intercept
    b.append(b_i)  #append this intercept to the effects
    y = b_i + y + np.random.normal(
        loc=0.0, scale=1.0,
        size=N)  #add the normally distributed error term and the intercept
    return [np.array(x), np.array(y), np.array(b)]


#make the data
N = 2000  #the number of observations
data = maker(N, 20,
             0.7)  #generate the data assuming that 70% of variables matter
y = data[1]  #pull out the dependent variable
X = data[0].T  #pull out the independent variable

#X = pd.DataFrame(X)
#X['y'] = y
#X.to_csv('Lasso_practice_data.csv')
X = pd.read_csv('Lasso_practice_data.csv')
y = X['y']
X = X.drop('y', 1)
X = np.array(X)
y = np.array(y)

#tune the lambda parameter by applying k-fold cross validation
kf = KFold(N, n_folds=5)  #produce the k folds

Lambda = np.arange(0.001, 1.0, 0.001)  #a list of lambdas
Prediction_error = []  #an empty list to hold the prediction error

for l in Lambda:  #loop over lambdas
    pe = 0.0  #initialize prediction error
    for train_index, test_index in kf:  #loop over the folds
        X_train, X_test = X[train_index], X[
            test_index]  #create training and test independent variable data
        y_train, y_test = y[train_index], y[
            test_index]  #create training and test dependent variable data

        model = Lasso(l)  #create the model object
        results = model.fit(X_train, y_train)  #fit the model
        pe += sum(
            (model.predict(X_test) - y_test)
            **2)  #predict the test data, compute the error, and add to total
    Prediction_error.append(pe)  #append the prediction error

#run the lasso:
#Lambda = sum(((1.0/np.array(Prediction_error))/sum(1.0/np.array(Prediction_error)))*np.array(Lambda))    #compute lambda as the weighted average
model = Lasso(Lambda[Prediction_error.index(
    min(Prediction_error))])  #generate a model object
results = model.fit(X, y)  #fit the model
for i, j in zip(results.coef_, data[2]):  #loop over results
    print('Lasso:', round(i, 4), '    True',
          round(j, 4))  #print and compare with the truth
