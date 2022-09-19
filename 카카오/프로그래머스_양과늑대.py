def dfs(info, edges, num_sheep, num_wolf):
    if num_sheep > num_wolf:
        global answer
        answer.append(num_sheep)
    else:
        return

    global visited
    for parent, child in edges:
        if not visited[child] and visited[parent]:
            visited[child] = True
            dfs(info, edges, num_sheep+(info[child]==0), num_wolf+(info[child]==1))
            visited[child] = False

def solution(info, edges):
    global visited, answer
    answer = []
    visited = [False for _ in range(len(info))]
    visited[0] = True

    dfs(info, edges, 1, 0)
    
    return max(answer)

if __name__ == "__main__":
    print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
    print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))