# Topological Sort Algorithm


def topological_sort(graph):
    order = []
    d_sum = {}  # dependencies sum
    for n in graph:
        d_sum[n] = 0
    for n in graph:
        for d in graph[n]:
            d_sum[d] += 1
    last_size = 0
    while len(d_sum) and last_size != len(d_sum):
        last_size = len(d_sum)
        temp = []
        for g in d_sum:
            if not d_sum[g]:  # Non Dependend Node
                for d in graph[g]:
                    d_sum[d] -= 1
                order.append(g)
                temp.append(g)
        for t in temp:
            del d_sum[t]
    return order


if __name__ == '__main__':
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [["a", "d"], ["f", "b"], ["b", "d"], ["f", "a"], ["d", "c"]]
    graph = {}
    for p in projects:
        graph[p] = []
    for d in dependencies:
        graph[d[0]].append(d[1])
    order = topological_sort(graph)
    print(order)
