# K-Means Clustering from Scratch and Scikit-Learn

## Overview
This repository contains implementations of the K-Means clustering algorithm both from scratch and using Scikit-Learn. The code demonstrates how to perform clustering on a dataset (`xclara.csv`) and visualize the results in both 2D and 3D.

## Files
- **`kmeans-from-scratch-and-sklearn.py`**: Implements K-Means clustering from scratch and compares the results with Scikit-Learn.
- **`kmeans-sklearn.py`**: Implements K-Means clustering in 3D using Scikit-Learn.
- **`xclara.csv`**: The dataset used for clustering.

## Dependencies
Make sure you have the following libraries installed:
```bash
pip install numpy pandas matplotlib scikit-learn
```

## Dataset
The dataset (`xclara.csv`) consists of two features (`V1`, `V2`), which represent data points to be clustered. Example data:
```
V1,V2
2.072345,-3.241693
17.93671,15.78481
1.083576,7.319176
11.12067,14.40678
23.71155,2.557729
```

## Running the Scripts
### 1. K-Means Clustering (From Scratch and Scikit-Learn)
Run the script to execute K-Means from scratch and compare it with Scikit-Learn:
```bash
python kmeans-from-scratch-and-sklearn.py
```
#### Outputs:
- Visualization of the raw dataset.
- Initial random centroids.
- Clusters and final centroids (from scratch and Scikit-Learn).

### 2. K-Means Clustering in 3D (Scikit-Learn)
Run the script to visualize clustering in 3D:
```bash
python kmeans-sklearn.py
```
#### Outputs:
- 3D scatter plot of data points.
- Clustered points with computed centroids.

## Results
The clustering results are visualized in 2D and 3D, showing how K-Means groups data into clusters. The centroids calculated from scratch and using Scikit-Learn are compared for accuracy.
