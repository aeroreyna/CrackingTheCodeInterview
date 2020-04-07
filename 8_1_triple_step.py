def tripple_step_comb(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return tripple_step_comb(n-1) + tripple_step_comb(n-2) + tripple_step_comb(n-3)


def tripple_step_comb_mem(n, mem=[]):
    if len(mem) == 0:
        mem = [0] * n
    if n < 1:
        return 0
    if n == 1:
        return 1
    sum = 0
    for i in range(3):
        if not mem[n-i-1]:
            mem[n-i-1] = tripple_step_comb_mem(n-i-1, mem)
        sum += mem[n-i-1]
    return sum

if __name__ == '__main__':
    n = 28
    for i in range(n+1):
        print(i, tripple_step_comb(i))
    n = 37
    for i in range(n+1):
        print(i, tripple_step_comb_mem(i))
