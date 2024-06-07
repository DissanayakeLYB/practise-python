class stack():

    def __init__(self):
        self.stack_of_balls = []

    def push(self, value):
        list_stack = self.stack_of_balls
        list_stack.append(value)

    def pop(self):
        list_stack = self.stack_of_balls
        removing = list_stack[-1]
        self.stack_of_balls = self.stack_of_balls[:-1]
        print(removing)

    def print_stack(self):
        print(self.stack_of_balls)


my_stack = stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(2)
my_stack.push(2)
my_stack.print_stack()
my_stack.pop()
my_stack.print_stack()
