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
    #print('head1: ',head1.data,' head2: ',head2.data)
    temp1 = head1.next
    temp2 = head2.next
    if head1.data < head2.data:
        
        while current1.next != None and current1.next.data < head2.data:
            current1 = current1.next
            #print('current1: ',current1.data,' head2: ',head2.data)
        if current1.next == None:
            temp2 = head2.next
            current1.next = head2
            head2.next = None
            head2 = temp2
        else:
            temp1 = current1.next
            temp2 = head2.next
            current1.next = head2
            head2.next = temp1
            head2 = temp2
            head = head1
    else:
        head2.next = head1
        head = head2
        head1 = head2
    head2 = temp2
    current1 = head1
    current2 = head2
    while current2 != None:
        temp1 = current1.next
        temp2 = current2.next
        while current1.next.data < current2.data:
            current1 = current1.next
            if current1.next == None:
                break
        if current1.next == None:
            current1.next = current2
        else:
            temp1 = current1.next
            temp2 = current2.next
            current1.next = current2
            current2.next = temp1
        current1 = current2
        current2 = temp2
    return head
        


if __name__ == '__main__':
