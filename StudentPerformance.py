import pandas as pd

#Load in dataset
df = pd.read_csv("student_info.csv")

#Get info about 
print(df.head())
print(df.info())

#Check for missing values
print("Missing values per column:\n", df.isnull().sum())

#Select academic columns
academic_data = df[['math_score','reading_score', 'writing_score']]

#Check basic stats
print(academic_data.describe())

from sklearn.preprocessing import StandardScaler

#initialize the scaler
scaler = StandardScaler()

#Transform the data
scaled_data = scaler.fit_transform(academic_data)

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns

#Empty list to store the inertia for each value of k
inertia = []
#Trying 1-10 clusters
k_range = range(1,11)

#Try k = 1-10
for k in k_range:
    kmeans = KMeans(n_clusters = k, random_state = 42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

#Plot the figure
plt.figure(figsize=(8,5))
plt.plot(k_range, inertia)
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.show()

#K = 2
kmeans = KMeans(n_clusters = 2, random_state = 42)
kmeans.fit(scaled_data)

#Add cluster labels to original data
df['performance_cluster'] = kmeans.labels_

#Compare academic features by cluster
cluster_summary = df.groupby('performance_cluster')[['math_score', 'reading_score', 'writing_score', 'attendance_rate', 'study_hours']].mean()
print(cluster_summary)

#Set grid style
sns.set(style = "whitegrid")

#plot the clusters
plt.figure(figsize=(8,5))
sns.scatterplot(
    x ='math_score',
    y ='reading_score',
    hue = 'performance_cluster',
    palette = 'Set1',
    data = df
)

plt.title('Student Clusters by Math and Reading Scores')
plt.xlabel('Math Score')
plt.ylabel('Reading Score')
plt.show()



