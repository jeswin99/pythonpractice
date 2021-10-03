

def lps(seq, i, j, dp):
     
    # Base Case 1: If there is
    # only 1 character
    if (i == j):
        return 1
 
    # Base Case 2: If there are only 2
    # characters and both are same
    if (seq[i] == seq[j] and i + 1 == j):
        return 2
     
    # If the first and last characters match
    if (seq[i] == seq[j]):

        dp[i][j] = lps(seq, i + 1, j - 1, dp) + 2
        return dp[i][j]
    # If the first and last characters
    # do not match
    else:
        dp[i][j] = max(lps(seq, i, j - 1, dp),
                lps(seq, i + 1, j, dp))
        return dp[i][j]
 
# Driver Code
if __name__ == '__main__':
    seq = "GEEKSFORGEEKS"
    n = len(seq)
    dp=[[-1 for i in range(n+1)] for j in range(n+1)]
    print("The length of the LPS is",lps(seq, 0, n - 1, dp))
