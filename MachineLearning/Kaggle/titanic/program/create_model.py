from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVR
from sklearn.model_selection import train_test_split
from data_preprocess import data_process

data_train, data_test = data_process()
train_df = data_train.filter(regex='Survived|Name_lenth_.*|Age_.*|SibSp_.*|Parch_.*|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
train_np = train_df.values
y = train_np[:, 0]
X = train_np[:, 1:]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)

log_reg = LogisticRegression(penalty='l1', tol=1e-6, C=1.0)
log_reg.fit(X_train, y_train)
# print(log_reg)

# test_df = data_test.filter(regex='Name_lenth_.*|Age_.*|SibSp_.*|Parch_.*|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
# X_test = test_df.values
predict_y = log_reg.predict(X_test)
score = log_reg.score(X_test, y_test)
print(score)

svr = LinearSVR(tol=1e-6, epsilon=0.1, C=1.0)
svr.fit(X_train, y_train)
predict_y = svr.predict(X_test)
score = svr.score(X_test, y_test)
print(score)