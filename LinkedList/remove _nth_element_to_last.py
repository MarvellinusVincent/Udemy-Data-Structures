from linked_lists_class import LinkedList

def nthToLast(list, n):
    pointer1 = list.head
    pointer2 = list.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1