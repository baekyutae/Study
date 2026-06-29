# 자료구조 / 알고리즘 Scratch 구현 로드맵

> 목적: AI 도움 없이 자료구조와 알고리즘 템플릿을 직접 설계하고 구현하는 능력 강화
> 연결 대상: 기존 `풀이 순서.md`, `코테관리.md`
> 운영 방식: 문제풀이 로드맵은 유지하고, 각 주차에 맞는 Scratch 사이드퀘스트를 병행한다.

---

## 0. 이 로드맵의 목적과 범위

### 진짜 목적 (이게 1순위)

이 로드맵은 "자료구조/알고리즘 CS를 한방에 끝내기" 위한 것이 **아니다.**
다음 세 가지가 진짜 목적이다.

```text
1. AI 의존 무력감 탈출 + 손 풀기
   - 프로젝트를 AI에 전부 맡기다 보니 "AI 없이는 아무것도 못 한다"는 무력감
   - 미니프로젝트는 분량이 커서 후순위로 밀렸음 → 더 작은 atomic 단위가 필요
   - Scratch Quest는 한 파일/한 자리에서 끝나므로 시작 비용이 거의 0

2. 직접 코딩에서 나오는 학습효과
   - 절차적 숙련(동작 메커니즘 체화) + 불변식 사고

3. 라이브 코딩 대비
   - 자료구조/알고리즘 즉석 구현 요청 대응
```

### 이 로드맵이 길러주는 것 / 아닌 것

```text
길러지는 것:
- 절차적 숙련 (heapify, BFS level 분리 등 "어떻게 도는가")
- 불변식 사고 ("항상 만족해야 하는 조건이 뭔가")
- 패턴 반사 ("이 문제 = 이 템플릿")

길러지지 않는 것 (한계로 인정):
- 왜 이 자료구조를 쓰는가 (when/why) → 문제풀이가 담당
- 복잡도 증명, 해시 충돌 원리 등 CS 이론 → 별도 학습 영역
```

### 핵심 원칙

```text
이 문서는 문제풀이 순서를 대체하지 않는다. 반드시 보조다.
"다 한 번씩 짰다"가 목적이 아니라 "재구현 시 막힘 없이 되는가"가 목적이다.
5개를 깊게가 15개를 얕게보다 낫다.
```

```text
문제풀이 메인퀘스트:
- LeetCode / 백준 문제 풀이
- 1일 / 3일 / 7일 복습
- A/B/C/D/E 등급 관리

Scratch 사이드퀘스트:
- 자료구조를 백지에서 직접 설계하고 구현
- 알고리즘 템플릿을 안 보고 직접 구현
- 라이브코딩에서 손이 멈추지 않게 만드는 훈련
```

---

## 1. 구분 기준

### 자료구조 Scratch

데이터를 어떻게 저장하고 관리할지 직접 구현하는 것.

```text
Linked List
Doubly Linked List
Stack
Queue
Deque
HashMap (직접 구현은 X, 활용 패턴만 — 2번 항목 참고)
Heap
BST
Graph
Trie
Union-Find
LRU Cache
```

### 알고리즘 / 패턴 Scratch

저장된 데이터를 어떻게 탐색하고 처리할지 직접 구현하는 것.

```text
Two Pointers
Sliding Window
Prefix Sum
Binary Search
DFS
BFS
Backtracking
Topological Sort
Dijkstra
Kadane
DP 1D
DP 2D
```

예시:

```text
array/list        -> 자료구조
two pointers      -> 패턴
binary search     -> 알고리즘

graph adjacency   -> 자료구조
DFS/BFS           -> 알고리즘

heap              -> 자료구조
Dijkstra          -> 알고리즘
```

---

## 2. 공통 클리어 조건

각 Scratch Quest는 아래 조건을 만족하면 클리어로 본다.

```text
1. AI 없이 백지 구현 가능
2. 핵심 API를 직접 설계 가능
3. 경계 조건 테스트 작성 (개수가 아니라 "깨지는 지점"을 잡았는가)
   - 빈 입력 / 단일 원소 / capacity 1 / 중복 키 / 음수 / 사이클 등
   - 이 자료구조/알고리즘이 틀려도 happy path는 통과한다는 점을 의식할 것
4. 시간복잡도 / 공간복잡도 설명 가능
5. 핵심 불변식 설명 가능
6. 3~7일 뒤 무예고 재구현 가능 (정착 검증이 아니라 "라이브 코딩 실전 리허설")
```

