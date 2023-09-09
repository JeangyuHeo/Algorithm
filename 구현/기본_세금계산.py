# 이 부분을 개선하면 됨
def calc_tax(num, size):
    start, end = 0, size
    
    while start < end:
        mid = (start + end) // 2
        if num >= rate[mid][0]:
            start = mid+1
        else:
            end = mid
    
    return num * (rate[end-1][2] / 100)

def solution(income, tax, rate):
    size = len(rate)
    x, y = 0, income

    while x <= y:
        cur_tax = calc_tax(x, size) + calc_tax(y, size)
        
        if cur_tax == tax:
            return [x, y]
        
        x += 1000
        y -= 1000
    
if __name__ == "__main__":
    income, tax = 1000000, 97000
    rate = [[0, 300000, 5], [300000, 700000, 7], [700000, 1000001, 10]]
    result = [60000, 940000]
    
    print(solution(income, tax, rate))