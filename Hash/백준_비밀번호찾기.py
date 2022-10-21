import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n,m = map(int, input().split())
    password_dict = {}
    
    for _ in range(n):
        domain, password = input().strip().split(" ")
        password_dict[domain] = password
        
    for _ in range(m):
        print(password_dict[input().strip()])