> 변경점: 기존 "assert 5개 이상" → "경계 조건 커버"로 변경.
> 변경점: 기존 "다음날 재구현" → "3~7일 뒤 무예고 재구현 = 라이브 리허설"로 재프레이밍.

---

## 3. 단위 쪼개기 원칙 (1번 목적의 생명줄)

미니프로젝트가 후순위로 밀린 이유 = 시작 비용이 높아서.
같은 실수를 반복하지 않으려면 클리어 단위를 **Kit이 아니라 함수 레벨**로 내린다.

```text
- "하루 = 함수 1~2개 완성"을 기본 단위로 한다.
- 체크박스는 Kit 단위가 아니라 그 안의 개별 함수 단위로 만든다.
- 완성 빈도가 높을수록 무력감이 더 빨리 깨진다.
  (무력감은 "큰 걸 못 했다"가 아니라
   "오늘 내 손으로 뭘 완성했다"의 누적으로 깨진다)
```

---

## 4. 회복 가시화 지표 (1번 목적 전용)

무력감 탈출이 목적이면 "나아지고 있다"는 증거가 보여야 한다.
체크박스만으로는 안 보인다.

```text
- 재구현할 때마다 "AI / 참고자료 본 횟수"를 0~3으로 기록한다.
- 3 → 2 → 1 → 0 추이가 곧 무력감이 깨지는 객관적 신호다.
- 측정 가능한 독립 baseline 사고와 동일한 결.
```

---

## 5. 시간 예산

```text
- 코테 학습: 하루 1~1.5h / 미니프로젝트: 격일 45분
- Scratch가 메인 문제풀이나 Biblio를 잠식하면 본말전도다.
- 각 Phase에 "주당 Scratch 할당 시간 상한"을 명시하고 지킨다.
  (예: Phase A 구간 = 주당 최대 2~3시간 등, 실제 여력에 맞춰 기입)
```

---

## 6. Scratch 파일 기본 템플릿

각 파일 상단에 아래 주석을 붙인다.
테스트는 파일 안 `assert`로 둔다 (pytest 분리는 시작 비용을 높여 1번 목적을 해치므로 지금은 하지 않음).

```python
"""
Scratch Quest:
- 구현 대상:
- 자료구조 / 알고리즘:
- 핵심 불변식:
- 지원 API:
- 시간복잡도:
- 공간복잡도:
- 경계 조건(테스트로 잡은 것):
- 헷갈린 지점:
- 재구현 날짜:
- 참고 본 횟수(0~3):
"""
```

---

## 7. 현재 진행도 기준 우선순위

현재 문제풀이 진행은 Tree BFS / BST / Heap 초입으로 본다.

따라서 지금 가장 먼저 보강할 Scratch Debt는 아래 순서다.
(LRU는 C/D로 흔들렸던 최우선 항목이므로 상위로 올림 — 체크리스트와 정합)

```text
1. LRU Cache
2. Tree BFS Kit
3. BST Kit
4. Tree Traversal Kit
5. Binary Heap
6. Binary Search Templates
7. Two Pointers Kit
8. Sliding Window Kit
```

특히 아래 항목은 C/D 등급으로 흔들렸던 구간이므로 우선순위가 높다.

```text
LRU Cache
Construct Binary Tree from Preorder and Inorder
Average of Levels in Binary Tree
Binary Tree Level Order Traversal
```

---

# Phase A. 즉시 갚을 Scratch Debt

## A-1. LRU Cache

### 분류

```text
자료구조 Scratch
```

### 구현 대상 (함수 단위 체크)

```text
[x] Node
[x] DoublyLinkedList._add_to_tail
[x] DoublyLinkedList._remove
[ ] DoublyLinkedList._pop_head
[x] LRUCache.get
[x] LRUCache.put
```

### 필수 API

```python
get(key)
put(key, value)
```

### 핵심 불변식

```text
1. dict[key]는 해당 key를 가진 Node를 가리킨다.
2. head 다음 노드는 가장 오래 전에 사용된 노드다.
3. tail 이전 노드는 가장 최근에 사용된 노드다.
4. get/put으로 접근된 노드는 tail 앞으로 이동한다.
5. capacity 초과 시 head 다음 노드를 제거한다.
```

