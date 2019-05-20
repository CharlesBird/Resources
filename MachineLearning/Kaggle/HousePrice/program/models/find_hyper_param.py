from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

from data_process import data_train_process

data_train = data_train_process()
train_np = data_train.values
y = train_np[:, 0]
X = train_np[:, 1:]


def find_LinearRegression_hyper_param():
    # 设置了fit_intercept=True,normalize=True时 数据会归一化
    param_grid = [
        {
            'fit_intercept': [False, True],
            'normalize': [True],
            'copy_X': [False, True]
        },
    ]
    grid_search = GridSearchCV(LinearRegression(), param_grid, n_jobs=-1, verbose=1, cv=5)
    grid_search.fit(X, y)
    print('best_lin_reg_score', grid_search.best_score_)
    print('best_lin_reg_param', grid_search.best_params_)
    return grid_search.best_estimator_


def find_RidgeCV_hyper_param():
    # 设置了fit_intercept=True,normalize=True时 数据会归一化
    param_grid = [
        {
            'alphas': [(0.1, 1.0, 10.0), (1, 10.0, 100.0)],
            'fit_intercept': [False, True],
            'normalize': [False, True]
        },
    ]
    grid_search = GridSearchCV(RidgeCV(), param_grid, n_jobs=-1, verbose=1, cv=5)
    grid_search.fit(X, y)
    print('best_rid_reg_score', grid_search.best_score_)
    print('best_rid_reg_param', grid_search.best_params_)
    return grid_search.best_estimator_


def find_RandomForestRegressor_hyper_param():
    param_grid = [
        {
            'n_estimators': [100, 200, 500],
            'max_depth': [None, 1, 10],
            # 'min_samples_leaf': [1],
            # 'max_leaf_nodes': [None, 5, 10],
            'oob_score': [True],
            'random_state': [100, 300, 500]
        },
    ]
    grid_search = GridSearchCV(RandomForestRegressor(), param_grid, n_jobs=-1, verbose=1, cv=5)
    grid_search.fit(X, y)
    print('best_Forest_reg_score', grid_search.best_score_)
    print('best_Forest_reg_param', grid_search.best_params_)
    return grid_search.best_estimator_


def find_GradientBoostingRegressor_hyper_param():
    param_grid = [
        {
            'loss': ['ls'],
            'n_estimators': [100, 200, 500],
            'max_depth': [3],
            'min_samples_leaf': [3],
            'max_leaf_nodes': [4],
            'random_state': [100, 300, 500],
            # 'tol': [1e-3, 1e-4, 1e-5]
        },
    ]
    grid_search = GridSearchCV(GradientBoostingRegressor(), param_grid, n_jobs=-1, verbose=1, cv=5)
    grid_search.fit(X, y)
    print('best_Gradient_reg_score', grid_search.best_score_)
    print('best_Gradient_reg_param', grid_search.best_params_)
    return grid_search.best_estimator_


def find_AdaBoostRegressor_hyper_param():
    # 可以不使用，留存
    param_grid = [
        {
            'n_estimators': [50, 100, 200],
            'loss': ['linear', 'square', 'exponential'],
            'random_state': [100, 300, 500],
        },
    ]
    grid_search = GridSearchCV(AdaBoostRegressor(), param_grid, n_jobs=-1, verbose=1, cv=5)
    grid_search.fit(X, y)
    print('best_AdaBoost_reg_score', grid_search.best_score_)
    print('best_AdaBoost_reg_param', grid_search.best_params_)
    return grid_search.best_estimator_


def find_DecisionTreeRegressor_hyper_param():
    # 可以不使用，留存
    param_grid = [
        {
            'min_samples_split': [0.1, 0.5, 1.0],
            'random_state': [100, 300, 500, 1000],
        },
    ]
    grid_search = GridSearchCV(DecisionTreeRegressor(), param_grid, n_jobs=-1, verbose=1, cv=5)
    grid_search.fit(X, y)
    print('best_DecisionTree_reg_score', grid_search.best_score_)
    print('best_DecisionTree_reg_param', grid_search.best_params_)
    return grid_search.best_estimator_


def find_ExtraTreeRegressor_hyper_param():
    # 可以不使用，留存
    param_grid = [
        {
            # 'max_depth': [None, 3, 5],
            'min_samples_leaf': [i for i in range(1, 10)],
            # 'max_leaf_nodes': [None, 3, 5],
            'random_state': [100, 300, 500, 1000],
        },
    ]
    grid_search = GridSearchCV(ExtraTreeRegressor(), param_grid, n_jobs=-1, verbose=1, cv=5)
    grid_search.fit(X, y)
    print('best_ExtraTree_reg_score', grid_search.best_score_)
    print('best_ExtraTree_reg_param', grid_search.best_params_)
    return grid_search.best_estimator_


if __name__ == '__main__':
    find_LinearRegression_hyper_param()
    find_RidgeCV_hyper_param()
    find_RandomForestRegressor_hyper_param()
    find_GradientBoostingRegressor_hyper_param()
    find_AdaBoostRegressor_hyper_param()
    find_DecisionTreeRegressor_hyper_param()
    find_ExtraTreeRegressor_hyper_param()