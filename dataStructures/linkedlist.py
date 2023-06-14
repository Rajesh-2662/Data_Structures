class SingleLinkedList:

    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None

        def __str__(self):
            return f'Node(data : {self.data})'

        def __repr__(self):
            return f'Node(data : {self.data})'

    def __init__(self):
        self.__head = None
        self.__tail = None

    def addAtBegin(self,data):
        new_node = self.Node(data)
        if self.isEmpty():
            self.__head = self.tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node


    def addAtLast(self,data):
        new_node = self.Node(data)
        if self.isEmpty():
            self.__head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def deleteAtBegin(self):
        if self.isEmpty():
            print("The List Is Empty There is nothing to delete")
        else:
            self.__head = self.__head.next


    def deleteAtLast(self):
        if self.isEmpty():
            print("The List Is Empty There is nothing to delete")
        else:
            if self.__head.next is None:
                self.__head = None
            else:
                current = self.__head
                while(current.next.next is not None):
                    current = current.next
                current.next = None
                self.tail = current


    def find(self,data):
        index = 0
        current = self.__head
        while (current is not None):
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def exists(self,data):
        return self.find(data) != -1


    def traversal(self):
        current = self.__head
        while(current != None):
            print(current.data,end='-->')
            current = current.next
        print()

    def isEmpty(self):
        return not bool(self.__head)

    def __str__(self):
        return self.Node.__str__()


class DoubleLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    class Node:

        def __init__(self,data):
            self.prev = None
            self.data = data
            self.next = None

        def __str__(self):
            return f'Node(data : {self.data})'

    def addAtBegin(self,data):
        new_node = self.Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def addAtLast(self,data):
        new_node = self.Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def deleteAtBegin(self):
        if self.isEmpty():
            print("There is nothing here :)")
        else:
            self.head = self.head.next
            self.head.prev = None

    def deleteAtLast(self):
        if self.isEmpty():
            print("There is Nothing here :)")
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def find(self,data):
        index = 0
        current = self.head
        while(current is not None):
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def rfind(self,data):
        index = 0
        current = self.tail
        while(current is not None):
            if current.data == data:
                return index
            current = current.prev
            index += 1
        return -1

    def exists(self,data):
        return self.find(data) != -1

    def traversal(self,reverse=False):
        if reverse:
            current = self.tail
            while(current is not None):
                print(current.data,end = '<--')
                current = current.prev

        else:
            current = self.head
            while(current is not None):
                print(current.data,end = '-->')
                current = current.next
        print()

    def isEmpty(self):
        return self.head is None
