# class MyQueue(object):

#     def __init__(self):
#         self.stack = []
        

#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         self.stack.append(x)
        

#     def pop(self):
#         """
#         :rtype: int
#         """
#         if self.stack:
#             self.stack.pop(0)
        

#     def peek(self):
#         """
#         :rtype: int
#         """
#         self.stack[0]
        

#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return len(self.stack)==0

class MyQueue(object):

    def __init__(self):
        self.input_stack = []
        self.output_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input_stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        if self.output_stack:
            return self.output_stack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.input_stack)==0 and len(self.output_stack) == 0


s = MyQueue()
s.push(1)
s.push(2)
s.peek()
s.pop()
s.empty()
