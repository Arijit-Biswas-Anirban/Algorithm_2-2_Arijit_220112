# Lab 20: Longest Common Sub-sequence

def lcs(X, Y):
    m, n = len(X), len(Y)
    
    dp = [["" for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + X[i-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
def main():
    X = input("Enter first String: ")
    Y = input("Enter second String: ")
    
    print(f"Final LCS is: {lcs(X, Y)}")
main()