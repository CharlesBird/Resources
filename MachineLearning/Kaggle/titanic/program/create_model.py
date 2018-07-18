from sklearn.linear_model import LogisticRegression
from data_preprocess import data_process

data_train, data_test = data_process()
train_df = data_train.filter(regex='Survived|Name_lenth_.*|Age_.*|SibSp_.*|Parch_.*|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
train_np = train_df.values
y_train = train_np[:, 0]
X_train = train_np[:, 1:]
# print(X_train.shape, y_train.shape)
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
print(log_reg)

test_df = data_test.filter(regex='Name_lenth_.*|Age_.*|SibSp_.*|Parch_.*|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
X_test = test_df.values
predict_y = log_reg.predict(X_test)
print(predict_y)