import pandas as pd
import re
import os
data_train = pd.read_csv(os.path.abspath(os.path.dirname(os.getcwd())) + '/train.csv')
data_test = pd.read_csv(os.path.abspath(os.path.dirname(os.getcwd())) + '/test.csv')

cols = ['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF', 'FullBath', 'TotRmsAbvGrd',
        'YearBuilt', 'YearRemodAdd', 'PoolArea', 'Fireplaces', 'CentralAir', 'KitchenAbvGr']
X_train = data_train[cols]
print(X_train.info())

X_test = data_test[cols]
print(X_test.info())