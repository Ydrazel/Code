#-*- code: utf-8 -*-

class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return ('🍪' * int(self._size))
    
    def deposit(self, n):
        if self._capacity < n:
            raise ValueError
        else:
            self._size = (self._size + n)
        return self._size
    
    def withdraw(self, n):
        if n < 0:
            raise ValueError
        else:
            self._size = self._size - n
            if self._size < 0:
                raise ValueError
            else:
                return self._size
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self._size
