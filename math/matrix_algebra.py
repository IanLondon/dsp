# Matrix Algebra

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
