from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from data_preprocess import data_process

data_train, data_test = data_process()
train_df = data_train.filter(regex='Survived|Name_lenth_.*|Age_.*|SibSp_.*|Parch_.*|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
train_np = train_df.values
y = train_np[:, 0]
X = train_np[:, 1:]


def find_log_reg_hyper_param():
    param_grid = [
        {
            'penalty': ['l1', 'l2'],
            'tol': [1e-4, 1e-5, 1e-6, 1e-7],
            'C': [0.1, 0.5, 1, 1.5, 10]
        },
        {
            'penalty': ['l2'],
            'tol': [1e-4, 1e-5, 1e-6, 1e-7],
            'C': [0.1, 0.5, 1, 1.5, 10],
            'multi_class': ['multinomial'],
            'solver': ['newton-cg']
        }
    ]
    grid_search = GridSearchCV(LogisticRegression(), param_grid, n_jobs=-1, verbose=1)
    grid_search.fit(X, y)
    print('best_log_reg_score', grid_search.best_score_)
    print('best_log_reg_param', grid_search.best_params_)
    return grid_search.best_estimator_


def find_svc_hyper_param():
    param_grid = [
        {
            'kernel': ['rbf'],
            'gamma': ['auto', 0.1, 0.01, 1, 100],
            'C': [0.1, 0.5, 1, 1.5, 10],
            'tol': [1e-3, 1e-4, 1e-5],
            'random_state': [0, 100, 300, 666],
            'probability': [True]
        },
    ]
    grid_search = GridSearchCV(SVC(), param_grid, n_jobs=-1, verbose=1)
    grid_search.fit(X, y)
    print('best_svc_score', grid_search.best_score_)
    print('best_svc_param', grid_search.best_params_)
    return grid_search.best_estimator_


def find_rb_forest_hyper_param():
    param_grid = [
        {
            'n_estimators': [100, 200, 500, 1000],
            'max_leaf_nodes': [10, 15, 20, 25, 30],
            'random_state': [300, 400, 500, 666, 1000, 2000]
        },
    ]
    grid_search = GridSearchCV(RandomForestClassifier(), param_grid, n_jobs=-1, verbose=1)
    grid_search.fit(X, y)
    print('best_rb_forest_score', grid_search.best_score_)
    print('best_rb_forest_param', grid_search.best_params_)
    return grid_search.best_estimator_


def find_gb_clf_hyper_param():
    param_grid = [
        {
            'n_estimators': [100, 200, 500, 1000],
            'max_leaf_nodes': [10, 15, 20, 25, 30],
            'random_state': [300, 400, 500, 666, 1000, 2000]
        },
    ]
    grid_search = GridSearchCV(GradientBoostingClassifier(), param_grid, n_jobs=-1, verbose=1)
    grid_search.fit(X, y)
    print('best_gb_clf_score', grid_search.best_score_)
    print('best_gb_clf_param', grid_search.best_params_)
    return grid_search.best_estimator_


def find_dt_clf_hyper_param():
    param_grid = [
        {
            'max_leaf_nodes': [10, 15, 20, 25, 30],
            'random_state': [300, 400, 500, 666, 1000, 2000]
        },
    ]
    grid_search = GridSearchCV(DecisionTreeClassifier(), param_grid, n_jobs=-1, verbose=1)
    grid_search.fit(X, y)
    print('best_gb_clf_score', grid_search.best_score_)
    print('best_gb_clf_param', grid_search.best_params_)
    return grid_search.best_estimator_


if __name__ == '__main__':
    # find_log_reg_hyper_param()
    # find_svc_hyper_param()
    # find_rb_forest_hyper_param()
    # find_gb_clf_hyper_param()
    find_dt_clf_hyper_param()