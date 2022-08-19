from linked_lists_class import LinkedList

def partition(list, x):
    temp = list.head
    list.tail = list.head

    while temp:
        nextNode = temp.next
        temp.next = None
        if temp.value < x:
            temp.next = list.head
            list.head = temp
        else:
            list.tail.next = temp
            list.tail = temp
        temp = nextNode
    
    if list.tail.next is not None:
        list.tail.next