#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length -1)

    startIndex = 0
    destinationIndex = 0

    for i in range(0, length):
        if tickets[i].destination == 'NONE':
            destinationIndex = i
        elif tickets[i].source == 'NONE':
            startIndex = i
        else:
            hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
            

    route[0] = tickets[startIndex].destination
    route[-1] = tickets[destinationIndex].source

    nextIndex = 1
    nextKey = tickets[startIndex].destination
    while True:
        if nextIndex == (length -1):
            break
        nextKey = hash_table_retrieve(hashtable, nextKey)
        route[nextIndex] = nextKey
        nextIndex += 1

    return route