### 클리어 조건

```text
- get O(1) / put O(1) (dict는 average case 기준임을 의식)
- 기존 key 갱신 처리 가능
- capacity 초과 처리 가능
- dummy head/tail을 사용하는 이유 설명 가능
- 경계: capacity 1, 같은 key 연속 put, 존재하지 않는 key get
```

### 추천 파일

```text
scratch/linked_list/lru_cache.py
```

---

## A-2. Tree Traversal Kit

### 분류

```text
자료구조 + 알고리즘 Scratch
```

### 구현 대상 (함수 단위 체크)

```text
[ ] TreeNode
[ ] preorder recursive
[ ] inorder recursive
[ ] postorder recursive
[ ] inorder iterative   (iterative는 이거 하나면 충분)
```

> 변경점: iterative postorder 제거. iterative는 inorder 하나로 족하다.
> preorder iterative는 여력 있으면 선택.

### 필수 API

```python
preorder(root)
inorder(root)
postorder(root)
inorder_iter(root)
```

### 핵심 불변식

```text
1. 재귀 DFS는 base case가 먼저다.
2. inorder는 BST에서 오름차순 순회가 된다.
3. iterative traversal은 stack으로 호출 스택을 직접 흉내낸다.
```

### 클리어 조건

```text
- 재귀 DFS 3종 구현 가능
- 반복 inorder 구현 가능
- inorder와 BST의 관계 설명 가능
- (응용 흡수) preorder + inorder로 트리 복원 1회 손으로 해보기
  → 기존 Tree Builder를 여기로 흡수
```

### 추천 파일

```text
scratch/tree/tree_traversal.py
```

---

## A-3. Tree BFS Kit

### 분류

```text
알고리즘 Scratch
```

### 구현 대상

```text
[ ] level_order
[ ] right_side_view
[ ] average_of_levels
```

### 필수 템플릿

```python
while queue:
    level_size = len(queue)

    for _ in range(level_size):
        node = queue.popleft()
```

### 핵심 불변식

```text
1. level_size는 현재 레벨의 노드 수를 고정한다.
2. for문 안에서 queue에 추가되는 노드는 다음 레벨이다.
3. 현재 레벨과 다음 레벨은 level_size로 분리된다.
```

### 클리어 조건

```text
- level order 구현 가능
- right side view 구현 가능
- average of levels 구현 가능
- level_size를 먼저 저장하는 이유 설명 가능
- 경계: 빈 트리, 한쪽으로만 치우친 트리
```

### 추천 파일

```text
scratch/tree/tree_bfs.py
```

---

## A-4. BST Kit

### 분류

```text
자료구조 + 알고리즘 Scratch
```

### 구현 대상

```text
[ ] BST insert
[ ] BST search
[ ] validate_bst
[ ] kth_smallest
[ ] (응용 흡수) preorder/inorder 복원 — 구 Tree Builder
```

### 필수 API

```python
insert(root, val)
search(root, target)
is_valid_bst(root)
kth_smallest(root, k)
```

### 핵심 불변식

```text
1. 모든 left subtree 값은 현재 노드보다 작다.
2. 모든 right subtree 값은 현재 노드보다 크다.
3. 단순히 부모와만 비교하면 안 된다.
4. lower/upper bound를 재귀적으로 들고 내려가야 한다.
```

### 클리어 조건

```text
- BST 삽입/탐색 구현 가능
- lower/upper bound 방식으로 validate 가능
- inorder로 kth smallest 구현 가능
- 경계: 중복값 처리(< vs <=), 단일 노드, 한쪽으로 긴 트리
```

### 추천 파일

```text
scratch/tree/bst.py
```

> 구 A-4 Tree Builder는 독립 Quest에서 해제하고 A-2 / A-4 응용으로 흡수했다.
> 이유: LC 105 한 문제 특화 기법, 라이브 출제 빈도 낮음.

---

# Phase B. 현재 주차 이후 Scratch 로드맵

## B-1. Two Pointers Kit  (신설 · 최상)

### 연결 주차

```text
Week 5~6 사이 조기 투입 권장 (배열 패턴은 라이브에서 손이 가장 자주 멈춤)
```

### 분류

```text
패턴 Scratch
```

### 구현 대상

