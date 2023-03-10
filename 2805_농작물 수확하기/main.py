import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    m = N//2 # 농작물중 가장 긴 행
    result = 0 # 농작물의 가치 총 합

    for i in range(N): # i : data의 행 인덱스
        for j in range(abs(m-i), N-abs(m-i)): # j : data의 열 인덱스
            result += data[i][j]

    print(f'#{tc} {result}')