import emoji

class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size
    # return how many cookies are in the jar
    def __str__(self):
        return f'{self.size * emoji.emojize(":cookie:")}'
    # add cookies 
    def deposite(self, n):
        self.n = n
        self.size = self.size + n
        return self.size * emoji.emojize(":cookie:")
    # remove cookies
    def withdraw(self, n):
        self.n = n
        self.size = self.size - n
        return self.size * emoji.emojize(":cookie:")
    # capacity of the jar (getter)
    @property
    def capacity(self):
        return self._capacity
    # set capacity of the jar
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("negative number")
        self._capacity = capacity
       
    @property
    def size(self):
        return self._size
        
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("too many cookies")
        self._size = size
    

        
i = Jar(12,0)
print(i.deposite(5))
print(i.deposite(5))
print(i.withdraw(2))
print(i)



