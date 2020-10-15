def printMatrix(matrix):
	for i in matrix:
		print(i)
def printSetMatrix(matrix):
	for i in matrix:
		print(i,":",matrix[i])
	
def isTranspose(mat):
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			if mat[i][j]!=mat[j][i]:
				return False
	return True

