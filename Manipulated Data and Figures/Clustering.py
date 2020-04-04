import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Import Dataset
col_list = ["z Employment Rate", "z Individual Income Normalized", "z Fraction Married", "z Incarceration Rate", "z Number of Children Normalized"]
data = pd.read_csv("Project3.csv", usecols=col_list)
print("Input data and shape")
print(data.shape)
data.head()

#Obtain values
var1 = col_list[0]
var2 = col_list[4]
f1 = data[var1].values
f2 = data[var2].values
X = np.array(list(zip(f2,f1)))

km = KMeans(
    n_clusters=4, init='random',
    n_init=10, max_iter=300,
    tol=1e-04, random_state=0
)
y_km = km.fit_predict(X)

# plot the 3 clusters
plt.scatter(
    X[y_km == 0, 0], X[y_km == 0, 1],
    s=50, c='lightgreen',
    marker='o', edgecolor='black',
)

plt.scatter(
    X[y_km == 1, 0], X[y_km == 1, 1],
    s=50, c='orange',
    marker='o', edgecolor='black',
    label='cluster 1'
)

plt.scatter(
    X[y_km == 2, 0], X[y_km == 2, 1],
    s=50, c='lightblue',
    marker='o', edgecolor='black',
    label='cluster 2'
)

plt.scatter(
    X[y_km == 3, 0], X[y_km == 3, 1],
    s=50, c='lightgreen',
    marker='o', edgecolor='black',
    label='cluster 3'
)

# plot the centroids
plt.scatter(
    km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
    s=250, marker='*',
    c='red', edgecolor='black',
    label='centroids'
)
plt.legend(scatterpoints=1)
plt.xlabel(var1)
plt.ylabel(var2)
plt.title("Los Angeles Social Mobility Clustering")
plt.ylim(-3,max(f1)+1)
plt.savefig(var1+var2+'.png')
plt.show()