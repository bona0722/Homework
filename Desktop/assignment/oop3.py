import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other:             # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other:                # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            if not x in self.data:     # Removes duplicates
                self.data.append(x)

    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:
    

    def issubset(self, other): #<=, <
        if self.data != other.data:
            if self.intersection(other).data == self.data: return self.intersection(other) and self.data
            else: return False
        else: return self.intersection(other).data and self.data

    
    def issuperset(self, other): #>=, >, |=
        if self.data != other.data:
            if self.intersection(other).data == other.data: return self.intersection(other).data or other.data
            else: return self.union(other).data or other.data
        else: return self.data or other.data


    def intersection_update(self, other): #&=
        self = self.intersection(other)
        return self
         
    def difference_update(self, other): #-=
        for i in range(len(self.union(other).data)):
            if self.intersection(other).data in self.intersection(other).data[i]:
                del self.intersection(other).data[i]
        return self
        
        
    #def symmetric_difference_update(self, other):
   
    # def add(self, elem):
    #     self.elem = elem
    #     self = self.concat(self.elem)
    #     return self

    # def remove(self, elem): 
    #     try:
    #         for i in self:
    #             if i == elem : 

if __name__ == "__main__":
    x = Set([1,3,5,7, 1, 3])
    y = Set([2,1,4,5,6])

    test(Set([1,2,3]).issubset(Set([1,2,3])) == [1,2,3]) 
    test(Set([1,2]).issubset(Set([1,2,3,4,5])) == [1,2])
    test(Set([1,2]).issubset(Set([3,4,5])) == False)

    test(Set([1,2,3]).issuperset(Set([1,2,3])) == [1,2,3]) 
    test(Set([1,2,3,4,5]).issuperset(Set([1,2])) == [1,2])
    test(Set([1,2]).issuperset(Set([3,4,5])) == [1,2,3,4,5])

    print(x.difference_update(y))
    #print(x.add(9))
