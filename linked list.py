class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_the_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_the_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next

            itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_the_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        elif index == 0:
            self.head = self.head.next
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        elif index == 0:
            self.head = self.head.next
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1

    def print(self):
        if self.head == None:
            print("Linked list is empty")
            return
        else:
            itr = self.head
            llstr = ''
            while itr:
                llstr = llstr + str(itr.data) + '--->'
                itr = itr.next
            print(llstr)


if __name__ == '__main__':
    ll = linkedlist()
    ll.insert_at_the_begining(89)
    ll.insert_at_the_begining(9)
    ll.insert_at_the_end(34)
    ll.insert_at_the_end(4)
    ll.insert_values(['banana', 'strawberry', 'apple', 'mango'])
    ll.print()
    print(ll.get_length())
    ll.remove_at(2)
    ll.print()
    ll.insert_at(2, 'jackfruit')
    ll.print()