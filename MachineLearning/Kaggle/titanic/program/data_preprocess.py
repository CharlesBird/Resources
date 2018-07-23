import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import os
data_train = pd.read_csv(os.path.abspath(os.path.dirname(os.getcwd())) + '/train.csv' )
data_test = pd.read_csv(os.path.abspath(os.path.dirname(os.getcwd())) + '/test.csv' )


def set_cabin(df):
    # 设置Cabin如果空值为No，有值为Yes
    df.loc[(df.Cabin.notnull()), 'Cabin'] = 'Yes'
    df.loc[(df.Cabin.isnull()), 'Cabin'] = 'No'
    return df


def set_title(df):
    # 设置称谓为5种，Mr,Mrs,Miss,noble,other
    import re
    df['Title'] = df.Name.map(lambda x: re.compile(",(.*?)\.").findall(x)[0])
    title_dict = {}
    title_dict.update(dict.fromkeys(['Mr'], 'mr'))
    title_dict.update(dict.fromkeys(['Mrs', 'Ms', 'Mme'], 'mrs'))
    title_dict.update(dict.fromkeys(['Miss', 'Mlle'], 'miss'))
    title_dict.update(dict.fromkeys(['Master', 'Sir', 'the Countess', 'Lady', 'Major', 'Mme', 'Col', 'Don', 'Dona'], 'noble'))
    title_dict.update(dict.fromkeys(['Rev', 'Dr', 'Jonkheer', 'Capt'], 'other'))
    # df['n_Title'] = df.Title.map(title_dict)
    titles = df['Title']
    for k, v in title_dict.items():
        titles[titles == k] = v
    df['n_Title'] = titles
    print(df)
    return df


def get_missing_embarked(df):
    # 缺失的不多使用众数填充
    df['Embarked'].fillna(df.Embarked.mode().iloc[0], inplace=True)
    return df


def set_missing_age(df_train, df_test):
    # 随机森林算法填补缺失年龄
    age_df = df_train[['Age', 'Fare', 'Pclass', 'Name_lenth', 'SibSp', 'Parch', 'Fare', 'Cabin_No', 'Cabin_Yes', 'Embarked_C', 'Embarked_Q', 'Embarked_S', 'Sex_female', 'Sex_male']]
    age_df_test = df_test[['Age', 'Fare', 'Pclass', 'Name_lenth', 'SibSp', 'Parch', 'Fare', 'Cabin_No', 'Cabin_Yes', 'Embarked_C', 'Embarked_Q', 'Embarked_S', 'Sex_female', 'Sex_male']]
    known_age = age_df[age_df.Age.notnull()].values
    unknown_age = age_df[age_df.Age.isnull()].values

    y = known_age[:, 0]
    X = known_age[:, 1:]
    rf_reg = RandomForestRegressor(n_estimators=1200, max_leaf_nodes=20, random_state=500, n_jobs=-1, oob_score=True)
    rf_reg.fit(X, y)
    predict_train_ages = rf_reg.predict(unknown_age[:, 1:])
    predict_test_ages = rf_reg.predict(age_df_test[age_df_test.Age.isnull()].values[:, 1:])
    df_train.loc[(df_train.Age.isnull()), 'Age'] = predict_train_ages
    df_test.loc[(df_test.Age.isnull()), 'Age'] = predict_test_ages
    return df_train, df_test


def set_data_standard(df_train, df_test):
    # 舱号，年龄，票价数据标准化
    standardScaler = StandardScaler()
    # standardScaler.fit(df_train[['Name_lenth', 'SibSp', 'Parch', 'Pclass', 'Age', 'Fare']].values)
    standardScaler.fit(df_train[['Name_lenth', 'Age', 'Fare']].values)
    df_train_scaled = standardScaler.transform(df_train[['Name_lenth', 'Age', 'Fare']].values)
    df_test_scaled = standardScaler.transform(df_test[['Name_lenth', 'Age', 'Fare']].values)
    df_train_scaled = pd.DataFrame(df_train_scaled, columns=['Name_lenth_scaled', 'Age_scaled', 'Fare_scaled'])
    df_train = pd.concat([df_train, df_train_scaled], axis=1)
    df_test_scaled = pd.DataFrame(df_test_scaled, columns=['Name_lenth_scaled', 'Age_scaled', 'Fare_scaled'])
    df_test = pd.concat([df_test, df_test_scaled], axis=1)
    return df_train, df_test


def data_process():
    # 填补缺失数据，数据标准化，数据转换
    # 测试数据缺少一个Fare数据，使用仓位平均值求得
    global data_train
    data_train = set_cabin(data_train)
    data_train = set_title(data_train)
    data_train = get_missing_embarked(data_train)
    data_train['Name_lenth'] = data_train.Name.apply(len)
    dummies_cabin = pd.get_dummies(data_train['Cabin'], prefix='Cabin')
    dummies_embarked = pd.get_dummies(data_train['Embarked'], prefix='Embarked')
    dummies_sex = pd.get_dummies(data_train['Sex'], prefix='Sex')
    data_train = pd.concat([data_train, dummies_cabin, dummies_embarked, dummies_sex], axis=1)
    data_train.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)

    global data_test
    data_test = set_cabin(data_test)
    data_test['Name_lenth'] = data_test.Name.apply(len)
    # print(data_train.Fare.groupby(by=data_train['Pclass']).mean().get([1, 2]))
    # print(data_test[data_test['Fare'].isnull()]['Pclass'])
    # print(data_test.loc[(data_test['Fare'].isnull()), 'Fare'])
    data_test['Fare'].fillna(data_train.Fare.groupby(by=data_train['Pclass']).mean().get([3]).values[0], inplace=True)
    dummies_test_cabin = pd.get_dummies(data_test['Cabin'], prefix='Cabin')
    dummies_test_embarked = pd.get_dummies(data_test['Embarked'], prefix='Embarked')
    dummies_test_sex = pd.get_dummies(data_test['Sex'], prefix='Sex')
    data_test = pd.concat([data_test, dummies_test_cabin, dummies_test_embarked, dummies_test_sex], axis=1)
    data_test.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)

    data_train, data_test = set_missing_age(data_train, data_test)

    data_train, data_test = set_data_standard(data_train, data_test)
    return data_train, data_test


if __name__ == '__main__':
    data_process()