
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Стек порожній!")
            return None

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Стек порожній!")
            return None

        return self.items[-1]

    def clear(self):
        self.items.clear()

    def count(self):
        return len(self.items)

    def size(self):
        return len(self.items)

    def toString(self):
        if self.is_empty():
            return "Стек порожній"

        return " -> ".join(str(item) for item in reversed(self.items))

    def is_empty(self):
        return len(self.items) == 0

stack = Stack()

print("Додаємо елементи: 10, 20, 30")
stack.push(10)
stack.push(20)
stack.push(30)

print("Вміст стеку:", stack.toString())
print("Верхній елемент:", stack.peek())
print("Кількість елементів (count):", stack.count())
print("Розмір стеку (size):", stack.size())

print("\nВидаляємо верхній елемент:", stack.pop())
print("Стек після видалення:", stack.toString())

stack.push(40)
print("\nДодаємо 40:", stack.toString())

print("\nОчищуємо стек...")
stack.clear()
print("Стек після очищення:", stack.toString())
print("Кількість елементів:", stack.count())
