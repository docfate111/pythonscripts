import numpy as np 
u=np.array([1, 2, 4, 6])
v=np.array([3, 6, 7, 8])
three_dim=np.array([1, 3, 5], [2, 4, 6], [3, 6, 9])
d=np.shape(three_dim)
#shape is number of entries, common number of arrays
e=np.size(three_dim)
#finds number of total entries: number of entries per array times array
y=u[:2]
m=u.mean()
maximum=u.max()
b=np.cosh(np.pi)
q=np.linspace(-3, 3,num=5)
#creates array between -3 and 3 with 5 evenly spaced values
def vectorAddition(a, b):
    c=a+b
    print(c)
def vectorSubtraction(a, b):
    c=a-b
    print(c)
def crossProduct(a, b):
    c=a*b
    print(c)
def dotProduct(a, b):
    print(np.dot(a, b))
def scalarProduct(a, b):
    c=a*b
    print(c)
def findDeterminant(a):
    print(np.determinant(a))
def findInverse(a):
    print(np.inv(a))
def findNumberOfDimensions(a):
    print(a.ndim)
vectorAddition(u, v)
vectorSubtraction(u, v)
crossProduct(u, v)
dotProduct(u, v)
scalarProduct(3, v)
print(np.sort(u+v)) 