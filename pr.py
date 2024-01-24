import numpy as np
A = np.array([[4, 9, 9],
              [9, 1, 6],
              [9, 2, 3]])

B = np.array([[2, 2],
              [5, 7],
              [4, 4]])

print(np.matmul(A,B)) #[[ 89 107]
                      # [ 47  49]
                      # [ 40  44]]
print("or")
print(A@B) #[[ 89 107]
           # [ 47  49]
           # [ 40  44]]
print(np.dot(B,A))