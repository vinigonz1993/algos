# Animal SheltenAn animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat.You may use the built-in LinkedLis t data structure.


from stack import Stack

class CustomStack(Stack):

    def __init__(self):
        self.items = []
        self.items_dequeued = []

    def row(self, stack, item):
        return f'{stack.index(item)} - {item["type"]} -> Age: {item["age"]}'

    def display(self):
        print("Queued:")
        for item in self.items:
            print(self.row(self.items, item))

    def display_dequeued(self):
        print(f"Dequeued:")
        for item in self.items_dequeued:
            print(self.row(self.items_dequeued, item))

    def queue(self, type):
        tmp_stack = []

        while self.items:
            current_value = self.items.pop()
            while tmp_stack and current_value["type"] == type and tmp_stack[-1]["age"] < current_value["age"]:
                self.items.append(tmp_stack.pop())

            tmp_stack.append(current_value)

        while tmp_stack:
            self.items.append(tmp_stack.pop())

    def dequeue(self, type):
        self.queue(type=type)

        current_value = self.items.pop()

        if current_value["type"] == type:
            self.items_dequeued.append(self.items.pop())
            return True
        else:
            return False

    def is_empty(self):
        return len(self.items) == 0


animals = [
    {"type": "cat", "age": 2},
    {"type": "cat", "age": 5},
    {"type": "cat", "age": 6},
    {"type": "cat", "age": 7},
    {"type": "cat", "age": 9},
    {"type": "dog", "age": 3},
    {"type": "dog", "age": 3},
    {"type": "dog", "age": 4},
    {"type": "dog", "age": 9}
]

stack = CustomStack()

for animal in animals:
    stack.push(animal)

stack.display()

animal_type = str(input("Do you want a 'dog' or a 'cat'? "))
total_animals = int(input("How many animals do you want to dequeue? "))

total_dequeued = 0

while total_animals > total_dequeued and not stack.is_empty():
    continue_dequeue = stack.dequeue(type=animal_type)

    if not continue_dequeue:
        break

    total_dequeued += 1

stack.display_dequeued()
