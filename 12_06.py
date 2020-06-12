# PROBLEM STATEMENT -  Design a data structure that supports all following operations in average O(1) time.
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []
        self.contained_items = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.contained_items: return False
        self.contained_items[val] = len(self.items)
        self.items.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.contained_items: return False
        index = self.contained_items[val]
        del self.contained_items[val]

        if index != len(self.items) - 1:
            self.contained_items[self.items[-1]] = index
            self.items[index], self.items[-1] = self.items[-1], self.items[index]
        self.items.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.items[int(random.random() * len(self.items))]