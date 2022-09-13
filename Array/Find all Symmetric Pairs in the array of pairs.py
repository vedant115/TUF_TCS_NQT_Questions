arr = [(1,2),(2,1),(3,4),(4,5),(5,4)]
arr = [(1,5),(2,3),(4,2),(5,1),(2,4)]

visited = []
for pair in arr:
    if set(pair) in visited:
        print(pair, end=" ")
    visited.append(set(pair))
