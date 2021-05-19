# Singly Linked List Insertions

> The linked list is alternative to an array-based structure. A linked list is collection of nodes that collectively form linear sequence. In a singly linked list, each node stores a reference to an object that is an element of the sequence, as well as a reference to the next node of the list. It does not store any pointer or reference to the previous node. To store a single linked list, only the reference or pointer to the first node in that list must be stored. The last node in a single linked list points to nothing.

## Challenge Description

1. Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node. Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created. 

2. Create methods in the LinkedList class : 


## Approach & Efficiency
1. *Create a class that creats a node with a next pointer property.*
2. *Create a class called linked_list that contains five methods.*
3. *Create an initialization method to set the head node.*
4. *Create a method to append a value in the last node.*
5. *Create a method to represent a class object as a string.*
6. *Create a method to add an node to the list.*
7. *Create a method to check if an element if exists in the list and returns a boolean (True/Flase).*
8. *Checked for any bugs/errors using unit testing.*
9. *Worked perfictly.*

## API

![img](https://github.com/abdalazzezzalsalahat/data-structures-and-algorithms/blob/main/python/linked_list/assets/Linked-List.png)


## Challenge


1. append(value) which adds a new node with the given value to the end of the list

2. insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value 

3. insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node

## Approach & Efficiency

* `space <- O(1)`
* `time  <- O(n)`

## API

> `append(value)` function  : which adds a new node with the given value to the end of the list

> `insertBefore(value, newVal)` function :  which add a new node with the given newValue immediately before the first value 

> `insertAfter(value, newVal)` function :  which add a new node with the given newValue immediately after the first value node

## Whiteboard

![img](https://github.com/abdalazzezzalsalahat/data-structures-and-algorithms/blob/main/python/linked_list/assets/Linked-List-BA.png)




## Challenge

1. kth_from_end(self, k) which takes in a value(k) and returns the Node k places away from the tail


## Approach & Efficiency

* `space <- O(1)`
* `time  <- O(n)`

## API

> `kth_from_end(self, k)` function  : which takes in a value(k) and returns the Node k places away from the tail

## Whiteboard

![img](https://github.com/abdalazzezzalsalahat/data-structures-and-algorithms/blob/main/python/linked_list/assets/Linked-List-kth.png)








## Challenge

1. Write function (zipLists) that takes two linked lists as arguments (list1,list2). Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.


## Approach & Efficiency

* `space <- O(1)`
* `time  <- O(n)`

## API

> `zipLists (list1,list2)` function : takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.

## Whiteboard

![img](https://github.com/abdalazzezzalsalahat/data-structures-and-algorithms/blob/main/python/linked_list/assets/Linked-List-ZIP.png)

