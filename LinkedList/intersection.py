from pandas import value_counts
from linked_lists_class import LinkedList, Node

def intersection(list1, list2):
    if list1.tail is not list2.tail:
        return False
    
    len1 = len(list1)
    len2 = len(list2)

    shorter = list1 if len1 < len2 else list2
    longer = list2 if len1 < len2 else list1

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode  = longerNode.next
    
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode - longerNode.next
    
    return longerNode

def add(list1, list2, value):
    tempNode = Node(value)
    list1.tail.next = tempNode
    list1.tail = tempNode
    list2.tail.next = tempNode
    list2.tail = tempNode
    