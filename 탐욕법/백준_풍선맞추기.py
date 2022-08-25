if __name__ == "__main__":
    n = int(input())
    balloons = list(map(int, input().split()))
    arrows = [0 for i in range(max(balloons)+1)]
    answer = 0
    
    for i in range(n):
        if arrows[balloons[i]] == 0:
            answer += 1
            arrows[balloons[i]-1] += 1
        else:
            arrows[balloons[i]] -= 1
            arrows[balloons[i]-1] += 1
            
    print(answer)