# JUNGLE Algorithm Study Archive

크래프톤 정글 학습 과정에서 풀이한 알고리즘 문제, 기본 개념 실습, 코어타임 코드, 주간 퀴즈를 정리한 개인 학습 저장소입니다.  
현재 저장소는 `week2`부터 `week5`까지의 Python 풀이를 포함하고 있으며, 주차별로 학습 주제와 산출물이 분리되어 있습니다.

## 저장소 개요

- 언어: Python
- 성격: 알고리즘/자료구조 학습 기록 저장소
- 구성 방식: 주차별 디렉터리 + 학습 유형별 분리
- 주요 학습 유형
  - `basic`: 개념 실습 및 예제 코드
  - `problem-solving`: 백준 / LeetCode 문제 풀이
  - `core_time`, `core-time`: 코어타임 중 작성한 코드
  - `weekly_quiz`: 주간 퀴즈 풀이

## 현재 폴더 구조

```text
JUNGLE/
├── README.md
├── problems set.md
├── explusive_string.png
├── week2/
│   ├── basic/
│   ├── core_time/
│   ├── problem-solving/
│   └── weekly_quiz/
├── week3/
│   ├── basic/
│   ├── core-time/
│   └── problem-solving/
├── week4/
│   ├── basic/
│   └── problem-solving/
└── week5/
    ├── basic/
    └── problem-solving/
```

## 주차별 구성

### Week 2
- `basic`: 12개 Python 파일
- `problem-solving`: 20개 문제 풀이
- `core_time`: 2개 실습 파일
- `weekly_quiz`: 6개 퀴즈 풀이

주요 주제:
- Python dict / array / string
- brute force / recursion / backtracking
- complexity / bubble sort / insertion sort
- number theory

### Week 3
- `basic`: 11개 Python 파일
- `problem-solving`: 20개 문제 풀이
- `core-time`: 6개 실습 파일

주요 주제:
- binary search
- divide and conquer
- quick sort / merge sort
- stack / queue / priority queue
- linked list / hash table

### Week 4
- `basic`: 7개 Python 파일
- `problem-solving`: 19개 문제 풀이

주요 주제:
- binary tree / BST
- graph basic
- BFS / DFS
- topological sort

### Week 5
- `basic`: 5개 Python 파일
- `problem-solving`: 17개 문제 풀이

주요 주제:
- dynamic programming
- greedy
- LIS / LCS / knapsack / TSP 계열 문제

## 문제 풀이 파일 규칙

`problem-solving` 폴더의 파일명은 아래 정보를 함께 담도록 정리되어 있습니다.

- 난이도
- 주제
- 문제 이름
- 티어

예시:

```text
난이도중_백트래킹_NQueen_골드4.py
난이도하_그래프DFSBFS_바이러스_실버3.py
Extra_DP_EditDistance.py
```

이 규칙 덕분에 파일명만 봐도 어떤 유형의 문제인지 빠르게 파악할 수 있습니다.

## 실행 방법

대부분의 풀이 파일은 표준 입력을 받아 실행하는 단일 Python 스크립트입니다.

예시:

```bash
python3 /Users/galatea/Documents/GitHub/JUNGLE/week4/problem-solving/난이도중_BFS_미로탐색_실버1.py
```

입력이 필요한 문제는 터미널에서 직접 입력하거나 리다이렉션해서 실행하면 됩니다.

```bash
python3 some_problem.py < input.txt
```

## 기본 예제 검증

`basic` 폴더에는 일부 주차에서 `check.py`가 포함되어 있어 예제 파일을 확인할 수 있습니다.

예시:

```bash
cd /Users/galatea/Documents/GitHub/JUNGLE/week2/basic
python3 check.py --all
```

또는 특정 파일만 실행할 수 있습니다.

```bash
cd /Users/galatea/Documents/GitHub/JUNGLE/week3/basic
python3 check.py 03_quick_sort.py
```

출력 예시는 각 주차의 `*_output.txt` 파일에 함께 저장되어 있습니다.

## 저장소 특징

- 템플릿 저장소 상태가 아니라 실제 풀이가 채워진 학습 아카이브입니다.
- 주차별 학습 흐름이 살아 있어 복습용으로 보기 좋게 정리되어 있습니다.
- 기본 개념 실습과 실전 문제 풀이가 분리되어 있어 탐색이 쉽습니다.
- 백준 스타일 문제와 LeetCode 스타일 연습 문제가 함께 포함되어 있습니다.

## 참고 파일

- [problems set.md](/Users/galatea/Documents/GitHub/JUNGLE/problems%20set.md)
  - 주차별 문제 목록 참고용 문서
- `week2/basic/check.py`, `week3/basic/check.py`, `week4/basic/check.py`, `week5/basic/check.py`
  - 기본 문제 점검용 스크립트

## 참고 사항

- 폴더명에 `core_time`과 `core-time`이 혼재되어 있습니다. 현재 저장소 구조를 그대로 반영한 상태입니다.
- 일부 파일은 개인 학습 중간 결과물이므로 코드 스타일이나 네이밍이 완전히 통일되어 있지는 않습니다.
- 루트 README는 저장소 전체 안내 문서이고, 실제 학습 내용은 각 주차 폴더 안의 파일들이 기준입니다.
