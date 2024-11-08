import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.decomposition import PCA
%matplotlib inline

iris=pd.read_csv("https://media.githubusercontent.com/media/neurospin/pystatsml/refs/heads/master/datasets/iris.csv")

iris.head()

iris.info()

iris.describe()

sns.heatmap(iris.drop(['species'], axis=1).corr(), annot=True, cmap="coolwarm")
plt.show()

pca = PCA()
x_new1 = pca.fit_transform(iris.drop(['species'], axis=1))
x_new1[:5]

explained_variance=pca.explained_variance_ratio_
explained_variance

plt.figure(figsize=(10,6))
plt.bar(range(4), explained_variance, alpha=0.5, align='center', label="Individual Explained Variance", color="darkred")
plt.ylabel("Explained Variance Ratio")
plt.xlabel("Principal Component")
plt.legend(loc="best")
plt.tight_layout()
plt.show()


pca = PCA(n_components=3)
x_new = pca.fit_transform(iris.drop(['species'], axis=1))
x_new[:5]

categ_num={"variety": {"setosa":0,"versicolor":1,"virginica":2}}
iris1 = iris.replace(categ_num)
columns= list(iris.columns[:4])

fig, axes = plt.subplots(3, 4, figsize=(15, 10)) 
for i in range(3):  # Loop over 3 PCA components
    for j in range(4):  # Loop over 4 original features
        axes[i, j].scatter(x_new[:, i], iris[columns[j]], c="r")
        axes[i, j].set_xlabel(f'PC {i+1}')
        axes[i, j].set_ylabel(columns[j])
plt.tight_layout()
plt.show()
