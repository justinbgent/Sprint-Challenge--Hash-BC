#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)

    for i in range(0, length):
        key = limit - weights[i]
        value = hash_table_retrieve(ht, key)
        if value:
            if i != value:
                return (value, i)

    #for i in range(0, length):
    #    for j in range(i + 1, length):
    #        if weights[i] + weights[j] == limit:
    #            return (j, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
