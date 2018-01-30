
#!python

from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        self.size = 0
        # set elememts to be hashtables
        self.elements = HashTable()
        # if elements is not None:
        #     for i in elements:
        #         self.append(i)

    ''' or use size property to use this function as property '''
    # @property
    # def sizd(self):
    #     return self.elements.size

    # return a boolean indicating whether element is in this set
    def contains(self, element):
        # check if the element is in the set
        if self.elements.contains(element):
            return True
        return False

    # add element to this set, if not present already
    def add(self, element):
        # get buckets of the set
        hashtable = self.elements
        # check if the key of the bucket exist, if not, add element to hashtable and plus size
        if not self.contains(element):
            self.size += 1
            # key of hashtable is the element of set
            hashtable.set(element, None)
        else:
            raise ValueError("element not in set")


    # remove element from this set, if present, or else raise KeyError
    def remove(self, element):
        # get index of the hashtable
        if element not in self.elements.keys():
            raise ValueError("element not in set")
        else:
            self.size -= 1
            # use hashtable function to delete element, which is the key of hashtable
            self.elements.delete(element)

    # return a new set that is the union of this set and other_set
    def union(self, other_set):
        for k in other_set.elements.keys():
            # self.add(k)
            self.elements.set(k, None)
        return self

    # return a new set that is the intersection of this set and other_set
    # loop through shorter set and use contain inside of for loop to reduce run time to the length of linkedlist
    def intersection(self, other_set):
        interset = Set()
        len_self = self.elements.length()
        len_other = other_set.elements.length()
        if len_self < len_other:
            # check if other set contain the key in self set keys
            for k in self.elements.keys():
                if other_set.elements.contains(k):
                    # add the key to new set
                    interset.add(k)
        else:
            for k in other_set.elements.keys():
                if self.elements.contains(k):
                    interset.add(k)
        return interset

    # return a new set that is the difference of this set and other_set
    def difference(self, other_set):
        diff_set = Set()
        # add key that's in self but not in other set
        for k in self.elements.keys():
            if not other_set.elements.contains(k):
                diff_set.add(k)
        # add key that's in other but not in self set
        for k in other_set.elements.keys():
            if not self.elements.contains(k):
                diff_set.add(k)
        return diff_set

    # return a boolean indicating whether other_set is a subset of this set
    def is_subset(self, other_set):
        for k in other_set.elements.keys():
            # if find a k of other set not in self, the subset not exist
            if not self.elements.contains(k):
                return False
        return True

def test_set():
    new_set = Set()
    new_set.add("a")
    new_set.add("b")
    new_set.contains("b")
    other_set = Set()
    other_set.add("you")
    other_set.add("a")
    test_union = new_set.union(other_set)
    test_inter = new_set.intersection(other_set)
    print(new_set.elements)
    print(other_set.elements)
    print(test_union.elements, test_inter.elements)

if __name__ == '__main__':
    test_set()

