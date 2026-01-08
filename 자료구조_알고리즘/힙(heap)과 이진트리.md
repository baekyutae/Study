# 이진트리(Binary Tree)

### 정의

- **트리(Tree):** 데이터(노드)들이 나뭇가지처럼 연결된 비선형 계층 구조.
    
- **이진 트리(Binary Tree):** 모든 노드가 최대 2개의 자식(Child)만을 가질 수 있는 트리.
### 이진 트리의 종류 

모양에 따라 이름이 다름

**A. 포화 이진 트리 (Perfect Binary Tree)**

- **모양:** 삼각형 모양으로 빈틈없이 꽉 찬 트리.
    
- **특징:** 모든 레벨이 꽉 차 있어서 노드 개수를 수식으로 딱 구할 수 있음. ($2^k - 1$)
    

 **B. 완전 이진 트리 (Complete Binary Tree) -> 힙(Heap)

- **모양:** 위에서 아래로, **왼쪽에서 오른쪽으로** 순서대로 차곡차곡 채워진 트리.
    
- **특징:**
    
    - 마지막 레벨을 제외하고는 꽉 차 있어야 함.
        
    - 마지막 레벨도 **왼쪽부터** 채워져 있어야 함. (오른쪽에 뜬금없이 노드가 있으면 안 됨)
        
    - **이 구조여야 배열(List)로 구현했을 때 빈 공간 없이 딱 들어맞음.**
        

 **C. 편향 이진 트리 (Skewed Binary Tree)**

- **모양:** 한쪽으로만 계속 자식이 달린 트리. (사실상 막대기)
    
- **특징:** 트리의 장점(빠른 탐색)을 다 잃어버리고 연결 리스트처럼 변해버린 최악의 형태.

# 힙(Heap)

### 정의

- **힙(Heap):** 최댓값이나 최솟값을 빠르게 O(logN) 찾아내기 위해 고안된 **완전 이진 트리(Complete Binary Tree)** 기반의 자료구조.
    
- '더미(Heap)'라는 뜻처럼 데이터들이 수북이 쌓여 있는 모습에서 유래

### 힙의 종류 

 **A. 최소 힙 (Min Heap)** - heapq

- **규칙:** 부모 노드 값 ≤ 자식 노드 값
    
- **특징:** 루트(가장 위)에 **가장 작은 값**이 위치함.
    
- **용도:** 오름차순 정렬, 우선순위가 낮은 순서 처리.
    

 **B. 최대 힙 (Max Heap)**

- **규칙:** 부모 노드 값 ≥ 자식 노드 값
    
- **특징:** 루트(가장 위)에 **가장 큰 값**이 위치함.
    
- **용도:** 내림차순 정렬, 점수가 높은 순서 처리.

### 동작 방식

 **데이터 삽입**

2. **맨 끝에 추가:** 새로운 데이터를 트리의 가장 마지막 자리에 넣는다
    
3. **부모와 비교 (Bubble Up):** 자신의 부모와 비교해서 내가 더 우선순위가 높다면(더 작다면) 자리를 바꾼다
    
4. **반복:** 제 자리를 찾을 때까지 위로 올라간다.


**데이터 삭제 (Pop)**

1. **루트 삭제:** 가장 위에 있는 데이터(최솟값)를 꺼낸다
    
2. **막내 이동:** 트리의 **가장 마지막 데이터**를 텅 빈 루트 자리로 올린다.
    
3. **자식과 비교 (Bubble Down):** 자식들과 비교해서 내가 더 우선순위가 낮다면(더 크다면) 자리를 바꾼다.
    
4. **반복:** 제 자리를 찾을 때까지 아래로 내려간다.


### 코드로 구현

힙은 리스트(배열)로 구현이 가능하다.

- **인덱스 규칙 (0번 인덱스부터 시작 시):**
    
    - 왼쪽 자식: `index * 2 + 1`
        
    - 오른쪽 자식: `index * 2 + 2`
        
    - 부모: `(index - 1) // 2`



``` python
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        # 막내(마지막 인덱스)부터 위로 올라가며 자리 찾기
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # 1. 루트(최솟값)를 미리 저장
        root = self.heap[0]
        # 2. 마지막 원소를 루트로 이동
        self.heap[0] = self.heap.pop()
        # 3. 위에서 아래로 내려가며 자리 찾기
        self._bubble_down(0)
        return root

    def _bubble_up(self, idx):
        # 루트에 도달할 때까지 반복
        while idx > 0:
            parent_idx = (idx - 1) // 2
            
            # 부모보다 내가 더 작으면 교체 (Swap)
            if self.heap[idx] < self.heap[parent_idx]:
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                idx = parent_idx
            else:
                break

    def _bubble_down(self, idx):
        while True:
            left_idx = idx * 2 + 1
            right_idx = idx * 2 + 2
            smallest = idx

            # 왼쪽 자식이 있고, 나보다 작다면?
            if left_idx < len(self.heap) and self.heap[left_idx] < self.heap[smallest]:
                smallest = left_idx

            # 오른쪽 자식이 있고, (현재의 최솟값)보다 작다면?
            if right_idx < len(self.heap) and self.heap[right_idx] < self.heap[smallest]:
                smallest = right_idx

            # 더 이상 바꿀 필요 없으면 종료
            if smallest == idx:
                break

            # 자리 바꾸기 (Swap)
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            idx = smallest

# --- 사용 예시 ---
h = MinHeap()
h.push(10)
h.push(5)
h.push(1) # 1이 들어오면서 5, 10을 제치고 맨 위로 올라감

print(h.pop()) # 1
print(h.pop()) # 5
print(h.pop()) # 10
```


### heapq

heapq 라이브러리를 이용하면 간단하게 구현 가능
``` python
import heapq

# 빈 리스트 생성
hq = []

# push
heapq.heappush(hq, 10)
heapq.heappush(hq, 5)
heapq.heappush(hq, 1) 

print(hq) 
# 출력: [1, 10, 5] 
# (주의: 인덱스 0번은 항상 최솟값이지만, 
#  나머지는 완벽하게 정렬된 상태가 아님!)

# pop
print(heapq.heappop(hq)) # 1
print(heapq.heappop(hq)) # 5
```