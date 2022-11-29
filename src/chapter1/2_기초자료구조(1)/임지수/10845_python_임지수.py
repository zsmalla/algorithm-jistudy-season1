import sys
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.lst = list()

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        return self.lst.pop(0) if self.lst else -1

    def size(self):
        return len(self.lst)

    def empty(self):
        return 1 if not self.lst else 0

    def front(self):
        return self.lst[0] if self.lst else -1

    def back(self):
        return self.lst[-1] if self.lst else -1

def main():
    N = int(input())
    queue = Queue()
    for _ in range(N):
        command = input().split()
        if command[0] == 'push':
            queue.push(int(command[1]))
        elif command[0] == 'front':
            print(queue.front())
        elif command[0] == 'back':
            print(queue.back())
        elif command[0] == 'size':
            print(queue.size())
        elif command[0] == 'empty':
            print(queue.empty())
        elif command[0] == 'pop':
            print(queue.pop())

if __name__ == '__main__':
    main()