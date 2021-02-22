# Program to multiply two matrices using nested loops
import random

N = 250

# NxN matrix
# Most time consuming function
@profile
def nxn(N):
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
        #X.append(random.sample(range(1,100),N))
        return X

# Nx(N+1) matrix
# Most time consuming function
@profile
def nxn1(N):
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
        #Y.append(random.sample(range(1,100),N+1))
        return Y

# result is Nx(N+1), it is only the shape of the resulting matrix
@profile
def result(N):
    result = []
    for i in range(N):
        result.append([0] * (N+1))
        return result

# iterate through rows of X
@profile
def eval(X,Y):
    res = result(N)
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                res[i][j] += X[i][k] * Y[k][j]
    return res

@profile
def print_r(result):
    for r in result:
        print(r)

X = nxn(N)
Y = nxn1(N)
result(N)
res = eval(X,Y)
print_r(res)
