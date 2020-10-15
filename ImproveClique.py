import time
from itertools import combinations
import json
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
def adjacencyToIndex(a):
	MATRIX=[]
	k=-1
	for i in range(len(a)):
		A=[]
		for j in range(len(a[i])):
			if a[i][j]==1:
				A.append(j)
			else:
				A.append(k)
				k=k-1
		MATRIX.append(A)	
	return MATRIX

def convertIntoSet(mat):
	dic={}
	k=0
	for i in mat:
		l=[]		
		for j in i:
			if j>=0:
				l.append(j)
		dic[k]=set(l)
		del(l)		
		k+=1
	return dic

def getClique(G,l,r,size=20):
	key=list(G.keys())
	#l=[i for i in range(0,size)]
	c=combinations(l,r)
	for i in c:
		res=[]
		pos=[]
		b=G[key[i[0]]]
		for j in i[1:]:
			b=b&G[key[j]]
		if b:
			for k in i:
				
				if key[k] in b:
					res.append(True)
					pos.append(key[k])
				else:
					res.append(False)
		if all(res) and res!=[]:
			#print(res)
			#print(b)
			print("Index of cliqued Element of size=",r)
			print(pos)
			del(res)
			del(pos)		
			return True  #remove return and it prints all clique of size r
			
def getMatrix(row):
	mat=[[1 if i %2==0 else 0 for i in range(0,row)]if j%2==0 else [1 if i %2==1 else 0 for i in range(0,row)] for j in range(0,row)]
	return mat

def getRowSum(matrix):
	row_sum=[]
	for i in matrix:
		row_sum.append(sum(i))
	countSum={}
	print(row_sum)
	for i in row_sum[:]:
		pos=[]
		if i not in countSum:
			for k in range(0,len(row_sum)):
				if row_sum[k]==i:
					pos.append(k)
			countSum[i]=(len(pos),set(pos))
		del(pos)
	print(countSum)
	indexofclique={}
	for i in countSum:
		b=countSum[i][1]
		#print(b)
		for j in countSum:
			if j>=i:
				b=b|countSum[j][1]
		print(b)		
		if len(b)>=i:
			indexofclique[i]=b
		del(b)	
	return indexofclique,list(indexofclique.keys())		


mat1=[
[1,1,0,0,1,0,1,1,0,1],
[1,1,1,1,0,1,1,1,0,1],
[0,1,1,1,1,0,1,1,1,0],
[0,1,1,1,0,0,0,0,0,0],
[1,0,1,0,1,1,0,1,0,0],
[0,1,0,0,1,1,1,1,1,0],
[1,1,1,0,0,1,1,1,1,1],
[1,1,1,0,1,1,1,1,0,1],
[0,0,1,0,0,1,1,0,1,1],
[1,1,0,0,0,0,1,1,1,1],
]



mat2=[
[1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,1,0,0,1,1],
[1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,1,0,0,1,1],
[0,0,1,1,1,0,1,1,0,0,1,0,1,0,1,1,0,0,1,1],
[0,0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,1,1],
[1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,0,0,1,1],
[0,0,0,1,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0],
[0,0,1,0,0,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0],
[1,1,1,0,1,0,1,1,0,1,1,1,1,1,1,1,0,0,1,1],
[0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,1,0,0,1,1],
[1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1],
[1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,1,1],
[1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,1,1],
[1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,1,1,0,1,1],
[1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,1,1],
[1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,0,0,1,1],
[0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0],
[1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,1,1],
[1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,0,0,1,1]
]
'''mat2[5][8]=1
mat2[5][9]=0
mat2[5][10]=1
mat2[14][6]=1
'''
mat3=[
[1,1,1,1,0],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,0],
[0,1,1,0,1]
]
mat4=[
[1,1,1,1,1],
[1,1,0,1,1],
[1,0,1,0,1],
[1,1,0,1,1],
[1,1,1,1,1]
]
mat5=[
[1,1,1,0,1,1,0,0,1,0],
[1,1,1,0,1,1,0,1,1,0],
[1,1,1,1,1,1,0,0,1,1],
[0,0,1,1,0,0,1,0,0,0],
[1,1,1,0,1,1,0,0,1,0],
[1,1,1,0,1,1,1,0,1,0],
[0,0,0,1,0,1,1,1,0,1],
[0,1,0,0,0,0,1,1,0,0],
[1,1,1,0,1,1,0,0,1,1],
[0,0,1,0,0,0,1,1,0,1]
]
start=time.time()
mat=getMatrix(30)
dic,key=getRowSum(mat)
printSetMatrix(dic)
#print("Adjacency Matrix")
#printMatrix(mat)
indexMat=adjacencyToIndex(mat)
#print("Index Matrix")
#printMatrix(indexMat)
#print("Set Matrix")
d=convertIntoSet(indexMat)
#printSetMatrix(d)
print("********************************************")
#for i in range(len(mat),0,-1):
#	if getClique(d,i,len(mat)):
#		break #pass use pass and it will print all clique start from maximum clique to size 1

for i in dic:
	if getClique(d,dic[i],i):
		break

end=time.time()
print(end-start)
