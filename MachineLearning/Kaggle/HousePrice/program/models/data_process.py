import pandas as pd
from sklearn.preprocessing import StandardScaler
import os
data_train = pd.read_csv(os.path.abspath(os.path.join(os.getcwd(), "../..")) + '/train.csv')
data_test = pd.read_csv(os.path.abspath(os.path.join(os.getcwd(), "../..")) + '/test.csv')

cols = ['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF', 'FullBath', 'TotRmsAbvGrd',
        'YearBuilt', 'YearRemodAdd', 'PoolArea', 'Fireplaces', 'CentralAir', 'KitchenAbvGr']

X_train = data_train[cols].copy()
X_test = data_test[cols].copy()


def set_PoolArea(df):
    # 有无泳池设置
    df['HasPool'] = df.PoolArea.map(lambda x: 1 if x > 0 else 0)
    return df


def set_Garage(df):
    # 车库面积设为0
    df.loc[(df.GarageCars.isnull()), 'GarageCars'] = 0
    df.loc[(df.GarageArea.isnull()), 'GarageArea'] = 0
    return df

def set_TotalBsmtSF(df):
    # 面积设为0
    df.loc[(df.TotalBsmtSF.isnull()), 'TotalBsmtSF'] = 0
    return df


def data_train_process():
    global X_train
    data_res = set_PoolArea(X_train)
    dummies_CentralAir = pd.get_dummies(data_res['CentralAir'], prefix='CentralAir', dtype='int64')
    data_res = pd.concat([data_res, dummies_CentralAir], axis=1)
    data_res.drop(['CentralAir'], axis=1, inplace=True)
    data_res = pd.concat([data_train['SalePrice'],data_res], axis=1)
    return data_res


def data_test_process():
    global X_test
    data_res = set_PoolArea(X_test)
    data_res = set_Garage(data_res)
    data_res = set_TotalBsmtSF(data_res)
    dummies_CentralAir = pd.get_dummies(data_res['CentralAir'], prefix='CentralAir', dtype='int64')
    data_res = pd.concat([data_res, dummies_CentralAir], axis=1)
    data_res = pd.concat([data_test['Id'], data_res], axis=1)
    data_res.drop(['CentralAir'], axis=1, inplace=True)
    return data_res


if __name__ == '__main__':
    # data_res = data_train_process()
    # print(data_res)
    data_res = data_test_process()
    data_res.info()
