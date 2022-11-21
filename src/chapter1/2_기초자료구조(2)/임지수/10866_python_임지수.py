import sys
input = sys.stdin.readline

class Deque:
    def __init__(self):
        self.deque = list()
    def push_front(self, item):
        self.deque.insert(0, item)
    def push_back(self, item):
        self.deque.append(item)
    def pop_front(self):
        return self.deque.pop(0) if self.deque else -1
    def pop_back(self):
        return self.deque.pop(-1) if self.deque else -1
    def size(self):
        return len(self.deque)
    def empty(self):
        return 1 if not self.deque else 0
    def front(self):
        return self.deque[0] if self.deque else -1
    def back(self):
        return self.deque[-1] if self.deque else -1

def main():
    deque = Deque()
    N = int(input())
    for _ in range(N):
        command = input().split()
        if len(command) == 2:
            exec(f'deque.{command[0]}({command[1]})')
        else:
            exec(f'print(deque.{command[0]}())')

if __name__ == '__main__':
    main()