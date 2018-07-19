from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
import pandas as pd
import numpy as np
import os
data_train = pd.read_csv(os.path.abspath(os.path.dirname(os.getcwd())) + '/train.csv' )
from data_preprocess import data_process
data_train, data_test = data_process()
train_df = data_train.filter(regex='Survived|Name_lenth_.*|Age_.*|SibSp_.*|Parch_.*|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
train_np = train_df.values
y = train_np[:, 0]
X = train_np[:, 1:]

test_df = data_test.filter(regex='Name_lenth_.*|Age_.*|SibSp_.*|Parch_.*|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
X_test = test_df.values


def get_training_goals(X, y, X_test):
    # 集成学习
    voting_clf = VotingClassifier(estimators=[
        ('log_clf', LogisticRegression(penalty='l1', tol=1e-4, C=0.5)),
        ('svm_clf', SVC(C=1.0, kernel='rbf', gamma=0.1, probability=True, random_state=0)),
        ('dt_clf', DecisionTreeClassifier(criterion='gini', max_leaf_nodes=20, random_state=1000)),
        ('rf_clf', RandomForestClassifier(n_estimators=500, max_leaf_nodes=30, random_state=1000)),
        ('gb_clf', GradientBoostingClassifier(n_estimators=100, max_leaf_nodes=15, random_state=666))
    ], voting='soft')
    voting_clf.fit(X, y)
    predict_y = voting_clf.predict(X_test)
    return predict_y


if __name__ == '__main__':
    predict = get_training_goals(X, y, X_test)
    result = pd.DataFrame({'PassengerId': data_test['PassengerId'].values, 'Survived': predict.astype(np.int64)})
    result.to_csv(os.path.abspath(os.path.dirname(os.getcwd())) + '/predict.csv', index=False)