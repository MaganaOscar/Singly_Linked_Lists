class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self
    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = new_node
        return self
    def remove_from_front(self):
        self.head = self.head.next
        return self
    def remove_from_back(self):
        runner = self.head
        while runner.next.next != None:
            runner = runner.next
        runner.next = None
        return self
    def remove_val(self, val):
        if val == self.head.value:
            self.remove_from_front()
        else:
            runner = self.head
            while runner.next.value != val and runner.next.next != None:
                runner = runner.next
            if runner.next.value == val:
                runner.next = runner.next.next
        return self
    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
        else:
            index = 0
            new_node = SLNode(val)
            runner = self.head
            while index < n - 1:
                if runner.next != None:
                    runner = runner.next
                index += 1
            new_node.next  = runner.next
            runner.next = new_node
        return self

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()

my_list.remove_from_front().print_values()
my_list.add_to_front("Linked Lists").print_values()
my_list.remove_from_back().print_values()
my_list.add_to_back("fun!").print_values()
my_list.add_to_back("ish").print_values()
my_list.remove_val('ar').print_values()
my_list.insert_at('hello', 6).print_values()