
if __name__ == "__main__":
    answer = 0
    n, m = map(int, input().split())
    s = set([input() for _ in range(n)])
    
    for _ in range(m):
        m_input = input()
        if m_input in s:
            answer += 1
            
    print(answer)