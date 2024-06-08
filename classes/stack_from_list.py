class stack():

    def __init__(self):
        self.stack_list = []

    def push(self, value):
        list_stack = self.stack_list
        list_stack.append(value)

    def pop(self):
        list_stack = self.stack_list
        removing = list_stack[-1]
        self.stack_list = self.stack_list[:-1]
        print(removing)

    def print_stack(self):
        print(self.stack_list)


my_stack = stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.print_stack()
my_stack.pop()
my_stack.print_stack()
