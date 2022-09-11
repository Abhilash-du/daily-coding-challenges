# Problem Description Design and implement a Linked List data structure. A node in a linked list should have the
# following attributes - an integer value and a pointer to the next node. It should support the following operations:
#
# insert_node(position, value) - To insert the input value at the given position in the linked list.
# delete_node(position) - Delete the value at the given position from the linked list.
# print_ll() - Print the entire linked list, such that each element is followed by a single space.
# Note:
#
# If an input position does not satisfy the constraint, no action is required.
# Each print query has to be executed in a new line.
#
#
# Problem Constraints
# 1 <= value <= 105
# 1 <= position <= n where, n is the size of the linked-list.
#
#
#
# Input Format
# First line contains an integer denoting number of cases, let's say t.
# Next t line denotes the cases.
#
#
# Output Format When there is a case of print_ll(),  Print the entire linked list, such that each element is followed
# by a single space. NOTE: You don't need to return anything.
#
#
# Example Input
# 5
# i 1 23
# i 2 24
# p
# d 1
# p
#
#
# Example Output
# 23 24
# 24
#
#
# Example Explanation
# After first two cases linked list contains two elements 23 and 24.
# At third case print: 23 24.
# At fourth case delete value at first position, only one element left 24.
# At fifth case print: 24.

head = None


class Node:
    data = None
    next = None

    def __init__(self, data=data, next=None):
        self.data = data
        self.next = next


class Head:
    def __init__(self, head_node):
        global head
        head = head_node


def insert_node(position, value):
    new_node = Node(value)
    current_node = head
    if position == 1:
        new_node.next = head  # if position is 1 means it will be the head node
        Head(new_node)
    else:
        for i in range(position - 2):  # reaches till position-1
            current_node = current_node.next
        if current_node.next is not None:
            new_node.next = current_node.next  # new node's next will be same as previous node's next
        current_node.next = new_node  # node at position(p-1)'s next will now point to new node


def delete_node(position):
    global head
    if position == 1:
        head = head.next
    else:
        current_node = head
        curr_position = 0
        while current_node.next is not None:  # iterating till we find the previous position of deleting position
            if curr_position == position - 2:  # if node reaches till position-1
                current_node.next = current_node.next.next  # the link to the position needs to be removed
                return
            else:
                current_node = current_node.next
                curr_position += 1
        return


def print_ll():
    if head is None:
        return None
    current_node = head
    while current_node.next is not None:  # iterating till the next element is null (till last element)
        print(current_node.data, end=" ")
        current_node = current_node.next
    print(current_node.data)

# Approach Followed/Observation:-
# We will maintain the head of the LinkedList.
#
# For Insert operation - Firstly, we will traverse the list and keep two pointers, current and previous. So if the
# position is 1, we will add the node in the beginning and update the head. Otherwise, we will traverse the list up
# to the desired position and add the node by making the current node, the next node of the newly added node,
# and the next node of the previous node will be the newly added node.
#
# For Print LinkedList Operation - We will print the data of all the nodes by traversing through the list and stop
# when our current pointer becomes null.
#
# For Delete LinkedList Operation - We will traverse the list up to the desired position and keep track of two
# pointers, current and previous. If the position is 1, we will make the new head of the list the next element of the
# last head. Otherwise, make the next element of the previous node the next element of the current node. At last,
# free the pointer of the current node.

# For execution/Test you can execute below:-
# insert_node(1, 4998)
# insert_node(2, 6629)
# insert_node(3, 7976)
# insert_node(4, 1445)
# insert_node(5, 6573)
# insert_node(6, 6416)
# insert_node(7, 2528)
# insert_node(8, 6208)
# insert_node(9, 7871)
# insert_node(10, 8738)
# insert_node(11, 9468)
# insert_node(12, 7983)
# insert_node(13, 6477)
# insert_node(14, 1214)
# insert_node(15, 8468)
# insert_node(16, 4793)
# insert_node(17, 5687)
# insert_node(18, 7074)
# insert_node(19, 430)
# insert_node(20, 3310)
# insert_node(21, 4005)
# insert_node(22, 3848)
# insert_node(23, 6598)
# insert_node(24, 2184)
# insert_node(25, 5350)
# insert_node(26, 201)
# insert_node(27, 952)
# insert_node(28, 2842)
# insert_node(29, 3564)
# insert_node(30, 8239)
# insert_node(31, 6513)
# insert_node(32, 6310)
# insert_node(33, 2195)
# insert_node(34, 4645)
# insert_node(35, 4237)
# insert_node(36, 4763)
# insert_node(37, 3786)
# insert_node(38, 1331)
# insert_node(39, 644)
# insert_node(40, 7022)
# insert_node(41, 4055)
# insert_node(42, 5940)
# insert_node(43, 7777)
# insert_node(44, 9343)
# insert_node(45, 5284)
# insert_node(46, 7284)
# insert_node(47, 9061)
# insert_node(48, 6201)
# insert_node(49, 4987)
# insert_node(50, 3808)
# insert_node(51, 8755)
# insert_node(52, 6335)
# insert_node(53, 2478)
# insert_node(54, 8615)
# insert_node(55, 4455)
# insert_node(56, 4466)
# insert_node(57, 4290)
# insert_node(58, 7744)
# insert_node(59, 5193)
# insert_node(60, 2801)
# insert_node(61, 3705)
# insert_node(62, 8208)
# insert_node(63, 7357)
# insert_node(64, 785)
# insert_node(65, 9765)
# insert_node(66, 7857)
# insert_node(67, 5365)
# insert_node(68, 5535)
# insert_node(69, 9190)
# insert_node(70, 8728)
# insert_node(71, 4598)
# insert_node(72, 242)
# insert_node(73, 8917)
# insert_node(74, 9501)
# insert_node(75, 6524)
# insert_node(76, 6305)
# insert_node(77, 5566)
# insert_node(78, 7105)
# insert_node(79, 3865)
# insert_node(80, 9204)
# insert_node(81, 6068)
# insert_node(82, 6423)
# insert_node(83, 2371)
# insert_node(84, 3519)
# insert_node(85, 4510)
# insert_node(86, 5354)
# insert_node(87, 9899)
# insert_node(88, 407)
# insert_node(89, 530)
# insert_node(90, 9102)
# insert_node(91, 8426)
# insert_node(92, 3926)
# insert_node(93, 686)
# insert_node(94, 8645)
# insert_node(95, 2445)
# insert_node(96, 2226)
# insert_node(97, 5199)
# insert_node(98, 1892)
# insert_node(99, 5012)
# insert_node(100, 9844)
# insert_node(24, 7114)
# delete_node(5)
# print_ll()
