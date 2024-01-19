import numpy as np
A = np.array([[4, -3, 1],
              [2, 1, 3],
              [-1, 2, -5]], dtype= np.dtype(float))

b = np.array([-10, 0, 17], dtype=np.dtype(float))

print(A) # [[ 4. -3.  1.]
         # [ 2.  1.  3.]
         # [-1.  2. -5.]]
print(f"Shape of A:{np.shape(A)}") # Shape of A: (3, 3)

print("")
print("======Solving using Matrices======")
x=np.linalg.solve(A, b)
print(f"Solution: {x}") # Solution: [ 1.  4. -2.]

print("")

d=np.linalg.det(A)
print(f"Determinant of matrix A: {d:.2f}") # Determinant of matrix A: -60.00

print("")

print("======Solving using Row Reductio======")
A_system = np.hstack((A, b.reshape((3, 1))))
print(A_system) # [[  4.  -3.   1. -10.]
                #  [  2.   1.   3.   0.]
                #  [ -1.   2.  -5.  17.]]