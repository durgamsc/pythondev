class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def add_node(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top

            self.top = new_node

        self.height += 1


    def print(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


stack1 = Stack(1)
stack1.add_node(2)
stack1.add_node(3)
stack1.add_node(4)
stack1.print()
