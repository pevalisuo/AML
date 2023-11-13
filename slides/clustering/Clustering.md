---
title: Clustering
theme: moon
revealOptions:
  
---

# Clustering

----

### Topics

   - Unsupervised learning
   - What is clustering
   - kMeans
   - Expectation maximization
   - Gaussian Mixture model  

----

## Cluster

> A group of the same or similar elements gathered or occurring closely together.

----

Fruits are placed in 2D coordinates based on their color and surface roughness


<div id="left">


![Apples and oranges](kuvat/ApplesAndOrangesWhite.svg) 


</div>

<div id="right">

- The similarity of objects can be measured with a distance metric <!-- .element class="fragment" -->
  - E.g. Euclidian distance $D_e=\sqrt{\Delta H^2 + \Delta S^2}$
- A Cluster is a group of objects close to each other separated with a sparse region <!-- .element class="fragment" -->

</div> 


----


### Clustering

A clustering algorithm clusters the data in the design matrix $X=[H^T, S^T]$ into cluster memberships, $c_i$.

`$$
   \begin{bmatrix}
   c_1 \\
   c_2 \\
   \vdots \\
   c_n
   \end{bmatrix}
   = f 
   \left( \begin{bmatrix}
     x_{11} & x_{12} & x_{13} & \dots  & x_{1p} \\
     x_{21} & x_{22} & x_{23} & \dots  & x_{2p} \\
     \vdots & \vdots & \vdots & \ddots & \vdots \\
     x_{n1} & x_{n2} & x_{n3} & \dots  & x_{np}
   \end{bmatrix} \right)
$$`


----






----

### How to do it in Python

```Python [1|4|5|8-11|12]
from sklearn.decomposition import PCA

# Perform PCA decomposition
pca=PCA(n_components=2)
Xp=pca.fit_transform(Xs)

# Plot the original data and transformed data side by side
fig, (ax1, ax2)=plt.subplots(nrows=1, ncols=2, figsize=(12,5))
plotData(Xs, ax1, xlab='X1', ylab='X2', title='Original data')
plotData(Xp, ax2, xlab='PC 1', ylab='PC 2', title='PCA', 
    noline=True)
pca.explained_variance_ratio_

```

----

### The end




<style>
#bright {
  color: deeppink;
}
#left {
    margin: 10px 0 15px 20px;
    text-align: center;
    float: left;
    z-index:-10;
    width:48%;
    font-size: 0.85em;
    line-height: 1.5;
}
#right {
    margin: 10px 0 15px 0;
    float: right;
    text-align: center;
    z-index:-10;
    width:48%;
    font-size: 0.85em;
    line-height: 1.5;
}

#dark_back {
  background-color: rgba(0, 0, 0, 0.9);
  color: #000;
  padding: 20px;
}

#white_back {
  background-color: rgba(1, 1, 1, 0.9);
  color: black;
  padding: 20px;
}
</style>
<link rel="stylesheet" href="plugin/highlight/monokai.css">
<link rel="stylesheet" href="plugin/chalkboard/style.css">
<!-- .slide: data-background="figures/uwrocks.png" -->
