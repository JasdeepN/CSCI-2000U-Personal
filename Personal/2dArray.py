import numpy as np
x = np.array([[1,2,3], [4,5,6], [7,8,9]])
print (x)
m = x.flatten()
q = x.flatten()
print(m)

print(np.concatenate((q, m)))

print('lets slice some shit')

print(x[0:,0:2]) 

y = np.zeros((3,3))
print(y)

np.random.seed(213123)
print(np.random.rand(5,2))

z = np.array(range(10), float)
z = z.reshape(5,2)
print(z.tolist())

print(np.arange(0,7,3, dtype=int))