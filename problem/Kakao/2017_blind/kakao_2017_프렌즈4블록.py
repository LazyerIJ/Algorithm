def solution(m, n, board):
    #  m: height
    #  n: width
    #  board: board
    empty ='0' 
    board = [list(x) for x in board]

    def check_board(m, n, board):
        flag = []
        for i in range(m):
            flag.append([False]*n)
        for r in range(m-1):
            for c in range(n-1):
                target = board[r][c] + board[r][c+1] + board[r+1][c] + board[r+1][c+1]
                if len(set(target))==1 and empty not in target:
                    flag[r][c] = flag[r][c+1] = flag[r+1][c] = flag[r+1][c+1] = True
        return flag

    def remove_board(board, flag, m, n):
        for c in range(n):#왼쪽에서 오른쪽
            for idx in range(m-1, 0, -1):#밑에서 위로
                if flag[idx][c] == False:#값이 있으면
                    continue
                for chk in range(idx-1, -1, -1):#값이 없으면 한칸 위에서부터 제일 위 까지
                    if flag[chk][c]==True and chk==0:
                        board[idx][c]='0'
                        break
                    if flag[chk][c]==False:#값이 있는 것을 찾으면
                        flag[chk][c]=True#데이터를 바꾼다
                        flag[idx][c]=False
                        board[idx][c]=board[chk][c]
                        board[chk][c]='0'
                        break
        return board

    max_point = 0
    while True:
        flag = check_board(m, n, board)
        point = sum([sum(x) for x in flag])
        print(point)
        if point==0:
            break
        board = remove_board(board, flag, m, n)
        max_point += point
    return max_point


if __name__ == '__main__':
    m = 4
    n = 5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]	
    #print(14, solution(m, n, board))

    m = 6
    n = 6
    board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	
    print(15, solution(m, n, board))
