import numpy as np


def accuracy_score(y_true, y_predict):
    """计算y_true与y_predict之间的准确率"""
    assert len(y_predict) == len(y_true), "the size of y_predict is equal to the size of y_true."

    return np.sum(y_predict == y_true) / len(y_true)


def mean_squared_error(y_true, y_predict):
    assert len(y_true) == len(y_predict), "the size of y_predict is equal to the size of y_true."
    return np.sum((y_true - y_predict) ** 2) / len(y_true)


def root_mean_squared_error(y_true, y_predict):
    assert len(y_true) == len(y_predict), "the size of y_predict is equal to the size of y_true."
    return np.sqrt(np.sum((y_true - y_predict) ** 2) / len(y_true))


def mean_absolute_error(y_true, y_predict):
    assert len(y_true) == len(y_predict), "the size of y_predict is equal to the size of y_true."
    return np.sum(np.absolute(y_true - y_predict)) / len(y_true)