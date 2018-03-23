# Story

# Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.
# Task

# Write a function that returns both the minimum and maximum number of the given list/array. 

# from random import randint, shuffle

# def test(lst, res):
#   Test.assert_equals(min_max(lst), res, "tested on " + str(lst));

# Test.describe("min_max")
# Test.it("should work for some examples")
# test([1,2,3,4,5], [1,5])
# test([2334454,5], [5, 2334454])

# for i in xrange(0,20):
#     r = randint(0,100)
#     test([r], [r,r])

def min_max(lst):
  return_list = [] 
  lst.sort() 
  return_list.append(lst[0]) 
  return_list.append(lst[-1]) 
  return return_list

  

