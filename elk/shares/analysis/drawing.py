import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('./result2019-09-09.csv')

# df['symbol'] = df['symbol'].astype('object')

# print(df.tail())

# df.info()
#
# print(df.describe())

sns.relplot(x="std_deviation_1y", y="pct_chg", hue="rise", data=df)

sns.relplot(x="std_deviation_6m", y="pct_chg", hue="rise", data=df)

sns.relplot(x="std_deviation_5m", y="pct_chg", hue="rise", data=df)

sns.relplot(x="std_deviation_4m", y="pct_chg", hue="rise", data=df)

sns.relplot(x="std_deviation_3m", y="pct_chg", hue="rise", data=df)

sns.relplot(x="std_deviation_2m", y="pct_chg", hue="rise", data=df)

sns.relplot(x="std_deviation_1m", y="pct_chg", hue="rise", data=df)

sns.relplot(x="std_deviation_1w", y="pct_chg", hue="rise", data=df)

sns.relplot(x="pct_chg_1y", y="pct_chg", hue="rise", data=df.query("-11.0 < pct_chg < 11.0"))

sns.relplot(x="pct_chg_6m", y="pct_chg", hue="rise", data=df.query("-11.0 < pct_chg < 11.0"))

sns.relplot(x="pct_chg_5m", y="pct_chg", hue="rise", data=df.query("-11.0 < pct_chg < 11.0"))

sns.relplot(x="pct_chg_4m", y="pct_chg", hue="rise", data=df.query("-11.0 < pct_chg < 11.0"))

sns.relplot(x="pct_chg_3m", y="pct_chg", hue="rise", data=df.query("-11.0 < pct_chg < 11.0"))

sns.relplot(x="pct_chg_2m", y="pct_chg", hue="rise", data=df.query("-11.0 < pct_chg < 11.0"))

sns.relplot(x="pct_chg_1m", y="pct_chg", hue="rise", data=df.query("-11.0 < pct_chg < 11.0"))

sns.relplot(x="pct_chg_1w", y="pct_chg", hue="rise", data=df.query("-11.0 < pct_chg < 11.0"))


plt.show()