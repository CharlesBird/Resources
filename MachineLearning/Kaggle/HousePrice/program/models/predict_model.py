from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.decomposition import PCA
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import VotingRegressor
import pandas as pd
import numpy as np
import os

from data_process import data_train_process, data_test_process


def forest_polynomialregression(degree=2):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        # ('std_scaler', StandardScaler()),
        ('rf_reg', RandomForestRegressor(max_depth=None, max_leaf_nodes=None, n_estimators=200, oob_score=True, random_state=100))
    ])


def gb_polynomialregression(degree=2):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        # ('std_scaler', StandardScaler()),
        ('gb_reg', GradientBoostingRegressor(loss='ls', max_depth=5, max_leaf_nodes=6, min_samples_leaf=3, n_estimators=200, random_state=1000))
    ])


def ls_polynomialregression(degree=2):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        # ('std_scaler', StandardScaler()),
        ('gb_reg', GradientBoostingRegressor(loss='ls', max_depth=5, max_leaf_nodes=6, min_samples_leaf=3, n_estimators=200, random_state=1000))
    ])


def get_training_goals(X, y, X_test):
    # 集成学习
    voting_reg = VotingRegressor(estimators=[
        ('rf_reg', forest_polynomialregression(degree=2)),
        ('gb_reg', gb_polynomialregression(degree=2)),
        # ('ls_reg', ls_polynomialregression(degree=2)),
        # ('ab_reg', AdaBoostRegressor(loss='exponential', n_estimators=50, random_state=500)),
        # ('et_reg', ExtraTreeRegressor(min_samples_leaf=3, random_state=100)),
        # ('rid_reg', RidgeCV(alphas=(0.1, 1.0, 10.0), fit_intercept=True, normalize=True))
    ])
    voting_reg.fit(X, y)
    predict_y = voting_reg.predict(X_test)
    return predict_y


if __name__ == '__main__':
    from sklearn.metrics import accuracy_score
    data_train = data_train_process()
    data_test = data_test_process()
    train_np = data_train.values
    X_test = data_test.values[:, 1:]
    y = train_np[:, 0]
    X = train_np[:, 1:]
    predict = get_training_goals(X, y, X_test)
    # data_y = pd.read_csv(os.path.abspath(os.path.dirname(os.getcwd())) + '/gender_submission.csv')
    # y = data_y['Survived'].values
    # score = accuracy_score(y, predict.astype(np.int64))
    # print(score)
    result = pd.DataFrame({'Id': data_test['Id'].values, 'SalePrice': predict.astype(np.float)})
    result.to_csv(os.path.abspath(os.path.abspath(os.path.join(os.getcwd(), "../.."))) + '/predict.csv', index=False)