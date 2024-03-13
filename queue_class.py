# queue_class.py ------------------------------------------------------------------------------------------------------------------------

# class Queue definition
class Queue:
    def __init__(self):
        self.items = []

    # Add item to the rear of the queue.
    def enqueue(self, item):
        self.items.insert(0, item)

    # Remove and return the front item from the queue.
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Queue is empty.")
            return None

    # Check if the queue is empty.
    def is_empty(self):
        return len(self.items) == 0

    # Return the number of items in the queue.
    def size(self):
        return len(self.items)

    # Return the front item in the queue without removing it.
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Queue is empty.")
            return None

# Dictionary to store quiz questions and options
quiz_questions = {
    "RAF People": [
        ("Who is CAS?", ("Rich Knighton", "Mike Andrews")),
        ("Who is Air + Space Cdr?", ("Harv Smyth", "Jane Doe")),
        ("Who is DCAS?", ("Paul Lloyd", "Alice Johnson")),
        ("Who is AOC 22 Gp?", ("Cab Townsend", "Tom Brown")),
        ("Who is WO RAF?", ("Subby Subramanium", "Chris Wilson")),
    ],
    "Pilot Questions": [
        ("What is the opposite of North?", ("South", "East")),
        ("Do you need polarised or unpolarised sunglasses?", ("Unpolarised", "Polarised")),
        ("What is the name of the RAF's jet trainer?", ("Hawk", "Tornado")),
        ("What is mach?", ("Speed of Sound", "Light Speed")),
        ("What is the nickname of the RAFAT?", ("Red Arrows", "Blue Angels")),
    ],
    "RAF Knowledge": [
        ("What does RAF stand for?", ("Royal Air Force", "Royal Army Force")),
        ("When was the RAF founded?", ("1918", "1945")),
        ("How many RAF groups are there?", ("5", "3")),
        ("What group is RAF training?", ("22 Gp", "15 Gp")),
        ("True or False. The RAF is the world's first independent Air Force?", ("True", "False")),
    ],
}

# Example usage of the Queue class
q = Queue()
for category, questions_and_options in quiz_questions.items():
    for question, options in questions_and_options:
        q.enqueue((category, question, options))

# Example usage:
print("Queue size:", q.size())  # Output: 15
print("Front item:", q.peek())  # Output: ("RAF People", "Who is CAS?", ("Rich Knighton", "Mike Andrews"))
print("Dequeue:", q.dequeue())  # Output: ("RAF People", "Who is CAS?", ("Rich Knighton", "Mike Andrews"))
print("Queue size after dequeue:", q.size())  # Output: 14
