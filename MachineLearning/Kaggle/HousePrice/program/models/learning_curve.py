from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from data_process import data_train_process
data_train = data_train_process()
train_np = data_train.values
y = train_np[:, 0]
X = train_np[:, 1:]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)


# 学习曲线
def plot_learning_curve(algo, X_train, X_test, y_train, y_test):
    train_score = []
    test_score = []
    for i in range(10, len(X_train) + 1, 5):
        algo.fit(X_train[:i], y_train[:i])

        y_train_predict = algo.predict(X_train[:i])
        train_score.append(mean_squared_error(y_train[:i], y_train_predict))

        y_test_predict = algo.predict(X_test[:i])
        test_score.append(mean_squared_error(y_test[:i], y_test_predict))

    plt.plot([i for i in range(10, len(X_train) + 1, 5)], np.sqrt(train_score), label="train")
    plt.plot([i for i in range(10, len(X_train) + 1, 5)], np.sqrt(test_score), label="test")
    plt.legend()
    plt.axis([0, len(X_train) + 1, 0, 40000])
    plt.show()


def Lin_polynomialregression(degree):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        # ('std_scaler', StandardScaler()),
        ('lin_reg', LinearRegression(copy_X=False, fit_intercept=True, normalize=True))
    ])


def ridCV_polynomialregression(degree):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('rid_reg', RidgeCV(alphas=(0.1, 1.0, 10.0), fit_intercept=True, normalize=True))
    ])

def forest_polynomialregression(degree):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('rf_reg', RandomForestRegressor(max_depth=10, n_estimators=100, oob_score=True, random_state=500))
    ])


def gb_polynomialregression(degree=2):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('std_scaler', StandardScaler()),
        ('gb_reg', GradientBoostingRegressor(loss='ls', max_depth=3, max_leaf_nodes=4, min_samples_leaf=3, n_estimators=500, random_state=100))
    ])


def ad_polynomialregression(degree=2):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('std_scaler', StandardScaler()),
        ('gb_reg', AdaBoostRegressor(loss='exponential', n_estimators=50, random_state=500))
    ])


if __name__ == '__main__':
    plot_learning_curve(forest_polynomialregression(degree=10), X_train, X_test, y_train, y_test)

    plot_learning_curve(gb_polynomialregression(degree=10), X_train, X_test, y_train, y_test)

    # plot_learning_curve(Lin_polynomialregression(degree=2), X_train, X_test, y_train, y_test)

    # plot_learning_curve(ridCV_polynomialregression(degree=3), X_train, X_test, y_train, y_test)

    # plot_learning_curve(ad_polynomialregression(degree=5), X_train, X_test, y_train, y_test)