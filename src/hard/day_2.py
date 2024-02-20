'''
Given an array of integers, return a new array such that 
each element at index i of the new array is the product of all the numbers 
in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

import copy, math

from typing import List


def array_with_product_elements_with_division(given_array: List[int]) -> List[int]:
    product_of_all_elemets : int = math.prod(given_array)
    return [product_of_all_elemets // number for number in given_array]

def array_with_product_elements_without_division(given_array: List[int]) -> List[int]:
    result_array : List[int] = []
    for i in range(len(given_array)):
        given_array.insert(0, given_array.pop(i))
        result_array.append(math.prod(given_array[1:]))
    return result_array
