from Matrix import printMatrix
def getMatrix(row):
	mat=[[1 if i %2==0 else 0 for i in range(0,row)]if j%2==0 else [1 if i %2==1 else 0 for i in range(0,row)] for j in range(0,row)]
	return mat

printMatrix(getMatrix(10))
