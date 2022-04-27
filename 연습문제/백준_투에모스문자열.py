def recursive_solution(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    if not num % 2:
        return recursive_solution(num//2)
    else:
        return 1 - recursive_solution(num//2)
        
if __name__ == "__main__":
    k = int(input())

    print(str(recursive_solution(k-1)))