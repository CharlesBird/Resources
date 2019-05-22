from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.decomposition import PCA

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

from data_process import data_train_process


def find_LinearRegression_hyper_param(X, y):
    # 设置了fit_intercept=True,normalize=True时 数据会归一化
    param_grid = [
        {
            'fit_intercept': [True],
            'normalize': [True],
            'copy_X': [False, True]
        },
    ]
    grid_search = GridSearchCV(LinearRegression(), param_grid, n_jobs=-1, verbose=1, cv=5)
    grid_search.fit(X, y)
    print('best_lin_reg_score', grid_search.best_score_)
    # 0.776011353040207
    print('best_lin_reg_param', grid_search.best_params_)
    # {'copy_X': False, 'fit_intercept': True, 'normalize': True}
    return grid_search.best_estimator_


def find_RidgeCV_hyper_param(X, y):
    # 设置了fit_intercept=True,normalize=True时 数据会归一化
    param_grid = [
        {
            'alphas': [(0.1, 1.0, 10.0)],
            'fit_intercept': [True],
            'normalize': [True]
        },
    ]
    grid_search = GridSearchCV(RidgeCV(), param_grid, n_jobs=-1, verbose=1, cv=5)
    grid_search.fit(X, y)
    print('best_rid_reg_score', grid_search.best_score_)
    # 0.7715897804018855
    print('best_rid_reg_param', grid_search.best_params_)
    # {'alphas': (0.1, 1.0, 10.0), 'fit_intercept': True, 'normalize': True}
    return grid_search.best_estimator_


def find_LassoCV_hyper_param(X, y):
    # 设置了fit_intercept=True,normalize=True时 数据会归一化
    param_grid = [
        {
            'cv': [3, 4, 5],
            'fit_intercept': [True],
            'normalize': [True],
            'random_state': [100, 300, 500, 1000, 0]
        },
    ]
    grid_search = GridSearchCV(LassoCV(), param_grid, n_jobs=-1, verbose=1, cv=5)
    grid_search.fit(X, y)
    print('best_LassoCV_score', grid_search.best_score_)
    # 0.7690358984932986
    print('best_LassoCV_param', grid_search.best_params_)
    # {'cv': 4, 'fit_intercept': True, 'normalize': True, 'random_state': 100}
    return grid_search.best_estimator_


def find_RandomForestRegressor_hyper_param(X, y):
    param_grid = [
        {
            'n_estimators': [100, 200, 500],
            'max_depth': [None, 3, 5, 10],
            'min_samples_leaf': [1, 2, 3],
            'max_leaf_nodes': [None, 5, 10],
            'oob_score': [True],
            'random_state': [0, 100, 300, 500]
        },
    ]
    grid_search = GridSearchCV(RandomForestRegressor(), param_grid, n_jobs=-1, verbose=1, cv=5)
    grid_search.fit(X, y)
    print('best_Forest_reg_score', grid_search.best_score_)
    # 0.8423066988062821
    print('best_Forest_reg_param', grid_search.best_params_)
    # {'max_depth': 10, 'n_estimators': 100, 'oob_score': True, 'random_state': 500}
    return grid_search.best_estimator_


def find_GradientBoostingRegressor_hyper_param(X, y):
    param_grid = [
        {
            'loss': ['ls'],
            'n_estimators': [100, 200, 500],
            'max_depth': [3, 5, 6],
            'min_samples_leaf': [3],
            'max_leaf_nodes': [3,5,6,7],
            'random_state': [100, 300, 500, 1000, 0],
            # 'tol': [1e-3, 1e-4, 1e-5]
        },
    ]
    grid_search = GridSearchCV(GradientBoostingRegressor(), param_grid, n_jobs=-1, verbose=1, cv=5)
    grid_search.fit(X, y)
    print('best_Gradient_reg_score', grid_search.best_score_)
    # 0.8704253429884784
    print('best_Gradient_reg_param', grid_search.best_params_)
    # {'loss': 'ls', 'max_depth': 3, 'max_leaf_nodes': 4, 'min_samples_leaf': 3, 'n_estimators': 500, 'random_state': 100}
    return grid_search.best_estimator_


def find_AdaBoostRegressor_hyper_param(X, y):
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
    # 0.7988266356486099
    print('best_AdaBoost_reg_param', grid_search.best_params_)
    # {'loss': 'exponential', 'n_estimators': 50, 'random_state': 500}
    return grid_search.best_estimator_


def find_DecisionTreeRegressor_hyper_param(X, y):
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
    # 0.7171158994667575
    print('best_DecisionTree_reg_param', grid_search.best_params_)
    # {'min_samples_split': 0.1, 'random_state': 100}
    return grid_search.best_estimator_


def find_ExtraTreeRegressor_hyper_param(X, y):
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
    # 0.7957707433747737
    print('best_ExtraTree_reg_param', grid_search.best_params_)
    # {'min_samples_leaf': 3, 'random_state': 100}
    return grid_search.best_estimator_


def get_data_in_pca(X, y, n_components='mle'):
    # PCA 降维
    pca = PCA(n_components=n_components)
    pca.fit(X, y)
    X_reduction = pca.transform(X)
    return X_reduction

if __name__ == '__main__':
    data_train = data_train_process()
    train_np = data_train.values
    y = train_np[:, 0]
    X = train_np[:, 1:]

    # find_LinearRegression_hyper_param(X, y)
    # find_RidgeCV_hyper_param(X, y)
    # find_LassoCV_hyper_param(X, y)
    # find_RandomForestRegressor_hyper_param(X, y)
    find_GradientBoostingRegressor_hyper_param(X, y)
    # find_AdaBoostRegressor_hyper_param(X, y)
    # find_DecisionTreeRegressor_hyper_param(X, y)
    # find_ExtraTreeRegressor_hyper_param(X, y)
