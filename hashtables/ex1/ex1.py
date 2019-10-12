#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
   # Insert all weights into hashtable (key - hashweight : value - index)
    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)
   # Search for two keys that sum to limit
    for i in range(0, length):
        result = hash_table_retrieve(ht, (limit - weights[i]))
        if result is not None:
            if result > i:
                tuple = (result, i)
            else:
                tuple = (i, result)
            return tuple
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
