def printBoundary(a, m, n): 
    sum = 0
    for i in range(m): 
        for j in range(n): 
            if (i == 0): 
                sum += a[i][j] 
            elif (i == m-1): 
                sum += a[i][j] 
            elif (j == 0): 
                sum += a[i][j] 
            elif (j == n-1): 
                sum += a[i][j] 
    return sum
          
# Driver code 
a = [ [ 1, 2, 3 ], [ 1, 5, 1 ], [ 1, 2, 1 ]] 
res = printBoundary(a, 3, 3)
print res