```text
[ ] 양끝 투포인터 (Valid Palindrome)
[ ] 정렬 배열 투포인터 (Two Sum II)
[ ] 면적/용량 최적화 (Container With Most Water)
```

### 핵심 불변식

```text
1. 두 포인터가 좁혀지는 방향과 종료 조건을 먼저 정한다.
2. 어느 포인터를 왜 움직이는지 매 스텝 근거가 있어야 한다.
```

### 클리어 조건

```text
- 양끝에서 좁히는 패턴 구현 가능
- 정렬 전제 투포인터 구현 가능
- 포인터 이동 결정 근거 설명 가능
- 경계: 길이 0/1, 모두 동일 원소
```

### 추천 파일

```text
scratch/patterns/two_pointers.py
```

---

## B-2. Sliding Window Kit  (신설 · 최상)

### 연결 주차

```text
Week 6 전후
```

### 분류

```text
패턴 Scratch
```

### 구현 대상

```text
[ ] 가변 윈도우 (Longest Substring Without Repeating Characters)
[ ] 조건 만족 최소 윈도우 (Minimum Size Subarray Sum)
```

### 핵심 불변식

```text
1. 윈도우 확장 조건과 축소 조건을 분리해서 정의한다.
2. 윈도우 안의 상태(빈도/합)는 확장·축소와 동기화되어야 한다.
```

### 클리어 조건

```text
- 윈도우 확장/축소 루프 구현 가능
- 윈도우 내부 상태 갱신 정확
- 경계: 빈 문자열, 답이 없는 경우, 전체가 답인 경우
```

### 추천 파일

```text
scratch/patterns/sliding_window.py
```

---

## B-3. HashMap Pattern Kit  (신설 · 상)

### 연결 주차

```text
Week 5~7 분산 투입
```

### 분류

```text
패턴 Scratch (HashMap 자체 구현 X, 도구로 쓰는 패턴 O)
```

### 구현 대상

```text
[ ] Two Sum (보수 lookup)
[ ] Group Anagrams (정규화 key)
[ ] 빈도 카운팅 / seen 집합 패턴
```

### 핵심 불변식

```text
1. "이미 본 것"을 hashmap에 저장해 O(1) 조회로 바꾸는 것이 핵심.
2. key를 무엇으로 잡느냐가 문제의 절반이다.
```

### 클리어 조건

```text
- 보수 lookup 패턴 구현 가능
- 정규화 key 설계 가능
- 빈도/seen 패턴 구현 가능
```

### 추천 파일

```text
scratch/patterns/hashmap_patterns.py
```

---

## B-4. Binary Heap

### 연결 주차

```text
Week 6: Tree BFS + Heap
```

### 분류

```text
자료구조 Scratch
```

### 구현 대상

```text
[ ] MinHeap (push / pop / peek)
[ ] _heapify_up
[ ] _heapify_down
[ ] MaxHeap (선택)
```

### 필수 공식

```python
parent = (i - 1) // 2
left = 2 * i + 1
right = 2 * i + 2
```

### 핵심 불변식

```text
MinHeap: 부모 노드는 항상 자식 노드보다 작거나 같다.
MaxHeap: 부모 노드는 항상 자식 노드보다 크거나 같다.
```

### 클리어 조건

```text
- heapq 없이 min heap 구현 가능
- push 후 heapify_up 가능
- pop 후 heapify_down 가능
- 배열 기반 트리 인덱스 설명 가능
- 경계: 원소 1개, pop을 빈 heap에 호출
```

### 추천 파일

```text
scratch/heap/binary_heap.py
```

---

## B-5. Median Finder  (우선순위 상 → 중 하향)

### 연결 주차

```text
Week 6: Find Median from Data Stream
```

### 분류

```text
자료구조 응용 Scratch
```

> 변경점: Binary Heap을 제대로 하면 따라오는 응용이고 문제 1개 특화라
> 우선순위를 "상"에서 "중"으로 내림. Heap 클리어 후에 다룬다.

### 구현 대상

```text
[ ] MedianFinder (Two Heap)
[ ] addNum / findMedian
```

### 핵심 불변식

```text
1. small heap은 작은 절반(max heap처럼 동작).
2. large heap은 큰 절반(min heap처럼 동작).
3. 두 heap의 크기 차이는 1 이하로 유지.
4. small의 최대값 <= large의 최소값.
```

### 클리어 조건

