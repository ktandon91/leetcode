w = [1,3,4,5]
v = [1,4,5,7]
c = 7
l = len(w)
def recusive_solution(n, capacity):
    if capacity == 0 or n == 0:
        return 0
    if w[n-1] <= capacity:
        return max(v[n-1]+recusive_solution(n-1, capacity-w[n-1]), recusive_solution(n-1, capacity))
    else:
        return recusive_solution(n-1, capacity)
print(recusive_solution(l, c))
