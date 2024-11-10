
def lcs(X,Y,i,j):
    if i==len(X) or j==len(Y):
        return 0
    elif X[i]==Y[j]:
        return 1 + lcs(X,Y,i+1,j+1)
    else:
        return max(lcs(X,Y,i+1,j),lcs(X,Y,i,j+1))
    
    
# Example usage
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS:", lcs(X, Y, 0, 0))