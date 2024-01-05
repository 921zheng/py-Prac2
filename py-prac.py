# # # 1. Task
# # # In this kata you will create a function that return True if two given strings are isomorphic to each other, and False otherwise. Remember that order is important.

# # # Your solution must be able to handle words with more than 10 characters.

# # # Example
# # # True:

# # # CBAABC DEFFED
# # # XXX YYY
# # # RAMBUNCTIOUSLY THERMODYNAMICS
# # # False:

# # # AB CC
# # # XXY XYY
# # # ABAB CD

# # def isomorph(a, b):
# #     return [a.index(x) for x in a] == [b.index(y) for y in b]
    

# # 2.Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

# # For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

# # The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

# # Based on: https://leetcode.com/problems/two-sum/

# # two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)


# # def two_sum(numbers, target):
# # 	for i in range(0,len(numbers)):
# #           for j in range(1, len(numbers)):
# #                 if i!=j and (numbers[i]+numbers[j])==target:
# #                     return i,j
                    
# # 3.An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

# # You have to write a function that receives a list, list size will always be at least 3 numbers. The missing term will never be the first or last one.

# # Example
# # find_missing([1, 3, 5, 9, 11]) == 7
# # PS: This is a sample question of the facebook engineer challenge on interviewstreet. I found it quite fun to solve on paper using math, derive the algo that way. Have fun!               
# # def find_missing(list):
# #     space=(list[len(list)-1]-list[0])/len(list)
# #     for i in range(len(list)):
# #         if list[i]+space!=list[i+1]:
# #             return list[i]+space               

# # 4. Background - the Collatz Conjecture:
# Imagine you are given a positive integer, n, then:

# if n is even, calculate: n / 2
# if n is odd, calculate: 3 * n + 1
# Repeat until your answer is 1. The Collatz conjecture states that performing this operation repeatedly, you will always eventually reach 1.

# You can try creating Collatz sequences with this kata. For further information, see the wiki page.

# Now! Your task:
# Given an array of positive integers, return the integer whose Collatz sequence is the longest.

# Example:

# longest_collatz([2, 4, 3])==3


# def longest(n):
#     count=0
#     while n!=1:
#         n=3 * n + 1 if n%2==1 else n//2
#         count+=1
#     return count

# def longest_collatz(arr):
#     return max(arr, key=longest)
















