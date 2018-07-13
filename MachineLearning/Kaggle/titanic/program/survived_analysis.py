import pandas as pd
import matplotlib.pyplot as plt
import os
data = pd.read_csv(os.path.abspath(os.path.dirname(os.getcwd())) + '/train.csv' )
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure()
fig.set(facecolor='gray')