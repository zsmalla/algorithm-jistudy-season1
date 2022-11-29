import sys
input = sys.stdin.readline
class Stack:
    def __init__(self):
        self.lst = list()

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        return self.lst.pop(-1) if self.lst else -1

    def size(self):
        return len(self.lst)

    def empty(self):
        return 1 if not self.lst else 0

    def top(self):
        return self.lst[-1] if self.lst else -1

def main():
    N = int(input().rstrip())
    stack = Stack()

    for _ in range(N):
        command = input().split()

        if command[0] == 'push':
            stack.push(int(command[1]))
        elif command[0] == 'pop':
            print(stack.pop())
        elif command[0] == 'size':
            print(stack.size())
        elif command[0] == 'empty':
            print(stack.empty())
        elif command[0] == 'top':
            print(stack.top())

if __name__ == '__main__':
    main()
