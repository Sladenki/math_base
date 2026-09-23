import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])
print("Матрица A:\n", A)

A_T = A.T
print("\nТранспонированная матрица A^T:\n", A_T)
print("Размер A: {}. Размер A^T: {}".format(A.shape, A_T.shape))
