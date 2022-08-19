from linked_lists_class import LinkedList

def sumlists(list1, list2):
    temp1 = list1.head
    temp2 = list2.head
    carry = 0
    sum = LinkedList()

    while temp1 or temp2 or carry:
        res = carry
        if temp1:
            res += temp1.value
            temp1 = temp1.next
        if temp2:
            res += temp2.value
            temp = temp2.next
        sum.add(int(res % 10))
        carry = res / 10
    
    return sum

