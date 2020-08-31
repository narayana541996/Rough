#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    current1 = head1
    current2 = head2
    #temp1 = current1.next
    #temp2 = current2.next
    le1 = 0
    le2 = 0
    while current1 != None:
        le1 += 1
        current1 = current1.next
    while current2 != None:
        le2 += 1
        current2 = current2.next
    if le1 >= le2:
        length = le1
    else:
        length = le2
    print('length: ',length)
    l1 = []
    i = 0
    current1 = head1
    current2 = head2
    while i <= (le1+le2):

        if current2 == None and current1 != None:
            l1.append(current1)
            current1 = current1.next
            continue
        elif current2 != None and current1 == None:
            l1.append(current2)
            current2 = current2.next
            continue
        if current1 != None and current1.data < current2.data:
            #if current1 != None:
            print('current1: ',current1.data)
            l1.append(current1)
            current1 = current1.next

        elif current2 != None and current2.data <= current1.data:
            #if current2 != None:
            print('current2: ',current2.data)
            l1.append(current2)
            if current2 != None:
                current2 = current2.next
        
        i += 1
    print(' l1: ', len(l1))
    i = 0
    while i < (len(l1)-1):
        print('i: ',i,' l1[i].data: ', l1[i].data)
        l1[i].next = l1[i+1]
        i += 1
    l1[-1].next = None

    return l1[0]


if __name__ == '__main__':
