def solution(sizes):
    answer = 0
    
    for size in sizes:
        size.sort(reverse=True)
    sizes.sort(reverse=True)
    
    return max([size[0] for size in sizes]) * max([size[1] for size in sizes])

if __name__ == "__main__":
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))