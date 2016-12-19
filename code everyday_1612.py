#Make a script both importable and executable, name can be replaced
__name__ =='__main__'
#list
##https://docs.python.org/2/tutorial/datastructures.html
from collections import deque
del popleft
stack and queue in list

#numpy
##https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
b.cumsum()
a[:6:2] = a[0:6:2] = -1000 
np.vstack((a,b)) np.hstack((a,b))
np.column_stack((a,b)) 
##The function column_stack stacks 1D arrays as columns into a 2D array. It is equivalent to vstack only for 1D arrays:
np.hsplit(a,3) np. hsplit((3,4)) np.vsplit(a,3)
np.random.random((3,3))
a = np.arange(12).reshape(3,4) b = a > 4   a[b]
## The dots (...) represent as many colons as needed to produce a complete indexing tuple. 
x[1,2,...] = x[1,2,:,:,:],