```text
- 홀수/짝수 개수 median 계산 가능
- 두 heap rebalancing 구현 가능
```

### 추천 파일

```text
scratch/heap/median_finder.py
```

---

## B-6. Binary Search Templates

### 연결 주차

```text
Week 7: Binary Search
```

### 분류

```text
알고리즘 Scratch
```

### 구현 대상

```text
[ ] exact binary search
[ ] lower_bound
[ ] upper_bound
[ ] search_insert_position
[ ] (선택) rotated_array_search
[ ] (선택) parametric search "답을 이분 탐색"
```

### 개념 구분

```text
exact: target 있으면 index, 없으면 -1
lower_bound: 처음으로 target 이상이 되는 위치
upper_bound: 처음으로 target 초과가 되는 위치
search insert: target이 들어갈 첫 위치 (사실상 lower_bound)
parametric: "최소 X를 찾아라" 류 — 값이 아니라 답을 이분 탐색
```

### 클리어 조건

```text
- left <= right 버전 구현 가능
- left < right 버전 구현 가능
- lower_bound / upper_bound 차이 설명 가능
- off-by-one을 경계 테스트로 잡을 수 있음
  경계: 빈 배열 / target이 모든 원소보다 큼·작음 / 중복 원소
```

### 추천 파일

```text
scratch/binary_search/templates.py
```

---

## B-7. Graph Kit

### 연결 주차

```text
Week 8: Graph DFS/BFS
```

### 분류

```text
자료구조 + 알고리즘 Scratch
```

### 구현 대상

```text
[ ] Adjacency List
[ ] add_vertex / add_edge
[ ] DFS recursive
[ ] DFS iterative
[ ] BFS
```

### 핵심 불변식

```text
1. graph[node]는 인접 노드 목록이다.
2. visited는 중복 방문을 막는다.
3. 무방향 그래프는 양쪽 간선을 모두 추가한다.
4. 방향 그래프는 한쪽 간선만 추가한다.
```

### 클리어 조건

```text
- 방향/무방향 그래프 구현 가능
- DFS/BFS 구현 가능
- 비연결 그래프 전체 순회 가능
```

### 추천 파일

```text
scratch/graph/graph.py
```

---

## B-8. Grid Search Kit

### 연결 주차

```text
Week 8: Number of Islands, Surrounded Regions
```

### 분류

```text
알고리즘 Scratch
```

### 구현 대상

```text
[ ] grid DFS
[ ] grid BFS
[ ] 방향 배열 / 범위 체크 / visited 처리
```

### 필수 템플릿

```python
directions = [(1,0), (-1,0), (0,1), (0,-1)]
```

### 핵심 불변식

```text
1. row/col이 범위를 벗어나면 탐색하지 않는다.
2. 이미 방문한 칸은 다시 방문하지 않는다.
3. BFS에서는 queue에 넣을 때 visited 처리하는 편이 중복 방지에 안전하다.
```

### 클리어 조건

```text
- grid DFS / BFS 구현 가능
- 방향 배열 실수 없이 작성 가능
- visited 찍는 시점 설명 가능
```

### 추천 파일

```text
scratch/graph/grid_search.py
```

---

## B-9. Topological Sort

### 연결 주차

```text
Week 8: Course Schedule, Course Schedule II
```

### 분류

```text
알고리즘 Scratch
```

### 구현 대상

```text
[ ] indegree 계산
[ ] queue 기반 처리
[ ] topological order 산출
[ ] cycle detection
```

### 핵심 불변식

```text
1. indegree는 현재 노드로 들어오는 간선 수다.
2. indegree가 0인 노드는 선행 조건이 없다.
3. 노드를 처리하면 그 노드가 가리키는 이웃의 indegree를 줄인다.
4. 처리한 노드 수가 전체보다 작으면 cycle이 있다.
```

### 클리어 조건

```text
- Course Schedule / II 방식 구현 가능
- cycle detection 설명 가능
```

### 추천 파일

```text
scratch/graph/topological_sort.py
```

---

## B-10. Backtracking Templates

### 연결 주차

```text
Week 9: Backtracking
```

### 분류

```text
알고리즘 Scratch
```

### 구현 대상

```text
[ ] subsets
[ ] permutations
[ ] combinations
[ ] combination_sum
[ ] grid backtracking (Word Search)
```

### 핵심 템플릿

