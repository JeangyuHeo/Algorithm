def solution(m, n, startX, startY, balls):
    answer = []
    
    for ball_x, ball_y in balls:
        min_dist = 1e9
        for x, y in ((-ball_x, ball_y), (ball_x, -ball_y), (2 * m - ball_x, ball_y), (ball_x, 2 * n - ball_y)):
            if not any([all([startX == ball_x, startY>ball_y>y or startY<ball_y<y]), all([startY == ball_y, startX>ball_x>x or startX<ball_x<x])]):
                min_dist = min(min_dist, (startX-x) ** 2 + (startY-y) ** 2)
    
        answer.append(min_dist)
    return answer

if __name__ == "__main__":
    print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]), [52, 37, 116])