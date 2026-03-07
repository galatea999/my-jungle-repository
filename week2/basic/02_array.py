"""
[배열 - 2차원 배열 회전]

문제 설명:
- N x N 크기의 2차원 배열을 시계방향으로 90도 회전시킵니다.
- 배열의 인덱스 변환 규칙을 이해하는 문제입니다.

입력:
- matrix: N x N 크기의 2차원 리스트

출력:
- 시계방향으로 90도 회전된 2차원 리스트

예제:
입력:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

출력:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

힌트:
- 회전 후 위치: (i, j) -> (j, n-1-i)
- 새로운 배열을 만들어 값을 채워넣으세요
"""

def rotate_matrix_90(matrix):
    """
    2차원 배열을 시계방향으로 90도 회전
    
    Args:
        matrix: N x N 2차원 리스트
    
    Returns:
        회전된 2차원 리스트
    """
    n = len(matrix)
    
    # TODO: n x n 크기의 새로운 배열을 생성하세요 (0으로 초기화) 이게 뭐라고 어렵냐? 
    rotated = [[0] * n for i in range(n)] #이해가 안가네 왜지? => 아.. [0]*n이 [0],[0],[0]이 아니라 [0,0,0]이 되고, for i in range[n]을 치면 i의 값에 관계 없이 n만큼 반복됨
        
    # TODO: 원본 배열의 각 요소를 회전된 위치에 배치하세요
    # 힌트: (i, j) 위치의 요소는 회전 후 (j, n-1-i) 위치로 이동

    #원본 배열의 모든 칸을 순회한 후, 각 칸의 값을 회전된 위치에 넣음
    # new_matrix = [[0,0,0],[0,0,0],[0,0,0]]

    for i in range(n) : # 행을 고르는 반복
        for j in range(n) : # 열을 고르는 반복
            rotated[j][n-1-i] = matrix[i][j] 
    # 잘 풀려면? 이것을 표 배열 그림이 아니라 좌표값으로 생각하기. [0][1] => (0,1) [0][2] => (0,2) 이런 식으로. 이따 다시 한 번 설명해보기
    
    return rotated

def print_matrix(matrix):
    """배열을 보기 좋게 출력하는 헬퍼 함수"""
    for row in matrix:
        print(row)

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 3x3 배열
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("원본 배열:")
    print_matrix(matrix1)
    print("\n회전 후:")
    rotated1 = rotate_matrix_90(matrix1)
    print_matrix(rotated1)
    print()
    
    # 테스트 케이스 2: 4x4 배열
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    print("원본 배열:")
    print_matrix(matrix2)
    print("\n회전 후:")
    rotated2 = rotate_matrix_90(matrix2)
    print_matrix(rotated2)


