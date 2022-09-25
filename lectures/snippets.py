import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def fourportdata():
    N=20
    Theta={'R' : 5.0}
    I=np.linspace(0,5,N)
    V=Theta['R']*I + 2*np.random.normal(size=N)
    return (I,V)

from matplotlib.colors import ListedColormap
def plotDB(predictor, X, y, steps=100, figsize=None):
    """Plots the Decision Boundary
        pipe = classification pipeline
        X is the training data used for training the classifier
        steps = number of x and y steps in calculating the boundary
    """
    if figsize:
        fig,ax=plt.subplots(figsize=figsize)
    else:
        fig,ax=plt.subplots()
        
    # Create color map
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    hx = (x_max - x_min)/steps
    hy = (y_max - y_min)/steps
    xx, yy = np.meshgrid(np.arange(x_min, x_max, hx),
                         np.arange(y_min, y_max, hy))
    Z = predictor.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    #plt.figure()
    ax.pcolormesh(xx, yy, Z, cmap=cmap_light, shading='auto')

    # Plot also the training points
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
                edgecolor='k', s=20)
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_title("Decision boundary")
    
# Display the support vectors of support vector machine
def DisplaySupportVectors(X,y,svc):
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
    colors="rgb"
    for i in svc.support_:
        a,b=X[i]
        c=y[i]
        plt.plot(a,b, '%sx' % (colors[c]), ms=8)
        
        
