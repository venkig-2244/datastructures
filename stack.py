class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Accepts an item as a parameter and appends it to the end of the list.
        reutrns Nothing
        :param item:
        :return:

        The run time for this method is O(1) or constant time, because it appends an item to the end of the list.
        """
        self.items.append(item)

    def pop(self):
        """
        Removes the last item form the list which is also the top item of the stack.

        :return:
        The run time for this is O(1).
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """
        The method returns the last item in the list, which is also the top item of the Stack
        :return:

        The run time for this function is O(1)
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
        The method returns the number of items in the list.
        :return:
        The run time for this function is O(1)
        """
        return len(self.items)

    def is_empty(self):
        """
        Returns True if the Stack is empty, otherwise returns False.
        :return:
        The run time for this function is O(1)
        """
        if self.items:
            return False

        return True



