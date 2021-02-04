import pytest

#function to add 2 numbers
def add_numbers(a,b):
  return a + b

def sub_numbers(a,b):
  return a - b

def test_add():
  assert add_numbers(1,3) == 4 

def test_sub():
  assert sub_numbers(1,3) == 1