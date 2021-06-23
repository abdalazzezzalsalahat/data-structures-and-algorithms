# Left-Join CC 33
##  Problem domain
> This challenge asks us to write a function that takes two hash tables as arguements and returns a list of the joined key/values. If there is no match in the second hash table for a given key, the list will include None for as the value joined from the 2nd hash table.

## Challenge
> Iterate through the entire 1st hash table (the left table) and when an element is found, check if that element's key exists in the second hash table. If it does, append (key, value_1, value_2) if it does not append (key, value_1, None).


## Approach & Efficiency
- Space --- O(n)
- Time --- O(n)

## White-Board

![img](../assets/hash_left_join.png)


