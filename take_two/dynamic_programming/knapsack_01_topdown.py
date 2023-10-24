w = [1,3,4,5]
v = [1,4,5,7]
cap = 7
l = len(w)
s = [[0 for _ in range(cap+1)] for _ in range (l+1)]


for i in range(1,l+1):
    for j in range(1, cap+1):
        if w[i-1] <= j:
            s[i][j] = max(v[i-1]+s[i-1][j-w[i-1]], s[i-1][j])
        else:
            s[i][j] = s[i-1][j]


print(s[-1][-1])
