class LinkNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkList:
    def __init__(self):
        self.head = LinkNode()

    def add(self, val):
        new_node = LinkNode(val)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def print(self):
        print_lost = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            print_lost.append(cur.val)
        return print_lost

    def len(self):
        count = 0
        cur = self.head
        while cur.next is not None:
            count += 1
            cur = cur.next

        return count


ll = LinkList()

ll.add(1)
ll.add(2)
ll.add(3)

print(ll.len())
print(ll.print())
