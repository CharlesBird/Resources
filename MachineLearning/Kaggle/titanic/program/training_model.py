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
train_df = data_train.filter(regex='Survived|Name_lenth_.*|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass')
train_np = train_df.values
y = train_np[:, 0]
X = train_np[:, 1:]

test_df = data_test.filter(regex='Name_lenth_.*|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass')
X_test = test_df.values


def get_training_goals(X, y, X_test):
    # 集成学习
    voting_clf = VotingClassifier(estimators=[
        ('log_clf', LogisticRegression(penalty='l2', tol=1e-4, C=0.1, multi_class='multinomial', solver='newton-cg')),
        ('svm_clf', SVC(C=1.5, kernel='rbf', gamma='auto', tol=1e-3, probability=True, random_state=0)),
        ('dt_clf', DecisionTreeClassifier(criterion='gini', max_leaf_nodes=20, random_state=300)),
        ('rf_clf', RandomForestClassifier(n_estimators=100, max_leaf_nodes=20, random_state=2000)),
        ('gb_clf', GradientBoostingClassifier(n_estimators=100, max_leaf_nodes=15, random_state=500))
    ], voting='soft')
    voting_clf.fit(X, y)
    predict_y = voting_clf.predict(X_test)
    return predict_y


if __name__ == '__main__':
    from sklearn.metrics import accuracy_score
    predict = get_training_goals(X, y, X_test)
    # data_y = pd.read_csv(os.path.abspath(os.path.dirname(os.getcwd())) + '/gender_submission.csv')
    # y = data_y['Survived'].values
    # score = accuracy_score(y, predict.astype(np.int64))
    # print(score)
    result = pd.DataFrame({'PassengerId': data_test['PassengerId'].values, 'Survived': predict.astype(np.int64)})
    result.to_csv(os.path.abspath(os.path.dirname(os.getcwd())) + '/predict.csv', index=False)