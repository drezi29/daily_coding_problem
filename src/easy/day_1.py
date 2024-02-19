'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
'''

from typing import List, Set


def if_numbers_add_up_to(number_list: List, k: int) -> bool:
    substract_result : List[int] = [k - number for number in number_list]
    results_union : Set[int] = set(number_list) & set(substract_result)
    return bool(results_union)
