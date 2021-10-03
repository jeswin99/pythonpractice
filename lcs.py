
import snoop
#@snoop
def lcs(X, Y, m, n,dp):
 
    if m == 0 or n == 0:
        return 0
    if dp[m][n] != -1:
        print(m,n)
        return dp[m][n]

    elif X[m-1] == Y[n-1]:
        dp[m][n] = 1 + lcs(X, Y, m-1, n-1,dp)
        return dp[m][n]
    else:
        dp[m][n] = max(lcs(X, Y, m, n-1,dp), lcs(X, Y, m-1, n,dp))
        return dp[m][n]
 
 
# Driver program to test the above function
X = "AXYT"
Y = "AYZX"
dp=[[-1 for i in range(len(Y)+1)]for j in range(len(X)+1)]
print(lcs(X , Y, len(X), len(Y),dp))
