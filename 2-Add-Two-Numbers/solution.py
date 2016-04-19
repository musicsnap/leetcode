class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll1 = LinkedList()
        ll1.initFromLeet(l1)

        ll2 = LinkedList()
        ll2.initFromLeet(l2)

        list1 = ll1.toList()
        list2 = ll2.toList()

        carry = False
        result = LinkedList()
        for i in range(len(list1) if len(list1) > len(list2) else len(list2) ):
            A1 = ll1[i]
            if A1 == None:
                A1 = 0
            else:
                A1 = A1.val

            A2 = ll2[i]
            if A2 == None:
                A2 = 0
            else:
                A2 = A2.val

            num =  A1  + A2
            if carry == True: num += 1
            if 9 < num:
                carry = True
                result.append(num%10)
            else:
                carry = False
                result.append(num)
        if True == carry:
            result.append(1)
        return result.toLeetResult()

        
class LinkedList(object):

    def __init__(self):
        self.head = ListNode(0) #带有头结点的链表
        self.tail = self.head
        self.len = 0

    def __getitem__(self, key):
        if key < 0:
            return None
        elif key - 1 > self.len:
            return None
        else: 
            pointer= self.head.next
            while key > 0:
                key -= 1
                next = pointer.next
                if None != next:
                    pointer = pointer.next
                else:
                    return None
            return pointer

                
    def __setitem__(self, key, value):
        if key < 0 or key > self.len: #小于零或者大于长度
            print "key range error"
            return False
        elif key == self.len:
            self.append(value)
        else:
            self.change(key,value)

    def clear(self):
        self.__init__()
        self.len = 0
        pass

    def initFromList(self, lst):
        self.clear()
        for a in lst:
            self.append(a)

    def append(self, value):
        self.len += 1
        node = ListNode(value)
        self.tail.next = node
        self.tail = node
        return True

    def toList(self):
        l = []
        for a in range(self.len):
            l.append(self.__getitem__(a).val)
        return l

    def getLen(self):
        pass

    def insert(self, index, value):
        pass

    def delete(self, index):
        self.len -= 1
        pass

    def change(self, index, value):
        node = self.__getitem__(index)
        if None != node:
            node.val = value
        else:
            return False
        pass

    def index(self, value):
        for a in range(self.len):
            node = self.__getitem__(a)
            if node != None and value == node.val:
                return a
        return None
    
    def loop(self):
        pointer = self.head.next
        while pointer != None:
            print pointer.val
            pointer = pointer.next

    def revert(self):
        for a in range(self.len / 2):
            print self.len - a - 1, a
            self.__getitem__(a).val, self.__getitem__(self.len - a -1).val = self.__getitem__(self.len - a -1).val, self.__getitem__(a).val

    def initFromLeet(self, ll):
        pointer = ll
        while None != pointer:
            self.append(pointer.val)
            pointer = pointer.next

    def toLeetResult(self):
        head = None
        tail = None
        for i in range(self.len):
            if 0 == i:
                head = ListNode(self.__getitem__(i).val) 
                tail = head  
            else:
                item = ListNode(self.__getitem__(i).val)
                tail.next = item
                tail = item
        return head
