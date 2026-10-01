"""import numpy as np
n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
print(type(n))"""

#for dimensional...........
"""import numpy as np
a = np.array([1,2,3,4])
print(a.ndim)"""


import numpy as np
#array slicing................
"""a=np.array([[1,2,3],[4,5,6]])
print(a[0,1])
print(a[1:4])
print(a[:1])
print(a[5:])


#for shape and reshape.............
print(a.shape)
print(a.reshape(3,2))



#for concatenate.............
n1=np.array([1,2,3])
n2=np.array([4,5,6])
n3=np.concatenate((n1,n2))
print(n3)
print(np.array_split(n3,3))


#zeros and ones...................
print(np.zeros((2,3)))
print(np.ones((2,3)))"""


#searching..........
"""a=np.array([1,2,3,4,5,6,7,8,9])
p=np.where(a==5)
print(p)"""

#sorting............
"""a=np.array([7,4,6,8,2,3,1])
print (np.sort(a))"""


#sorting string array..........
"""n=np.array('hi','java','python','app')
print(np.sort(n))"""


#looping...........
"""n=np.array([[1,2,3],[4,5,6],[7,8,9]])
for x in n:
    print(x)"""


#arthimetic operators
n1=np.array([1,2,3,4])
n2=np.array([2,4,5,6])
print(np.add(n1,n2))
print(np.subtract(n1,n2))
print(np.multiply(n1,n2))
print(np.divide(n1,n2))

#for dimensional...........
"""import numpy as np
a = np.array([1,2,3,4])
print(a.ndim)"""
