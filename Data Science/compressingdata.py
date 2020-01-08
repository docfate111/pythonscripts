#pca: principal components analysis-takes a dataset as an input then returns a new dataset of the same shape with 
#uncorrelated data in order of importance
from sklearn.datasets import load_boston
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import numpy as np
boston=load_boston() #getting data example
X, y=boston.data, boston.target
pca=PCA().fit(X)
#informative power of PCA: 
print(' '.join(['%5i'%(k+1) for k in range(13)]))
print(' '.join(['-----']*13))
print(' '.join(["%0.3f" % (variance) for variance in pca.explained_variance_ratio_]))
print(' '.join(["%0.3f" % (variance) for variance in np.cumsum(pca.explained_variance_ratio_)]))

