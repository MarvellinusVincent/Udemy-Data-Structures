from linked_lists_class import LinkedList

def removeDups(list):
    if list.head is None:
        return
    else:
        current = list.head
        visited = set([current.value])
        while current:
            if current.value in visited:
                current = current.next
            else:
                visited.add(current.next.value)
                current = current.next
        return list

test = LinkedList()
test.generate(10, 0, 99)
print(test)
removeDups(test)
print(test)