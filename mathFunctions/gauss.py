def array_fill(i, n, v):
    a = [v for element in range(i,n)]
    return a

def gauss(A, x):
    isSolveable = True
    for i in range(0, len(A)):
        A[i].append(x[i])
    n = len(A)

    for i in range(0,n):
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i,n+1): 
                if i==j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    x = array_fill(0, n, 0)
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]

    
    return {
        'isSolveable': isSolveable,
        'x': x
        }