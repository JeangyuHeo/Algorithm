import sys

if __name__ == "__main__":
    alpha_to_num = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6}
    tour = [input() for _ in range(36)]
    if len(tour) != len(set(tour)):
        print("Invalid")
    
    else:
        tour.append(tour[0])

        for i in range(1, 37):
            x = abs(alpha_to_num[tour[i][0]] - alpha_to_num[tour[i-1][0]])
            y = abs(int(tour[i][1]) - int(tour[i-1][1]))

            if not ((x == 1 and y== 2) or (x == 2 and y == 1)):
                print("Invalid")
                break
        else:
            print("Valid")