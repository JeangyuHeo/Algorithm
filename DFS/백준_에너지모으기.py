
def dfs(tmp_energy, total):
    length = len(tmp_energy)
    
    if length == 2:
        global answer
        answer = max(answer, total)
        return
    
    for i in range(1, length-1):
        dfs(tmp_energy[:i]+tmp_energy[i+1:], total + tmp_energy[i-1] * tmp_energy[i+1])

if __name__ == "__main__":
    answer = -1
    n = int(input())
    energy = list(map(int, input().split()))
    
    dfs(energy, 0)
    
    print(answer)