from collections import defaultdict

def check_area(board, x,y):
    base = board[x][y]
    return (base == board[x][y+1]) and (base == board[x+1][y]) and (base == board[x+1][y+1])

def add_dict(break_dict, r, c):
    break_dict[r].add(c)
    break_dict[r].add(c+1)
    break_dict[r+1].add(c)
    break_dict[r+1].add(c+1)
        
def solution(m, n, board):
    answer = 0
    trans_board = [[] for _ in range(n)]

    for c in range(n):
        for r in range(m-1, -1, -1):
            trans_board[c].append(board[r][c])
    
    while True:
        break_dict = defaultdict(set)
        for r in range(0, n-1):
            for c in range(0, m-1):
                if trans_board[r][c] == '^':
                    break
                if check_area(trans_board, r, c):
                    add_dict(break_dict,r,c)

        if break_dict:
            for key, val in break_dict.items():
                for v in sorted(list(val), reverse=True):
                    answer += 1
                    trans_board[key].pop(v)
                    trans_board[key].append("^")
        else:
            break
    
    return answer

if __name__ == "__main__":
    print(14, solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(15, solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
    print(8, solution(8, 5, ["HGNHU", "CRSHV", "UKHVL", "MJHQB", "GSHOT", "MQMJJ", "AGJKK", "QULKK"]))
    print(4, solution(2, 2, ["AA","AA"]))
    print(0, solution(2, 2, ["AA","AB"]))
    print(4, solution(3, 2, ["AA","AA","AB"]))
    print(8, solution(6, 2, ["AA", "AA", "CC", "AA", "AA", "DD"]))
    print(8, solution(4, 4, ["ABCD", "BACE", "BCDD", "BCDD"]))
    print(27,solution(8, 9, ["ABCDADFDA", "ABDFQWERF", "WKDNFNRIT", "AKAKWODCJ", "AKAKWODCJ", "KKKKKKKKK", "KKKKKKKKK", "KKKKKKKKK"]))
    print(15, solution(4, 5, ["AAAAA", "AAAAU", "AAAUU", "UUUUU"]))
    print(24, solution(5, 6, ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"]))
    print(32, solution(6, 6, ["AABBEE", "AAAEEE", "VAAEEV", "AABBEE", "AACCEE", "VVCCEE"]))
    print(14, solution(4, 5, ["AAAAA","AUUUA","AUUAA","AAAAA"]))
    print(4, solution(3, 2, ["AA","AA","AB"]))
    print(8, solution(4, 2, ["CC","AA", "AA", "CC"]))
    print(12, solution(6, 2, ["DD", "CC", "AA", "AA", "CC", "DD"]))
    print(8, solution(8, 2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"]))
    print(14, solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(15, solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))