```python
def backtrack(path):
    if 종료조건:
        result.append(path[:])
        return
    for choice in choices:
        path.append(choice)
        backtrack(path)
        path.pop()
```

### 개념 구분

```text
순열: visited 필요
조합: start index 필요
중복 허용 조합: 같은 i를 다시 넘길 수 있음
grid backtracking: 방문 표시 후 재귀, 돌아오면서 방문 해제
```

### 클리어 조건

```text
- subsets / permutations / combinations / combination_sum 구현 가능
- Word Search 스타일 grid backtracking 구현 가능
```

### 추천 파일

```text
scratch/backtracking/templates.py
```

---

## B-11. Trie

### 연결 주차

```text
Week 9: Implement Trie
```

### 분류

```text
자료구조 Scratch
```

### 구현 대상

```text
[ ] TrieNode
[ ] insert / search / startsWith
```

### 핵심 불변식

```text
1. 각 노드는 children dict를 가진다.
2. 단어의 끝은 is_end로 표시한다.
3. prefix 존재와 word 존재는 다르다.
```

### 클리어 조건

```text
- insert / search / startsWith 구현 가능
- prefix와 word를 구분해서 설명 가능
```

### 추천 파일

```text
scratch/trie/trie.py
```

---

## B-12. Kadane + Prefix Sum

### 연결 주차

```text
Week 9: Maximum Subarray
```

### 분류

```text
알고리즘 Scratch
```

### 구현 대상

```text
[ ] Kadane (Maximum Subarray)
[ ] Prefix Sum + HashMap (Subarray Sum Equals K)  ← 신설
```

### 핵심 아이디어

```text
Kadane:
현재 원소부터 새로 시작할지, 이전 subarray에 이어 붙일지 결정.

Prefix Sum:
누적합을 hashmap에 저장해 "구간 합 = k"를 O(1) 조회로 바꾼다.
이 "prefix sum을 hashmap에 저장" 아이디어는 손으로 안 짜보면 라이브에서 안 나온다.
```

### 클리어 조건

```text
- Kadane: current_sum / best_sum 갱신, 모든 수가 음수인 경우 처리
- Prefix Sum: 누적합 hashmap 패턴 구현, 구간 합 = k 카운트 가능
```

### 추천 파일

```text
scratch/dp/kadane.py
scratch/patterns/prefix_sum.py
```

---

## B-13. DP 1D Kit

### 연결 주차

```text
Week 10: DP 1D
```

### 분류

```text
알고리즘 Scratch
```

### 구현 대상

```text
[ ] climbing stairs
[ ] house robber
[ ] coin change
[ ] word break
[ ] LIS
```

### 공통 절차

```text
1. dp[i]가 무엇인지 정의한다.
2. 초기값을 정한다.
3. 점화식을 세운다.
4. 정답이 dp의 어디에 있는지 정한다.
```

### 클리어 조건

```text
- dp[i] 의미를 주석으로 먼저 작성
- 1D 배열로 상태 관리 가능
- 선택/비선택 패턴 설명 가능
- 최소/최대/가능 여부 DP 구분 가능
```

### 추천 파일

```text
scratch/dp/dp_1d.py
```

---

## B-14. DP 2D Kit

### 연결 주차

```text
Week 11: DP Multi-D
```

### 분류

```text
알고리즘 Scratch
```

### 구현 대상

```text
[ ] grid dp
[ ] string dp
[ ] edit distance
[ ] maximal square
```

### 핵심 불변식

```text
1. dp[r][c] 또는 dp[i][j]가 무엇을 뜻하는지 먼저 정한다.
2. 첫 행/첫 열 초기화가 중요하다.
3. 문자열 DP는 인덱스가 한 칸 밀리는 경우가 많다.
```

### 클리어 조건

```text
- grid / string DP 구현 가능
- edit distance 테이블 구현 가능
- 인덱스 밀림을 주석으로 설명 가능
```

### 추천 파일

```text
scratch/dp/dp_2d.py
```

---

## B-15. Dijkstra

### 연결 주차

```text
Week 12: 백준 최단경로
```

### 분류

```text
알고리즘 Scratch
```

### 구현 대상

```text
[ ] weighted graph (adjacency list)
[ ] distance array 초기화
[ ] priority queue
[ ] relaxation + stale entry skip
```

### 핵심 불변식

