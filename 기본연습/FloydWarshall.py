def Floyd_Warshall():
    
    for t in range(4):
        for i in range(4):
            for j in range(4):
                graph[i][j] = min(graph[i][j], graph[i][t] + graph[t][j])
    
    print(graph)
    return 0

if __name__ =="__main__":
    graph = [
        [0,5,1e9,8],
        [7,0,9,1e9],
        [2,1e9,0,4],
        [1e9,1e9,3,0]
    ]
    
    Floyd_Warshall()