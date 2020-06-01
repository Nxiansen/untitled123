import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

plt.figure()

n_samples = 1500
random_state = 170
X, y = make_blobs(n_samples=n_samples, random_state=random_state)
data = pd.DataFrame(X)
# correct number of clusters
estimator = KMeans(n_clusters=3, random_state=random_state)
y_pred = estimator.fit_predict(X)
xy = estimator.cluster_centers_
data['y']=estimator.labels_
data.to_csv('sss.csv')
print(data)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.plot(xy[:, 0], xy[:, 1], 'r^')
plt.title("Correct Number of Blobs")
plt.show()