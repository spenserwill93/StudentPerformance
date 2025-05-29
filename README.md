# Student Academic Performance Clustering


## Project Overview
This project uses K-Means clustering to group students based on their academic performance, specifically their math, reading, and writing scores. The goal is to identify distinct clusters of students that share similar academic characteristics, which can help in targeting support for at-risk students or tailoring educational interventions.

## Dataset Description
The dataset contains anonymized student-level data with the following key features:
student_id, name, gender, age, grade_level
Academic scores: math_score, reading_score, writing_score
Behavioral and demographic features: attendance_rate, parent_education, study_hours, internet_access, lunch_type, extra_activities
final_result indicating overall student outcome
This project focuses primarily on the academic features (math_score, reading_score, writing_score) for clustering.

## Methodology
Data Loading & Inspection
The dataset is loaded and inspected for missing values and data quality.

## Feature Selection & Scaling
Academic scores are selected and standardized using StandardScaler to ensure equal weighting in clustering.

## K-Means Clustering
The elbow method is used to find the optimal number of clusters (k). Clustering is performed with the chosen k which was 2.

## Cluster Analysis
The resulting clusters are summarized by their average academic and behavioral features.

## Visualization
Clusters are visualized using scatter plots of math and reading scores colored by cluster assignment.

## How to Run
Clone or download this repository.

Ensure you have the required libraries installed:
pandas scikit-learn matplotlib seaborn

Place the student_info.csv dataset in the project directory.

Run the script:
python student_clustering.py
View the printed cluster summaries and the cluster visualization plot.

## Key Insights
The data naturally separates into clusters representing groups of students with distinct academic profiles.
These clusters can help identify students who may benefit from additional academic support.
Behavioral features like attendance rate and study hours can be compared across clusters to gain further understanding.




## Author: Spenser Williams

