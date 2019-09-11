def solution(X, Y, D):
    dist = Y-X
    return int(dist/D) + round(dist/D-dist//D+0.5)


if __name__ == '__main__':
    print(solution(10, 100, 30))
