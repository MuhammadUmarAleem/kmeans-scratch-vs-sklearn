from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Set plot size and style
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

# Importing the dataset
data = pd.read_csv('xclara.csv')
print("Input Data and Shape")
print(data.shape)
data.head()

# Getting the values and plotting it
f1 = data['V1'].values
f2 = data['V2'].values
X = np.array(list(zip(f1, f2)))

# Plot the raw data
plt.scatter(f1, f2, c='black', s=7)
plt.title("Raw Data Points")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# Euclidean Distance Calculator
def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)

# Number of clusters
k = 3

# X coordinates of random centroids
C_x = np.random.randint(0, np.max(X) - 20, size=k)
# Y coordinates of random centroids
C_y = np.random.randint(0, np.max(X) - 20, size=k)
C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
print("Initial Centroids")
print(C)

# Plotting along with the initial centroids
plt.scatter(f1, f2, c='#050505', s=7)
plt.scatter(C_x, C_y, marker='*', s=200, c='g')
plt.title("Data Points with Initial Centroids")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

# To store the value of centroids when it updates
C_old = np.zeros(C.shape)

# Cluster Labels (0, 1, 2)
clusters = np.zeros(len(X))

# Error function - Distance between new centroids and old centroids
error = dist(C, C_old, None)

# Loop will run till the error becomes zero
while error != 0:
    # Assigning each value to its closest cluster
    for i in range(len(X)):
        distances = dist(X[i], C)
        cluster = np.argmin(distances)
        clusters[i] = cluster

    # Storing the old centroid values
    C_old = deepcopy(C)

    # Finding the new centroids by taking the average value
    for i in range(k):
        points = [X[j] for j in range(len(X)) if clusters[j] == i]
        if len(points) > 0:  # Avoid division by zero
            C[i] = np.mean(points, axis=0)

    error = dist(C, C_old, None)

# Visualize the final clusters and centroids from scratch
colors = ['r', 'g', 'b', 'y', 'c', 'm']
fig, ax = plt.subplots()
for i in range(k):
    points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
    ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i], label=f'Cluster {i + 1}')
ax.scatter(C[:, 0], C[:, 1], marker='*', s=200, c='black', label='Centroids')
plt.title("Clusters and Centroids (From Scratch)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()

'''
==========================================================
scikit-learn
==========================================================
'''
from sklearn.cluster import KMeans

# Number of clusters
kmeans = KMeans(n_clusters=3)

# Fitting the input data
kmeans = kmeans.fit(X)

# Getting the cluster labels
labels = kmeans.predict(X)

# Centroid values
centroids = kmeans.cluster_centers_

# Comparing with scikit-learn centroids
print("Centroid values")
print("Scratch")
print(C)  # From Scratch
print("sklearn")
print(centroids)  # From sci-kit learn

# Visualize the final clusters and centroids from Scikit-learn
fig, ax = plt.subplots()
for i in range(k):
    points = np.array([X[j] for j in range(len(X)) if labels[j] == i])
    ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i], label=f'Cluster {i + 1}')
ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='black', label='Centroids')
plt.title("Clusters and Centroids (Scikit-learn)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()