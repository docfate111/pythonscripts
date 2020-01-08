import math
def vector_add(v, w):
	return [v_i+w_i for v_i, w_i in zip(v, w)]
def vector_sub(v, w):
	return [v_i-w_i for v_i, w_i in zip(v, w)]
def vector_sum(vectors):
	result=vectors[0]
	for vector in vectors[1:]:
		result=vector_add(result, vector)
	return result
def scalar_multiply(c, v):
	return [c*v_i for v_i in v]
def vector_mean(vectors):
	n=len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))
def dot(v, w):
	return sum(v_i*w_i for v_i, w_i in zip(v, w))
def sum_of_squares(v):
	return dot(v, v)
def mag(v):
	return math.sqrt(sum_of_squares(v))
def sqd_dist(v, w):
#distance between v and w squared
	return math.sqrt(sqd_dist(v, w))
def dist(v, w):
	return mag(vector_sub(v, w))
A=[[1, 2], [3, 4], [5, 6]] #matrix
def shape(m):
	num_rows=len(m)
	num_cols=len(m[0]) if m else 0 #num of elements in 1st row
	return num_rows, num_cols
def get_row(m, i):
	return m[i]
def get_col(m, j):
	return [A_i[j] for A_i in A]
def make_matrix(num_rows, num_cols, entry_fn): #make matrix given a function
	return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]
def is_diagonal(i, j):
	return 1 if i==j else 0
def identitymatrix(i, j):
	return make_matrix(i, j, is_diagonal)