```text
1. dist[node]는 현재까지 발견한 start -> node 최단거리다.
2. heap에는 다음으로 볼 후보가 들어간다.
3. heap에서 꺼낸 거리가 dist[node]보다 크면 오래된 정보이므로 스킵한다.
4. 더 짧은 경로를 찾으면 dist를 갱신하고 heap에 넣는다.
5. 음수 가중치에서는 Dijkstra가 틀린다 → 그때는 Bellman-Ford.
```

### 클리어 조건

```text
- adjacency list 기반 가중치 그래프 구현 가능
- dist 배열 초기화 가능
- stale entry skip 구현 가능
- relaxation 설명 가능
- "왜 음수 간선에서 안 되는가" 설명 가능
```

### 추천 파일

```text
scratch/graph/dijkstra.py
```

---

## B-16. Union-Find

### 연결 주차

```text
Week 12: 유니온파인드
```

### 분류

```text
자료구조 Scratch
```

### 구현 대상

```text
[ ] find / union / connected
[ ] path compression
[ ] union by rank 또는 size
```

### 핵심 불변식

```text
1. parent[x]는 x의 부모를 가리킨다.
2. find(x)는 x가 속한 집합의 대표 루트를 찾는다.
3. union(a, b)는 두 집합을 합친다.
4. path compression은 find 과정에서 부모를 루트로 압축한다.
5. union by rank/size는 트리가 한쪽으로 길어지는 것을 막는다.
```

### 클리어 조건

```text
- find / union 구현 가능
- path compression 구현 가능
- union by rank 또는 size 구현 가능
```

### 추천 파일

```text
scratch/union_find/union_find.py
```

---

## B-17. Simulation Kit

### 연결 주차

```text
Week 12: 구현/시뮬레이션
```

### 분류

```text
알고리즘 Scratch
```

### 구현 대상

```text
[ ] direction control
[ ] grid copy
[ ] state transition
[ ] rotation
[ ] combination brute force
```

### 클리어 조건

```text
- 방향 배열을 실수 없이 작성
- 상태를 동시에 바꿔야 하는 경우와 순차 변경해도 되는 경우 구분
- grid deepcopy 필요 여부 판단
- 회전 구현 가능
```

### 추천 파일

```text
scratch/simulation/grid_simulation.py
```

---

# Phase C. Final Boss 재구현 목록

모의고사 구간에서는 새 구현을 늘리지 말고, 아래 항목을 랜덤으로 백지 구현한다.
단, interleaving(섞어서 재구현)은 Phase C를 기다리지 말고
**Week 8 이후부터 주 2~3회 "이전 Phase 항목 랜덤 1개 재구현"으로 미리 끼워넣는다.**
(라이브 코딩은 본질적으로 무엇이 나올지 모르는 interleaved 환경이다)

```text
LRU Cache
Tree Traversal Kit
Tree BFS Kit
BST Kit
Two Pointers Kit
Sliding Window Kit
HashMap Pattern Kit
Binary Heap
Median Finder
Binary Search Templates
Graph Kit
Grid Search Kit
Topological Sort
Backtracking Templates
Trie
Kadane + Prefix Sum
DP 1D Kit
DP 2D Kit
Dijkstra
Union-Find
Simulation Kit
```

## Final Boss 클리어 기준

```text
1. 랜덤으로 하나 고른다.
2. 백지에서 구현한다.
3. 경계 조건 테스트를 직접 작성한다.
4. 시간복잡도 / 공간복잡도를 적는다.
5. 핵심 불변식을 적는다.
6. 과거에 틀렸던 지점이 재발했는지 확인한다.
7. 참고 본 횟수(0~3)를 기록한다.
```

---

# 추천 폴더 구조

```text
scratch/
  patterns/
    two_pointers.py
    sliding_window.py
    hashmap_patterns.py
    prefix_sum.py

  linked_list/
    singly_linked_list.py
    doubly_linked_list.py
    lru_cache.py

  tree/
    tree_traversal.py
    tree_bfs.py
    bst.py

  heap/
    binary_heap.py
    median_finder.py

  binary_search/
    templates.py

  graph/
    graph.py
    grid_search.py
    topological_sort.py
    dijkstra.py

  backtracking/
    templates.py

  trie/
    trie.py

  union_find/
    union_find.py

  dp/
    kadane.py
    dp_1d.py
    dp_2d.py

  simulation/
    grid_simulation.py
```

