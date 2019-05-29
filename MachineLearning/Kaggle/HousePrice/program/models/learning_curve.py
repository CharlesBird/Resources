from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split, learning_curve, ShuffleSplit
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from data_process import process_main


# 学习曲线
def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None, train_sizes=np.linspace(0.1, 1.0, 5), n_jobs=1, random_state=None):
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, train_sizes=train_sizes, cv=cv, n_jobs=n_jobs, random_state=random_state)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.legend(loc="best")
    plt.show()


# def ridCV_polynomialregression(degree):
#     return Pipeline([
#         ('poly', PolynomialFeatures(degree=degree)),
#         ('rid_reg', RidgeCV(alphas=(0.1, 1.0, 10.0), fit_intercept=True, normalize=True))
#     ])
#
# def forest_polynomialregression(degree):
#     return Pipeline([
#         ('poly', PolynomialFeatures(degree=degree)),
#         ('rf_reg', RandomForestRegressor(max_depth=10, n_estimators=100, oob_score=True, random_state=500))
#     ])
#
#
# def gb_polynomialregression(degree=2):
#     return Pipeline([
#         ('poly', PolynomialFeatures(degree=degree)),
#         ('gb_reg', GradientBoostingRegressor(loss='ls', max_depth=3, max_leaf_nodes=4, min_samples_leaf=3, n_estimators=500, random_state=100))
#     ])
#
#
# def ad_polynomialregression(degree=2):
#     return Pipeline([
#         ('poly', PolynomialFeatures(degree=degree)),
#         ('std_scaler', StandardScaler()),
#         ('gb_reg', AdaBoostRegressor(loss='exponential', n_estimators=50, random_state=500))
#     ])
#
#
if __name__ == '__main__':
    data_train, data_test = process_main()
    train_np = data_train.values
    y = train_np[:, 0]
    X = train_np[:, 1:]
    cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=666)
    title = 'Learning Curves (Random Forest)'
    estimator1 = RandomForestRegressor(n_estimators=100, oob_score=True, random_state=500)
    plot_learning_curve(estimator1, title, X, y, ylim=(0.7, 1.01), train_sizes=np.linspace(0.1, 1.0, 10), cv=cv, n_jobs=1, random_state=666)

    title = 'Learning Curves (Gradient Boosting)'
    estimator2 = GradientBoostingRegressor(loss='ls', max_depth=3, max_leaf_nodes=10, min_samples_leaf=1, n_estimators=200, random_state=100)
    plot_learning_curve(estimator2, title, X, y, ylim=(0.7, 1.01), train_sizes=np.linspace(0.1, 1.0, 10), cv=cv, n_jobs=1, random_state=666)

#     pca = PCA(n_components=0.98)
#     X = pca.fit_transform(X)
#     X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)
#
#     poly_reg = forest_polynomialregression(degree=4)
#     poly_reg.fit(X_train, y_train)
#     y_train_predict = poly_reg.predict(X_train)
#     y_test_predict = poly_reg.predict(X_test)
#     res_train = mean_squared_error(y_train, y_train_predict)
#     res_test = mean_squared_error(y_test, y_test_predict)
#     print(res_train, res_test)
    # degree=2 135464430.0332776 818786809.8635224
    # degree=3 124665221.86368628 734563453.5463767

    # plot_learning_curve(forest_polynomialregression(degree=2), X_train, X_test, y_train, y_test)

    # plot_learning_curve(gb_polynomialregression(degree=2), X_train, X_test, y_train, y_test)

    # plot_learning_curve(Lin_polynomialregression(degree=2), X_train, X_test, y_train, y_test)

    # plot_learning_curve(ridCV_polynomialregression(degree=3), X_train, X_test, y_train, y_test)

    # plot_learning_curve(ad_polynomialregression(degree=5), X_train, X_test, y_train, y_test)