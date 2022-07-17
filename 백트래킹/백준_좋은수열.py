import sys
input = sys.stdin.readline

def check(num):
    length = len(num)
    for idx in range(1, length//2 + 1):
        if num[-idx:] == num[-(idx*2):-idx]:
            return False
    else:
        return True
    
def recursive(num):
    if len(num) == n:
        print(num)
        sys.exit()
    
    for i in '123':
        if check(num + i):
            recursive(num+i)
    
        
if __name__ == "__main__":
    n = int(input())
    
    recursive('')