---

# 진행 체크리스트

| 상태 | Quest | 분류 | 연결 주차 | 우선순위 |
|---|---|---|---|---|
| ⬜ | LRU Cache | 자료구조 | Week 4 복습 | 최상 |
| ⬜ | Tree BFS Kit | 알고리즘 | Week 6 | 최상 |
| ⬜ | BST Kit | 자료구조 + 알고리즘 | Week 6 | 최상 |
| ⬜ | Tree Traversal Kit | 자료구조 + 알고리즘 | Week 5 | 최상 |
| ⬜ | Two Pointers Kit | 패턴 | Week 5~6 | 최상 |
| ⬜ | Sliding Window Kit | 패턴 | Week 6 | 최상 |
| ⬜ | HashMap Pattern Kit | 패턴 | Week 5~7 | 상 |
| ⬜ | Binary Heap | 자료구조 | Week 6 | 상 |
| ⬜ | Median Finder | 자료구조 응용 | Week 6 | 중 |
| ⬜ | Binary Search Templates | 알고리즘 | Week 7 | 상 |
| ⬜ | Graph Kit | 자료구조 + 알고리즘 | Week 8 | 최상 |
| ⬜ | Grid Search Kit | 알고리즘 | Week 8 | 최상 |
| ⬜ | Topological Sort | 알고리즘 | Week 8 | 상 |
| ⬜ | Backtracking Templates | 알고리즘 | Week 9 | 상 |
| ⬜ | Trie | 자료구조 | Week 9 | 상 |
| ⬜ | Kadane + Prefix Sum | 알고리즘 | Week 9 | 중 |
| ⬜ | DP 1D Kit | 알고리즘 | Week 10 | 상 |
| ⬜ | DP 2D Kit | 알고리즘 | Week 11 | 상 |
| ⬜ | Dijkstra | 알고리즘 | Week 12 | 최상 |
| ⬜ | Union-Find | 자료구조 | Week 12 | 최상 |
| ⬜ | Simulation Kit | 알고리즘 | Week 12 | 상 |

---

# 오답노트 연결 템플릿

Scratch 구현 후 기존 `코테관리.md`의 오답노트 형식과 연결해서 아래처럼 기록한다.

```text
- 유형:
- 막힌 이유:
- 트리거:
- 파이썬 포인트:
- Scratch Quest:
- 핵심 불변식:
- 참고 본 횟수(0~3):
- 다시 구현 필요 여부:
```

예시:

```text
- 유형: Tree BFS
- 막힌 이유: level_size를 고정하지 않아 현재 레벨과 다음 레벨이 섞임
- 트리거: "각 층", "level", "right side", "average"가 보이면 BFS level order
- 파이썬 포인트: deque, popleft, len(queue)
- Scratch Quest: Tree BFS Kit
- 핵심 불변식: level_size는 현재 레벨의 노드 수를 고정한다
- 참고 본 횟수: 2
- 다시 구현 필요 여부: 예
```

---

# 현재 기준 다음 액션

지금 바로 이어서 할 순서는 아래가 가장 자연스럽다.
(LRU는 C/D로 흔들렸던 최우선 항목이라 1번으로 올림)

```text
1. LRU Cache
2. Tree BFS Kit
3. BST Kit
4. Tree Traversal Kit
5. Two Pointers Kit
6. Sliding Window Kit
7. Binary Heap
8. Binary Search Templates
```

이 순서는 현재 진행 중인 Tree BFS / BST / Heap 구간과 잘 맞고,
기존 기록상 C/D로 흔들렸던 LRU를 가장 먼저 보강하며,
라이브에서 손이 자주 멈추는 배열 패턴(투포인터/슬라이딩윈도우)을 조기 투입한다.

---

# 한 줄 요약

```text
문제풀이는 기존 로드맵대로 간다. Scratch는 보조다.
단위는 함수 레벨로 잘게(완성 빈도 = 무력감 탈출의 핵심).
클리어 기준은 개수가 아니라 경계 조건. 재구현은 라이브 리허설.
트리·그래프에 치우쳤던 구성에 배열 패턴(투포인터/슬라이딩윈도우/프리픽스/해시맵)을 보강.
참고 본 횟수 0~3으로 회복을 가시화한다.
```
