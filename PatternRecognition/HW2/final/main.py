import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier as KNN


def toPairs(item1, item2, size):
    pairs = []
    for i in range(size):
        pairs.append([item1[i], item2[i]])
    return pairs

# part 1

mean1 = [37, 37]
cov = [[4, 0], [0, 4]]
size1 = 10
class1_x, class1_y = np.random.multivariate_normal(mean=mean1, cov=cov, size=size1).T

mean2 = [39, 39]
class2_x, class2_y = np.random.multivariate_normal(mean=mean2, cov=cov, size=size1).T

y1 = [1]*size1
y2 = [2]*size1

size2 = 1000
class3_x, class3_y = np.random.multivariate_normal(mean=mean2, cov=cov, size=size2).T
class4_x, class4_y = np.random.multivariate_normal(mean=mean2, cov=cov, size=size2).T
# part 2
lda = LinearDiscriminantAnalysis()

lda.fit(toPairs(class1_x, class1_y, size1) + toPairs(class2_x, class2_y, size1), y1 + y2)
test1 = lda.predict(toPairs(class3_x, class3_y, 1000) + toPairs(class4_x, class4_y, size2))

for i in range(len(test1)):
    print(test1[i])
