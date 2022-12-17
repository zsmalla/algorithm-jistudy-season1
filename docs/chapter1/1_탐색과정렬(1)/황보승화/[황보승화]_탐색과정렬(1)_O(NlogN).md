### ☑️ 개념 및 구현

---

<aside>
💡 **병합 정렬(Merge Sort)이란?** 전체 원소를 하나의 단위로 분할한 후 분할한 원소를 다시 병합하는 정렬 방식!

- 장점 : **안정적인** 정렬 방법이다 (데이터 분포에 영향을 덜 받는다)
- 단점 : 만약 레코드를 리스트로 구성하면, **임시 리스트**가 필요하다. 레코드들의 크기가 큰 경우에는 이동 횟수가 많아서 **시간 낭비**가 발생한다.
</aside>

### ☑️ 동작 방식

---

1. 리스트의 길이가 1 이하이면 이미 정렬된 것으로 본다.
2. 그렇지 않을 경우
    1. 분할 : 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분으로 리스트 생성한다.
    2. 정복 : 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
    3. 결합 : 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다. 이 때 정렬 결과가 임시 배열에 저장된다.
    4. 복사 : 임시 배열에 저장된 결과를 원래 배열에 복사한다.

### 💻 병합 정렬

---

```python
unsorted_list = [int(x) for x in input().split()]

def merge_sort(unsorted_list):
	# 크기가 1이면 반환
	if len(unsorted_list) <= 1:
		return unsorted_list

	# 리스트를 2분할
	mid = len(unsorted_list) // 2
	left = unsorted[:mid]
	right = unsorted[mid:]

	# 2분할한 리스트를 각각 merge sort 진행
	left_ = merge_sort(left)
	right_ = merge_sort(right)
	
	return merge(left_, right_) **# 질문? 여기서 리턴되는가?? if문에서 리턴되는거 맞지?**

def merge(left, right): **# 질문? 실행과정**
	i,j = 0,0
	sorted_list = []

	while i < len(left) and j < len(right):
		if left[i] <right[i]:
			sorted_list.append(left[i])
			i += 1
		else:
			sorted_list.append(right[i])
	
	while i < len(left):
		sorted_list.append(left[i])
		i += 1

	while j < len(right):
		sorted_list.append(right[i])
			j += 1

	return sorted_list

print(merge_sort(unsorted_list))
```

### ✅ Python 기초

---

```python
**⭐ 값 입력 받는 방법(1) - list comprehension 사용**
>>> a,b,c,d = [int(x) for x in input().split()]
- intput()을 받고 공백을 기준으로 split : ["1 2 3 4"] -> ["1","2","3","4"]
- 나온 x를 int(x)로 변환 : [1,2,3,4]
- 이때 각 리스트에 값을 순서대로 넣는다 : [a=1, b=2, c=3, d=4]

# list comprehension? 리스트를 쉽게, 짧게 한 줄로 만들 수 있는 파이썬 문법!
```

```python
**⭐ 값 입력 받는 방법(2) - map function 사용**
>>> a,b,c,d = map(int, input().split())
- intput()을 받고 공백을 기준으로 split : ["1 2 3 4"] -> ["1","2","3","4"]
- int를 통해 형변환을 해준다 : [1,2,3,4]
- map 자료구조에 해당 값을 넣어준다
- 이때 순서대로 a,b,c,d에 map의 값을 넣어준다
```

```python
**⭐ 값 입력 받는 방법(3) - List comprehension with stdion stdout 사용
# 가장 빠른 방법!**
>>> from sys import stdin, stdout
>>> a,b,c,d = [int(x) for x in stdin.readline().rstrip().split()]
>>> stdout.write(str(a*b*c*d)+'\n')
- list compreshension을 쓰는 것을 같고 코드에서 stdin, stdout을 쓰는 차이
```

---
### ☑️ 개념 및 구현

---

<aside>
💡 **힙이란?** 최소값 또는 최대값을 빠르게 찾아내기 위해 완9전이진트리 형태로 만들어진 자료구조!

(조건 : 부모 노드는 항상 자식 노드보다 우선순위가 높다!)

→ 루트 노드(root node)는 항상 우선순위가 높은 노드!

- 힙 자료구조
    1. **최대힙** : 부모 노드의 값(key값) ≥ 자식 노드의 값(key값)
    2. **최소힙** : 부모 노드의 값(key값) ≤ 자식 노드의 값 (key값) 
    
- 특징 (**노드 인덱스**) - 배열로 구현 시 1번째 인덱스에서부터 시작!
    - 왼쪽 자식 노드 인덱스 = 부모 노드 인덱스 * 2 + 1
    - 오른쪽 자식 노드 인덱스 = 부모 노드 인덱스 * 2 + 2
    - 부모 노드 인덱스 = (자식 노드 인덱스 -1) / 2
</aside>

### ☑️ 동작 방식

---

```python
**⭐ heapq 라이브러리**
- heapq.heappush() : 힙에서 원소를 삽입할 때
- heapq.heappop() : 힙에서 원소를 꺼낼 때 항상 가장 작은 원소를 꺼낸다.
```

### 💻 힙 삽입/삭제 코드(1) - 오름차순(최소힙)

---

```python
# heapq 라이브러리 사용
import heapq

def heapsort(iterable):
    h = []
    result = []
    
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value) **# heapq.heappush() : 힙에서 원소를 삽입할 때**
        
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h)) **# heapq.heappop() : 합에서 원소를 꺼낼 때 항상 가장 작은 원소를 꺼낸다.**
        
    return result
    
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 💻 힙 삽입/삭제 코드(1) - 내림차순(최대힙)

---

```python
import heapq

def heapsortDesc(iterable):
    h = []
    result = []
    
    **# 모든 원소를 차례대로 힙에 삽입(부호를 변경하여)**
    for value in iterable:
        heapq.heappush(h, **-value**)
        
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(**-heapq.heappop(h)**)
        
    return result
    
result = heapsortDesc([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```