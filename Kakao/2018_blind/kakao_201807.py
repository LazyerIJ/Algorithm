'''
https://www.welcomekakao.com/learn/courses/30/lessons/42894
블록 게임
''' 
def solution(board):

    add_block_num = -1

    def check_block(board, width, height):
        block_cnt = 0
        for col in range(0, len(board[0])-(width-1)):
            for row in range(0, len(board)-(height-1)):
                matrix = []
                for c in range(width):
                    for r in range(height):
                        val = board[row+r][col+c]
                        matrix.append(val)
                if matrix.count(0)==0 and matrix.count(add_block_num)==2:
                    if(len(set(matrix))==2):
                        for c in range(width):
                            for r in range(height):
                                board[row+r][col+c] = 0
                        block_cnt += 1
        return board, block_cnt

    def add_block(board):
        for col in range(0, len(board[0])):
            for row in range(0, len(board)-1):
                if board[row][col]==0:
                    board[row][col] = add_block_num
                else:
                    break
        return board

    def replace_block(board):
        for col in range(0, len(board[0])):
            for row in range(0, len(board)):
                if board[row][col] == add_block_num:
                    board[row][col] = 0
        return board

    def print_board(board):
        for t in board:
            print(t)
        print()
        
    rs = 0
    while True:
        board = add_block(board)
        board, cnt_1 = check_block(board, 2, 3)
        board, cnt_2 = check_block(board, 3, 2)
        cnt = cnt_1 + cnt_2
        if cnt == 0:
            return rs
        else:
            rs += cnt
        board = replace_block(board)
    return rs



if __name__ == '__main__':
    board = [[0,0,0,0,1,1,1,0,0,0],
             [0,0,1,0,0,1,0,0,0,0],
             [0,1,1,1,5,0,0,0,0,0],
             [0,0,0,5,5,5,0,0,0,0],
             [0,0,0,0,0,0,4,0,0,0],
             [0,2,0,0,0,4,4,0,0,0],
             [1,2,2,2,3,0,4,0,0,0],
             [1,1,1,2,3,0,0,0,5,5],
             [1,2,2,2,3,3,0,0,0,5],
             [1,1,1,0,0,0,0,0,0,5]]	


    board = [[1,0,0,0],
             [1,0,0,0],
             [1,1,2,0],
             [2,2,2,0]]
    rs = solution(board)
    print(rs)
