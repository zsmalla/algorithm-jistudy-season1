# DFS(Depth First Search)
## 개요
대표적인 그래프 탐색 알고리즘 중 하나이다. 그래프의 정점(node)를 탐색하는 방법으로, 이름 그대로 최대한 깊이 탐색한 이후, 더이상 탐색할 것이 없다면 이전으로 돌아가 탐색을 이어가는 것
- 즉, 넓게(wide) 탐색하기보다 깊게(deep) 탐색하는 방법이다.
- 단순 검색 속도 자체는 너비 우선 탐색(BFS)에 비해서 느리다.
- stack을 활용한 알고리즘, 자기 자신을 호출하는 순환(재귀) 알고리즘의 형태를 가지고 있다.
![dfs 그래프 탐색 예시](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif)

## 활용
- 모든 노드를 탐색하고자 하는 경우 단순 DFS를 활용한다.
  - DFS에서 조건을 추가해서 유효하지 않은 경우의 수를 제거하는 방법 -> [백트래킹](https://github.com/zsmalla/algorithm-jistudy-season1/blob/main/docs/chapter2/1_%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9(1)/%EC%9E%84%EC%A7%80%EC%88%98/%5B%EC%9E%84%EC%A7%80%EC%88%98%5D_%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9(1).md)
- 따라서 그래프 완전 탐색의 경우 어떤 노드를 방문했었는지 여부를 반드시 검사해야 한다.
  - 재귀 종료 조건, 무한 반복 회피
- 순열, 조합 구현에 활용

## 구현
### stack을 활용한 DFS 구현
``` python
from collections import deque # deque을 stack으로 사용

def dfs(graph, root):
  visited = []
  stack = deque()
  
  stack.append(root)
  
  while stack:
    node = stack.pop()
    
    if node not in visited:
      visited.append(node)
      stack.append(인접노드들)
      
  return visited
```
### 재귀를 통한 DFS 구현
```python
def dfs_recursive(graph, root, visited = []):
  visited.append(root)
  
  for node in graph(root):  # 인접 노드 순회
    if node not in visited:
      dfs_recursive(graph, node, visited)
  return visited
```

# BFS(Breadth First Search)
## 개요
대표적인 그래프 탐색 알고리즘 중 하나이다. 그래프의 정점(node)를 탐색하는 방법으로, 시작 정점으로부터 가까운 정점을 먼저 방문하고, 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법
- 즉, 깊게(deep) 탐색하기 전에 넓게(wide) 탐색하는 것. 
- 직관적이지 않은 면이 있다.
  - BFS는 시작 노드에서 시작해서 거리에 따라 단계별로 탐색한다고 볼 수 있다.
- queue를 활용한 반복문 형태의 알고리즘 : 선입선출(FIFO)원칙으로 탐색

![bfs 탐색 예시](https://upload.wikimedia.org/wikipedia/commons/5/5d/Breadth-First-Search-Algorithm.gif)

## 활용
- DFS와 마찬가지로 연결된 그래프를 완전탐색하는 데 활용
- depth(깊이)를 계산해야되는 문제에 활용(ex. 최단경로의 길이 = depth(깊이))
- 가중치가 같은 그래프에서 최단거리를 찾는데 활용

## 구현
```python 
def bfs(graph, root):
  from collections import deque
  queue, visited = deque(), []
  visited.append(root)
  
  while queue:
    node = queue.popleft()
    
    if node not in visited:
      visited.append(node)
      queue.append(인접 노드들)
  return visited
```