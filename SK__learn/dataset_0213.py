
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.base import BaseEstimator
iris = datasets.load_iris()
data = iris.data
print (data.shape)

digits = datasets.load_digits()
print (digits.images.shape)

plt.imshow(digits.images[-1], cmap=plt.cm.gray_r)
# plt.show()
# To use this dataset with the scikit, we transform each 8x8 image into a feature vector of length 64
data = digits.images.reshape((digits.images.shape[0], -1))
print (data)
BaseEstimator.fit(data)
estimator = BaseEstimator(param1=1, param2=2)
estimator.param1