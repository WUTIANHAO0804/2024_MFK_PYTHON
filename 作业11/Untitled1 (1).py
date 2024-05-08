#!/usr/bin/env python
# coding: utf-8

# In[1]:


#11.4
class GeomRange:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 1
            self.stop = args[0]
            self.step = 2
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 2
        else:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]

    def __iter__(self):
        return self.GeomRangeIterator(self.start, self.stop, self.step)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("index cannot be negative")

        value = self.start * (self.step ** index)
        if value < self.stop:
            return value
        else:
            raise IndexError("index is out of the progression")

    class GeomRangeIterator:
        def __init__(self, start, stop, step):
            self.start = start
            self.stop = stop
            self.step = step
            self.current = start

        def __next__(self):
            if self.current < self.stop:
                result = self.current
                self.current *= self.step
                return result
            else:
                raise StopIteration


# In[2]:


#11.3
class SpyingNumber:
    global_counter = 0

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"SpyingNumber({self.value})"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        SpyingNumber.global_counter += 1
        return SpyingNumber(self.value + other.value)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        SpyingNumber.global_counter += 1
        return SpyingNumber(self.value - other.value)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        SpyingNumber.global_counter += 1
        return SpyingNumber(self.value * other.value)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        SpyingNumber.global_counter += 1
        return SpyingNumber(self.value / other.value)

    @staticmethod
    def get_global_counter():
        return SpyingNumber.global_counter

    @staticmethod
    def reset_global_counter():
        SpyingNumber.global_counter = 0


# In[10]:


#11.2
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = float(age)

    def __str__(self):
        return f"Student {self.name} of age {self.age}"

    def __repr__(self):
        return f"Student({self.name}, {self.age})"


# In[3]:


# 11.1
class Incapsulator:
    def __init__(self, value=0):
        self._value = value

    def set_value(self, new_value):
        self._value = new_value

    def get_value(self):
        return self._value


# In[ ]:




