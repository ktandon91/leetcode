w = [1,3,4,5]
v = [1,4,5,7]
c = 7
l = len(w)
s = [[-1 for col in range(c+1)] for row in range (l+1)]
def recusive_solution(n, capacity):
    if s[n][capacity] != -1:
        return s[n][capacity]
    if capacity == 0 or n == 0:
        return 0
    if w[n-1] <= capacity:
        s[n][capacity] = max(v[n-1]+recusive_solution(n-1, capacity-w[n-1]), recusive_solution(n-1, capacity))
    else:
        s[n][capacity] = recusive_solution(n-1, capacity)
    return s[n][capacity]
recusive_solution(l, c)

print(s)
print(s[-1][-1])
