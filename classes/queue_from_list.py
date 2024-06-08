class queue():

    def __init__(self):
        self.queue_list = []

    def enqueue(self, value):
        queue_list = self.queue_list
        queue_list.append(value)

    def dequeue(self):
        queue_list = self.queue_list
        queue_list.pop(0)
        self.queue_list = queue_list

    def print_queue(self):
        print(self.queue_list)


my_queue = queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()
