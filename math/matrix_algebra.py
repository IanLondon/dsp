# Matrix Algebra

# Results:
# 1.1) A is a 2 x 3 matrix
# 1.2) B is a 2 x 2 matrix
# 1.3) C is a 3 x 2 matrix
# 1.4) D is a 2 x 3 matrix
# 1.5) u is a 1 x 4 matrix
# 1.6) w is a 4 x 1 matrix
# 2.1) [[ 9  7 -4  9]]
# 2.2) [[ 3 -3 -2  1]]
# 2.3) [[ 36  12 -18  30]]
# 2.4) [[51]]
# 2.6) 8.60232526704
# 3.1) not defined
# 3.2)
# [[-4 -7 -3]
#  [ 3  6  4]]
# 3.3)
# [[14  3  3]
#  [ 2  7  9]]
# 3.4)
# [[-1 -5 -1]
#  [ 2  7  4]]
# 3.5) not defined
# 3.6) not defined
# 3.7)
# [[ 5 -6]
#  [ 9 -8]
#  [ 6 -6]]
# 3.8)
# [[ 1 -4]
#  [ 0  1]]
# 3.9)
# [[14 28]
#  [28 69]]
# 3.10)
# [[10 -4  0]
#  [-4  8  8]
#  [ 0  8 10]]


import numpy as np

A = np.matrix('1 2 3; 2 7 4')
B = np.matrix('1 -1; 0 1')
C = np.matrix('5 -1; 9 1; 6 0')
D = np.matrix('3 -2 -1; 1 2 3')
u = np.matrix([6, 2, -3, 5])
v = np.matrix([3, 5, -1, 4])
w = np.matrix('1; 8; 0; 5')
alpha = 6

# Part 1.
for matrix, name, problem_no in zip((A,B,C,D,u,w), ('A','B','C','D','u','w'), range(1,7)):
    print "1.{problem_no}) {name} is a {shape[0]} x {shape[1]} matrix".format(name=name,
        shape=matrix.shape, problem_no=problem_no)

# Part 2.
print '2.1)', u + v
print '2.2)', u - v
print '2.3)', alpha * u
print '2.4)', np.dot(u,v.T) # must transpose v b/c it's a matrix not a vector
print '2.6)', np.linalg.norm(u)

# Part 3.
try:
    print '3.1)', A + C
except ValueError:
    print 'not defined'
print '3.2)\n', A - C.T
print '3.3)\n', C.T + 3*D
print '3.4)\n', np.dot(B,A)
try:
    print '3.5)', np.dot(B,A.T)
except ValueError:
    print 'not defined'

# Optional section.
try:
    print '3.6)', np.dot(B,C)
except ValueError:
    print 'not defined'
print '3.7)\n', np.dot(C,B)
print '3.8)\n', B**4
print '3.9)\n', np.dot(A,A.T)
print '3.10)\n', np.dot(D.T,D)
