import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# 读取数据
data = pd.read_csv('kmeans_data.csv')
X = data[['x', 'y']].values
# K-means聚类（k=4）
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_
centers = kmeans.cluster_centers_
# 可视化
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.6)
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200)
plt.xlabel('x')
plt.ylabel('y')
plt.title('K-means Clustering with k=4')
plt.show()
