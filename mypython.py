#!/usr/bin/env python

import argparse
import os
import os.path as op
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("my_file",
                       type=str, help="Path to the input csv file.")
args = parser.parse_args()

my_file = args.my_file

header_names = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM",
                "AGE", "DIS", "RAD", "TAX", "PTRATIO",
                 "B", "LSTAT", "MEDV"]
data = pd.read_csv(my_file, sep='\s+|,', header=None, names=header_names)
print(data.head())


sns.set(style='whitegrid', context='notebook')
cols = ['LSTAT','INDUS','PTRATIO','RM','MEDV','AGE']

plt.figure(figsize=(15,10))
plt.scatter(data.LSTAT, data.MEDV, color='red', marker="v", label = 'LSTAT')
plt.scatter(data.INDUS, data.MEDV, color='green', marker="s", label = 'INDUS')
plt.scatter(data.PTRATIO, data.MEDV, color='blue', marker="p", label = 'PTRATIO')
plt.scatter(data.RM, data.MEDV, color='yellow', marker="h", label = 'RM')
plt.scatter(data.AGE, data.MEDV, color='black', marker="D", label = 'AGE')


plt.title('Multiple factors that affect housing price')
plt.xlabel("Factors affect housing price")
plt.ylabel("MEDV")
plt.legend()
plt.savefig("Factors.png")
plt.show()


plt.figure(figsize=(10,10))
cm = np.corrcoef(data[cols].values.T)
sns.set(font_scale=1.5)
hm = sns.heatmap(cm,cbar=True,annot=True,square=True,fmt='.2f',annot_kws={'size':15},yticklabels=cols, xticklabels=cols)
plt.savefig("heatmap.png")
plt.show()
